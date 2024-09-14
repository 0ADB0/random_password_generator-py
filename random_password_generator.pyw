import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def show_password():
    password = generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(password_entry.get())

# Uygulama penceresi oluştur
app = tk.Tk()
app.title("Random Password Generator")

# Etiket
label = tk.Label(app, text="Click the button to generate a 15-character password:")
label.pack(pady=10)

# Şifre gösterim alanı
password_entry = tk.Entry(app, width=50)
password_entry.pack(pady=5)

# Şifre oluşturma butonu
generate_button = tk.Button(app, text="Generate Password", command=show_password)
generate_button.pack(pady=10)

# Şifreyi kopyalama butonu
copy_button = tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Uygulamayı çalıştır
app.mainloop()
