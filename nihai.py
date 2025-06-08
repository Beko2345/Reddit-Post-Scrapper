import os
import requests
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import praw
import json
import urllib.parse
import shutil
import re
import threading
from moviepy.editor import VideoFileClip, AudioFileClip
import subprocess

CONFIG_FILE = "config.json"
DOWNLOADED_IDS_FILE = "downloaded_ids.json"
LOG_FILE = "log.txt"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_config(data):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_downloaded_ids():
    if os.path.exists(DOWNLOADED_IDS_FILE):
        with open(DOWNLOADED_IDS_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()

def save_downloaded_ids(ids):
    with open(DOWNLOADED_IDS_FILE, "w", encoding="utf-8") as f:
        json.dump(list(ids), f)

def write_log(message, widget):
    widget.insert(tk.END, message)
    widget.see(tk.END)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message)

def download_media(media_url, save_path):
    try:
        r = requests.get(media_url, stream=True)
        if r.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
            return True
        else:
            return f"Status code {r.status_code}"
    except Exception as e:
        return str(e)

def extract_gallery_images(submission):
    media_metadata = submission.media_metadata
    gallery_urls = []
    if media_metadata:
        for item in media_metadata.values():
            if 's' in item and 'u' in item['s']:
                url = item['s']['u']
                decoded_url = urllib.parse.unquote(url.replace("&amp;", "&"))
                gallery_urls.append(decoded_url)
    return gallery_urls

def download_reddit_video_with_ytdlp(url, save_path, log_widget):
    try:
        cmd = ["yt-dlp", "-f", "bv+ba", url, "-o", save_path]
        subprocess.run(cmd, check=True)
        write_log(f"  yt-dlp ile video indirildi: {url}\n", log_widget)
        return True
    except subprocess.CalledProcessError as e:
        write_log(f"  yt-dlp başarısız: {url} → {e}\n", log_widget)
        return False

def archive_subreddit(subreddit_name, client_id, client_secret, user_agent, keyword, log_widget):
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent)

    subreddit = reddit.subreddit(subreddit_name)

    downloaded_ids = load_downloaded_ids()

    subreddit_folder = os.path.join("posts", subreddit_name)
    os.makedirs(subreddit_folder, exist_ok=True)

    for submission in subreddit.new(limit=None):
        if submission.id in downloaded_ids:
            continue

        if keyword and keyword.lower() not in submission.title.lower():
            continue

        write_log(f"Post indiriliyor: {submission.title}\n", log_widget)

        post_folder = os.path.join(subreddit_folder, submission.id)
        os.makedirs(post_folder, exist_ok=True)

        with open(os.path.join(post_folder, "post.txt"), "w", encoding="utf-8") as f:
            f.write(f"Title: {submission.title}\n\n")
            f.write(f"Selftext: {submission.selftext}")

        submission.comments.replace_more(limit=0)
        with open(os.path.join(post_folder, "comments.txt"), "w", encoding="utf-8") as f:
            for comment in submission.comments.list():
                f.write(f"{comment.author}: {comment.body}\n\n")

        media_dir = os.path.join(post_folder, "media")
        os.makedirs(media_dir, exist_ok=True)

        if hasattr(submission, 'is_gallery') and submission.is_gallery:
            gallery_urls = extract_gallery_images(submission)
            for idx, url in enumerate(gallery_urls):
                ext = url.split(".")[-1].split("?")[0]
                path = os.path.join(media_dir, f"gallery_{idx}.{ext}")
                result = download_media(url, path)
                if result is True:
                    write_log(f"  Gallery görsel indirildi: {url}\n", log_widget)
                else:
                    write_log(f"  Gallery görsel indirilemedi: {url} → {result}\n", log_widget)

        elif submission.url:
            url = submission.url
            if any(ext in url for ext in [".jpg", ".jpeg", ".png", ".gif", ".mp4"]):
                ext = url.split(".")[-1].split("?")[0]
                path = os.path.join(media_dir, f"media.{ext}")
                result = download_media(url, path)
                if result is True:
                    write_log(f"  Medya indirildi: {url}\n", log_widget)
                else:
                    write_log(f"  Medya indirilemedi: {url} → {result}\n", log_widget)

            elif "v.redd.it" in url:
                output_template = os.path.join(media_dir, "video_with_audio.%(ext)s")
                success = download_reddit_video_with_ytdlp(url, output_template, log_widget)
                if not success:
                    write_log(f"  Reddit video indirilemedi (yt-dlp ile de): {url}\n", log_widget)

        downloaded_ids.add(submission.id)
        save_downloaded_ids(downloaded_ids)

# GUI
root = tk.Tk()
root.title("Reddit Arşivleyici")
root.geometry("600x700")

labels = ["Subreddit Adı:", "Client ID:", "Client Secret:", "User Agent:", "🔑 Sadece bu kelimeyi içeren postları indir:"]
entries = []
config = load_config()

for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.pack()
    entry = tk.Entry(root, width=60)
    key = ["subreddit", "client_id", "client_secret", "user_agent", "keyword"][i]
    entry.insert(0, config.get(key, ""))
    entry.pack()
    entries.append(entry)

def start_download_thread():
    threading.Thread(target=start_download, daemon=True).start()

def start_download():
    subreddit_name = entries[0].get()
    client_id = entries[1].get()
    client_secret = entries[2].get()
    user_agent = entries[3].get()
    keyword = entries[4].get()

    config_data = {
        "subreddit": subreddit_name,
        "client_id": client_id,
        "client_secret": client_secret,
        "user_agent": user_agent,
        "keyword": keyword
    }
    save_config(config_data)

    if not os.path.exists("posts"):
        os.makedirs("posts")

    write_log("\n--- İndirme işlemi başladı ---\n", log_widget)
    archive_subreddit(subreddit_name, client_id, client_secret, user_agent, keyword, log_widget)
    write_log("--- Tüm uygun postlar indirildi ---\n", log_widget)

button = tk.Button(root, text="⬇️ Postları İndir", command=start_download_thread)
button.pack(pady=10)

log_widget = scrolledtext.ScrolledText(root, width=80, height=20)
log_widget.pack()

root.mainloop()
