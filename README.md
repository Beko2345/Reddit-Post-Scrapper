# Reddit Arşivleyici (GUI'li Python Uygulaması)

Bu proje, belirli bir subreddit’teki ya da kullanıcıya ait Reddit gönderilerini indirip organize bir şekilde arşivleyen gelişmiş bir **masaüstü uygulamasıdır.** `tkinter` GUI ile kullanıcı dostu bir arayüz sunar.

---

## 🎯 Özellikler

- ✅ Subreddit veya kullanıcı bazlı içerik arşivleme
- ✅ Belirli bir kelimeyi içeren gönderileri filtreleyebilme
- ✅ Banlı kullanıcılar için `author:username` yöntemi ile arama desteği
- ✅ Subreddit + Kullanıcı birlikte girildiğinde, sadece o subredditteki o kullanıcıya ait postlar indirilir
- ✅ Post başlıkları ve açıklamaları `.txt` dosyasına kaydedilir  
- ✅ Tüm yorumlar ayrı bir dosyaya kaydedilir  
- ✅ Görseller (.jpg, .png, .gif, .webp vs.) ve videolar indirilir  
- ✅ Galeri postları desteklenir  
- ✅ `v.redd.it` videoları `yt-dlp` ile indirilebilir ve ses+video birleştirilir  
- ✅ Her post subreddit bazlı kullanıcı klasörüne kaydedilir  
- ✅ Daha önce indirilen postlar tekrar indirilmez (`downloaded_ids.json` kontrolü)  
- ✅ Kullanıcı bilgileri (subreddit adı, kullanıcı adı, client ID vb.) hatırlanır (`config.json`)  
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
   python reddit_user_archiver.py
   ```

---

## 📂 Çıktı Yapısı

```
posts/
├── subreddit_adi/           # subreddit indiriliyorsa
│   └── post_id/
│       ├── post.txt
│       ├── comments.txt
│       └── media/
├── kullanıcı_adi/
│   └── subreddit_adi/       # kullanıcı indiriliyorsa
│       └── post_id/
│           ├── post.txt
│           ├── comments.txt
│           └── media/
```

---

## 🔒 Gereken Reddit API Bilgileri

- `client_id`
- `client_secret`
- `user_agent`

Bu bilgileri [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps) adresinden oluşturabilirsin.
