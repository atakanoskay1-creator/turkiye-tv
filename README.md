# Türkiye TV

24 kanal: TRT kanalları, ana ulusal Türk televizyonları ve haber kanalları. Her kanalın logosu ve yayın akışı (EPG) bilgisi listede tanımlıdır.

## Playlist adresi

M3U destekleyen oynatıcınızın playlist URL alanına şu adresi ekleyin:

```
https://raw.githubusercontent.com/atakanoskay1-creator/turkiye-tv/main/turkiye.m3u
```

Dosya güncellendiğinde aynı adres kullanılmaya devam eder; oynatıcıda listeyi yenilemek yeterlidir.

## Kanallar

**TRT:** TRT 1, TRT 2, TRT Haber, TRT Spor, TRT Spor Yıldız, TRT Çocuk, TRT Belgesel, TRT Müzik, TRT Türk, TRT Avaz.

**Ulusal:** ATV, Kanal D, Show TV, Star TV, NOW, TV8, Kanal 7, 360 TV, Beyaz TV.

**Haber:** NTV, Habertürk, Halk TV, TV100, TGRT Haber.

## Logo ve yayın akışı

- Logolar [tv-logo/tv-logos](https://github.com/tv-logo/tv-logos/tree/main/countries/turkey) deposundan `tvg-logo` ile gelir.
- Yayın akışı, listenin başındaki `url-tvg` adresinden (`https://iptv-epg.org/files/epg-tr.xml`) okunur ve kanallar `tvg-id` ile eşleşir. Oynatıcı `url-tvg` okumuyorsa bu adresi EPG ayarına elle ekleyin. Program bilgisi görünmeyen kanallarda EPG kaynağı o kanalı yayınlamıyor olabilir.

## Kaynaklar ve çalışma durumu

Adresler [iptv-org](https://github.com/iptv-org/iptv/blob/master/streams/tr.m3u), [Free-TV](https://github.com/Free-TV/IPTV/blob/master/lists/turkey.md) ve [discevisita](https://github.com/discevisita/iptv/blob/main/tr.m3u) listelerinden seçildi. Video bu depoda barındırılmaz; oynatıcı yayın adresine doğrudan bağlanır.

M3U dosyasının biçimi kontrol edilmiştir; akışlar Google TV/Nuvio üzerinde tek tek oynatılarak doğrulanmamıştır. Yayın adresleri değişebilir, bölge veya içerik hakları kısıtlamaları uygulanabilir. Bozulan URL aynı dosyada güncellenebilir.
