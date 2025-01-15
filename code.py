import tkinter as tk
from tkinter import messagebox
import time

# Тексты для двух языков
texts = {
    "en": {
        "title_label": "Title Text",
        "message_label": "Message Text",
        "generate_button": "Generate Message",
        "language_button": "Switch to Russian",
        "error_title": "Error",
        "success_title": "Success",
    },
    "ru": {
        "title_label": "Заголовок",
        "message_label": "Текст сообщения",
        "generate_button": "Создать сообщение",
        "language_button": "Переключить на английский",
        "error_title": "Ошибка",
        "success_title": "Успех",
    }
}

# Текущий язык (по умолчанию английский)
current_language = "en"

# Ваш оригинальный код
unnie = """
███████╗██████╗ ██████╗  ██████╗ ███████╗███╗   ██╗
██╔════╝██╔══██╗██╔══██╗██╔════╝ ██╔════╝████╗  ██║
█████╗  ██████╔╝██████╔╝██║  ███╗█████╗  ██╔██╗ ██║
██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══╝  ██║╚██╗██║
███████╗██║  ██║██║  ██║╚██████╔╝███████╗██║ ╚████║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
"""

def generate_message():
    title = title_entry.get()
    message = message_entry.get()

    if title and message:
        print(f"Generating {title} and {message}")
        time.sleep(1)
        messagebox.showerror(title, message)
    else:
        messagebox.showerror(texts[current_language]["error_title"], "Please fill in both fields!")

def switch_language():
    global current_language
    if current_language == "en":
        current_language = "ru"
    else:
        current_language = "en"
    update_ui()

def update_ui():
    title_label.config(text=texts[current_language]["title_label"])
    message_label.config(text=texts[current_language]["message_label"])
    generate_button.config(text=texts[current_language]["generate_button"])
    language_button.config(text=texts[current_language]["language_button"])

# Создание основного окна
root = tk.Tk()
root.title("Message Generator")
root.geometry("400x200")

# Элементы интерфейса
title_label = tk.Label(root, text=texts[current_language]["title_label"])
title_label.pack(pady=5)

title_entry = tk.Entry(root, width=40)
title_entry.pack(pady=5)

message_label = tk.Label(root, text=texts[current_language]["message_label"])
message_label.pack(pady=5)

message_entry = tk.Entry(root, width=40)
message_entry.pack(pady=5)

generate_button = tk.Button(root, text=texts[current_language]["generate_button"], command=generate_message)
generate_button.pack(pady=10)

language_button = tk.Button(root, text=texts[current_language]["language_button"], command=switch_language)
language_button.pack(pady=10)

# Запуск основного цикла
root.mainloop()
