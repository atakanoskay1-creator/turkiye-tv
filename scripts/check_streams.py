#!/usr/bin/env python3
"""turkiye.m3u içindeki yayın adreslerini kontrol eder ve Markdown rapor üretir."""
import concurrent.futures
import re
import sys
import urllib.error
import urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
TIMEOUT = 15


def parse(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    channels = []
    for i, line in enumerate(lines):
        if line.startswith("#EXTINF"):
            j = i + 1
            while j < len(lines) and lines[j].startswith("#"):
                j += 1
            group = re.search(r'group-title="([^"]*)"', line)
            channels.append({
                "name": line.rsplit(",", 1)[1].strip(),
                "group": group.group(1) if group else "",
                "url": lines[j].strip(),
            })
    return channels


def check(ch):
    req = urllib.request.Request(ch["url"], headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            body = r.read(4096)
            if b"#EXTM3U" not in body:
                return ch, "içerik M3U8 değil"
            return ch, None
    except urllib.error.HTTPError as e:
        return ch, f"HTTP {e.code}"
    except Exception as e:  # zaman aşımı, DNS, TLS vb.
        return ch, type(e).__name__ + (f": {e.reason}" if hasattr(e, "reason") else "")


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "turkiye.m3u"
    channels = parse(path)
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
        results = list(pool.map(check, channels))
    broken = [(ch, err) for ch, err in results if err]

    print(f"## Yayın kontrolü\n")
    print(f"{len(channels)} kanalın {len(channels) - len(broken)} tanesi yanıt verdi, {len(broken)} tanesi vermedi.\n")
    if broken:
        print("| Grup | Kanal | Hata | Adres |")
        print("|---|---|---|---|")
        for ch, err in sorted(broken, key=lambda x: (x[0]["group"], x[0]["name"])):
            print(f"| {ch['group']} | {ch['name']} | {err} | `{ch['url']}` |")
        print()
    print("Kontrol GitHub sunucularından (Türkiye dışı) yapılır. Yalnızca Türkiye'den açılan "
          "kanallar burada bozuk görünebilir; kaldırmadan önce oynatıcıda deneyin.")
    return len(broken)


if __name__ == "__main__":
    main()
