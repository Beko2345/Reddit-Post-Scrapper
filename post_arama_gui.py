
import os
from tkinter import Tk, Entry, Button, Listbox, Scrollbar, END, Label, filedialog
from pathlib import Path

def search_posts():
    listbox.delete(0, END)
    query = entry.get().lower()
    base_dir = Path(filedialog.askdirectory(title="Postların bulunduğu ana klasörü seçin"))

    if not base_dir:
        return

    for subdir in base_dir.glob("*"):
        if subdir.is_dir():
            for txt_file in subdir.glob("*.txt"):
                try:
                    with open(txt_file, "r", encoding="utf-8") as f:
                        content = f.read().lower()
                        if query in content:
                            listbox.insert(END, f"{txt_file}")
                except Exception as e:
                    listbox.insert(END, f"HATA: {txt_file} ({e})")

def open_selected():
    import subprocess
    selection = listbox.curselection()
    if selection:
        file_path = listbox.get(selection[0])
        folder = os.path.dirname(file_path)
        subprocess.Popen(f'explorer "{folder}"')

root = Tk()
root.title("Reddit Post Arama")
root.geometry("600x400")

Label(root, text="Aranacak kelime:").pack()
entry = Entry(root, width=50)
entry.pack()

Button(root, text="Ara", command=search_posts).pack(pady=5)

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(root, width=80, height=15, yscrollcommand=scrollbar.set)
listbox.pack(pady=10)
scrollbar.config(command=listbox.yview)

Button(root, text="Klasörü Aç", command=open_selected).pack()

root.mainloop()
