🔐 WordPress Brute Force Login Tester (GUI)
=================================================

Bu araç, WordPress giriş sayfalarına yönelik basit bir brute-force denemesi gerçekleştirmek için tasarlanmıştır. Eğitim ve farkındalık amaçlıdır. Arayüzü kullanıcı dostudur ve Tkinter ile geliştirilmiştir.

🧰 ÖZELLİKLER
---------------------
- 🖼️ Kullanıcı dostu grafik arayüz (Tkinter)
- 🔣 Rastgele şifre oluşturma:
  - Sadece sayı
  - Sadece harf
  - Sadece özel karakter
  - Sayı + harf
  - Tümü
- 📏 Şifre uzunluğu aralığı belirleme (Min / Max)
- ⏱️ Süre bazlı durdurma (timeout)
- 🔁 Maksimum deneme sınırı
- ✅ Başarılı girişleri "basarili_girisler.txt" dosyasına kaydetme

🚀 KULLANIM
---------------------
GEREKSİNİMLER:
    pip install requests

ÇALIŞTIRMA:
    python wp_bruteforce_dynamic.py

KULLANIM ADIMLARI:
1. WordPress sitenizin giriş URL'sini girin (örnek: https://siteadi.com)
2. Kullanıcı adını girin.
3. Şifre kombinasyonu için uzunluk ve karakter seçimi yapın.
4. Süre veya maksimum deneme sınırı belirleyin.
5. 🚀 Başlat butonuna tıklayın.

📁 KAYITLAR
---------------------
Başarılı bir giriş tespit edilirse şu formatta dosyaya kaydedilir:

Site: https://siteadi.com
Kullanıcı: admin
Şifre: denenenSifre123!
----------------------------------------

⚠️ SORUMLULUK REDDİ
---------------------
Bu araç yalnızca EĞİTİM, GÜVENLİK FARKINDALIĞI ve KENDİ SİSTEMLERİNİZİ TEST ETME amacıyla geliştirilmiştir.

❌ Bu aracı başkalarının izni olmadan herhangi bir sistem üzerinde kullanmak YASA DIŞIDIR.

👮‍♂️ Kullanım sonucunda doğabilecek HER TÜRLÜ YASAL SORUMLULUK tamamen kullanıcıya aittir.

📚 Lütfen yerel yasaları ve etik kuralları dikkate alarak kullanınız.

🧑‍💻 GELİŞTİRİCİ
---------------------
Bu araç "Ebubekir Bastama" tarafından hazırlanmıştır.
Katkı sağlamak veya geliştirme önerileri için lütfen iletişime geçin.

📜 LİSANS
---------------------
MIT Lisansı
