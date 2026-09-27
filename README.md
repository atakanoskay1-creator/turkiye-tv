# Türkiye TV

128 kanal: TRT, ulusal, haber, ekonomi, spor, belgesel, çocuk, müzik, dini yayın ve yerel kanallar. Kanalların logosu ve yayın akışı (EPG) bilgisi listede tanımlıdır.

## Playlist adresi

M3U destekleyen oynatıcınızın playlist URL alanına şu adresi ekleyin:

```
https://raw.githubusercontent.com/atakanoskay1-creator/turkiye-tv/main/turkiye.m3u
```

Dosya güncellendiğinde aynı adres kullanılmaya devam eder; oynatıcıda listeyi yenilemek yeterlidir.

## Kanallar

**TRT:** TRT 1, TRT 2, TRT Haber, TRT Spor, TRT Spor Yıldız, TRT Çocuk, TRT Belgesel, TRT Müzik, TRT Türk, TRT Avaz, TRT World, TRT Arabi, TRT Kurdî, TRT 3, TRT Genç, TRT Diyanet Çocuk, TRT EBA İlkokul, TRT EBA Ortaokul, TRT EBA Lise.

**Ulusal:** ATV, Kanal D, Show TV, Star TV, NOW, TV8, Kanal 7, 360 TV, Beyaz TV, A2, TV4.

**Haber:** NTV, Habertürk, Halk TV, TV100, TGRT Haber, A Haber, Haber Global, 24 TV, Tele 1, TVNET, GZT, Bengütürk, TürkHaber, TBMM TV.

**Ekonomi:** Bloomberg HT, CNBC-e, Ekotürk.

**Spor:** A Spor, HT Spor, TJK TV, TJK TV 2.

**Belgesel:** DMAX, TLC, TGRT Belgesel.

**Çocuk:** Minika Çocuk, Minika Go.

**Müzik:** Kral Pop, Power Türk, Power TV, Power Türk Taptaze, Power Türk Slow, Power Türk Akustik, Power Dance, Power Love, Number1, Number1 Aşk, Number1 Damar, Number1 Dance, Dream Türk.

**Dini:** Diyanet TV, Semerkand TV.

**Yerel:** Aksu TV, Alanya Posta TV, Altas TV, Anadolu Net TV, ATV Alanya, Bir TV, BRTV, Bursa AS TV, Bursa TV, Çay TV, Çekmeköy TV, Deniz Postası TV, Diyar TV, Edessa TV, Er TV, ES TV, ETV Kayseri, ETV Manisa, Fortuna TV, Güneydoğu TV, Haber61 TV, Hunat TV, İçel TV, Kanal 3, Kanal 12, Kanal 15, Kanal 23, Kanal 26, Kanal 32, Kanal 33, Kanal 58, Kanal Fırat, Kanal V, Kay TV, Kent Türk TV, Kocaeli TV, Konya Olay TV, Life TV, Line TV, Mavi Karadeniz, Mercan TV, Meltem TV, MTürk TV, Natural TV, Olay Türk TV, On4 TV, Sun RTV, Tempo TV, Tivi 6, Ton TV, TV 1, TV 41, TV 42, TV 52, TV 264, Urfa Natik TV, Van 65 TV.

## Logo ve yayın akışı

- Logolar [tv-logo/tv-logos](https://github.com/tv-logo/tv-logos) deposundan `tvg-logo` ile gelir. Depoda logosu bulunmayan 33 kanalda (çoğu yerel kanal) logo yoktur.
- Yayın akışı, listenin başındaki `url-tvg` adresinden (`https://iptv-epg.org/files/epg-tr.xml`) okunur ve kanallar `tvg-id` ile eşleşir. Oynatıcı `url-tvg` okumuyorsa bu adresi EPG ayarına elle ekleyin. Program bilgisi görünmeyen kanallarda EPG kaynağı o kanalı yayınlamıyor olabilir.

## Kaynaklar ve çalışma durumu

Yerel kanallar genellikle 7/24 yayın yapmaz; bazıları yalnızca Türkiye'den izlenebilir.


Adresler [iptv-org](https://github.com/iptv-org/iptv/blob/master/streams/tr.m3u), [Free-TV](https://github.com/Free-TV/IPTV/blob/master/lists/turkey.md) ve [discevisita](https://github.com/discevisita/iptv/blob/main/tr.m3u) listelerinden seçildi. Video bu depoda barındırılmaz; oynatıcı yayın adresine doğrudan bağlanır.

M3U dosyasının biçimi kontrol edilmiştir; akışlar Google TV/Nuvio üzerinde tek tek oynatılarak doğrulanmamıştır. Yayın adresleri değişebilir, bölge veya içerik hakları kısıtlamaları uygulanabilir. Bozulan URL aynı dosyada güncellenebilir.
