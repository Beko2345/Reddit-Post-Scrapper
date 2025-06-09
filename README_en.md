# Reddit Archiver (Python GUI Application)

This project, belirli bir subreddit’teki ya da kullanıcıya ait Reddit gönderilerini indirip organize bir şekilde arşivleyen gelişmiş bir **masaüstü uygulamasıdır.** `tkinter` GUI ile kullanıcı dostu bir arayüz sunar.

---

## 🎯 Features

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

## 🖥️ Usage

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

## 📂 Output Structure

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

## 🔒 Required Reddit API Credentials

- `client_id`
- `client_secret`
- `user_agent`

You can generate these credentials from [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps) .

---

## 🔎 Additional Tool: Reddit Post Search Tool (`post_arama_gui.py`)

Bu araç, `reddit_user_archiver.py` ile indirilen `.txt` dosyaları içinde **anahtar kelimeyle metin araması** yapmanızı sağlar.

### 🧩 Features

- 📂 Belirlediğiniz ana klasör altında `.txt` uzantılı tüm dosyalarda kelime arar.
- ✅ Eşleşen dosyaları listeler ve bulunduğu klasörü tek tıklamayla açmanıza imkân tanır.
- 🧠 Geniş Reddit arşivleri içinde hızlıca konu bazlı içerik bulmanıza yardımcı olur.

### 🖥️ Usage

```bash
python post_arama_gui.py
```

Program açıldığında:
1. Type the keyword you want to search for.
2. Select the main directory where the posts are stored.
3. Matching files will be listed and can be opened with a click.
