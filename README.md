# Reddit Arşivleyici (GUI'li Python Uygulaması)

Bu proje, belirli bir subreddit’teki tüm postları indirip organize bir şekilde arşivleyen, gelişmiş bir **masaüstü uygulamasıdır.** `tkinter` GUI ile kullanıcı dostu arayüz sunar.

---

## 🎯 Özellikler

- ✅ Post başlıkları ve açıklamaları `.txt` dosyasına kaydedilir  
- ✅ Tüm yorumlar ayrı bir dosyaya kaydedilir  
- ✅ Görseller (.jpg, .png, .gif, .webp vs.) ve videolar indirilir  
- ✅ Galeri postları desteklenir  
- ✅ `v.redd.it` videoları `yt-dlp` ile indirilebilir ve ses+video birleştirilir  
- ✅ Her post ayrı klasöre kaydedilir  
- ✅ Daha önce indirilen postlar tekrar indirilmez (`downloaded_ids.json` kontrolü)  
- ✅ Kullanıcı bilgileri (subreddit adı, client ID vb.) hatırlanır (`config.json`)  
- ✅ Tüm işlemler hem GUI'de hem `log.txt` dosyasında kayıt altına alınır  

---

## 🖥️ Kullanım

1. Terminalde sanal ortam oluştur:
   ```bash
   python -m venv env
   env\Scripts\activate  # Windows
   ```

2. Gerekli kütüphaneleri kur:
   ```bash
   pip install -r requirements.txt
   ```

3. Programı çalıştır:
   ```bash
   python nihai.py
   ```

---

## 📂 Çıktı Yapısı

```
posts/
└── subreddit_adi/
    └── post_id/
        ├── post.txt
        ├── comments.txt
        └── media/
            ├── media.jpg / gallery_0.png / video_with_audio.mp4
```

---

## 🔒 Gereken Reddit API Bilgileri

- `client_id`
- `client_secret`
- `user_agent`

Bu bilgileri [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps) adresinden oluşturabilirsin.
