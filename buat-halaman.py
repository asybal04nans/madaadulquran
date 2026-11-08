#!/usr/bin/env python3
"""Membuat halaman alat (waris.html, zakat.html, dalil.html) dari index.html.
Jalankan setiap kali index.html diubah:  python3 buat-halaman.py
"""
import re
BASE='https://asybal04nans.github.io/madaadulquran/'
HALAMAN={
 'waris.html':('waris','Kalkulator Waris Mazhab Syafi\'i - Yayasan Madaadul Qur\'an',
   'Kalkulator waris (faraid) menurut mazhab Syafi\'i dengan cara hitung langkah demi langkah. Gratis dari Yayasan Madaadul Qur\'an, Lembang.'),
 'zakat.html':('zakat','Kalkulator Zakat Mal dan Fitrah - Yayasan Madaadul Qur\'an',
   'Hitung zakat mal dan zakat fitrah dengan nisab emas terbaru. Gratis dari Yayasan Madaadul Qur\'an, Lembang.'),
 'dalil.html':('dalil','Cari Dalil Al-Qur\'an dan Hadis - Yayasan Madaadul Qur\'an',
   'Pustaka dalil terpilih: ayat Al-Qur\'an, hadis, dan pendapat ulama tentang infaq, zakat, waris, ibadah, dan akhlak.'),
}
src=open('index.html',encoding='utf8').read()
for fn,(fokus,judul,desk) in HALAMAN.items():
    s=src
    url=BASE+fn
    s=re.sub(r'<title>.*?</title>','<title>'+judul+'</title>',s,count=1)
    s=re.sub(r'(<meta name="description" content=")[^"]*(")',lambda m:m.group(1)+desk+m.group(2),s,count=1)
    s=re.sub(r'(<link rel="canonical" href=")[^"]*(")',lambda m:m.group(1)+url+m.group(2),s,count=1)
    s=re.sub(r'(<meta property="og:title" content=")[^"]*(")',lambda m:m.group(1)+judul+m.group(2),s,count=1)
    s=re.sub(r'(<meta property="og:description" content=")[^"]*(")',lambda m:m.group(1)+desk+m.group(2),s,count=1)
    s=re.sub(r'(<meta property="og:url" content=")[^"]*(")',lambda m:m.group(1)+url+m.group(2),s,count=1)
    s=s.replace('<script>\n/* Bagikan ke WhatsApp','<script>window.FOKUS=\''+fokus+'\'</script>\n<script>\n/* Bagikan ke WhatsApp',1)
    open(fn,'w',encoding='utf8').write(s)
    print('dibuat',fn)
pages=['']+list(HALAMAN)
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{BASE}{p}</loc></url>\n' for p in pages)+'</urlset>\n')
open('robots.txt','w').write('User-agent: *\nAllow: /\nSitemap: '+BASE+'sitemap.xml\n')
