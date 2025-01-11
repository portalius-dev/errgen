import tkinter
from tkinter import messagebox
import time

unnie = """
███████╗██████╗ ██████╗  ██████╗ ███████╗███╗   ██╗
██╔════╝██╔══██╗██╔══██╗██╔════╝ ██╔════╝████╗  ██║
█████╗  ██████╔╝██████╔╝██║  ███╗█████╗  ██╔██╗ ██║
██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══╝  ██║╚██╗██║
███████╗██║  ██║██║  ██║╚██████╔╝███████╗██║ ╚████║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
"""

print(unnie)

time.sleep(1)

while True:
    title = input("Title Text - ")
    message = input("Message Text - ")

    print("Generating " + title + " and " + message)
    time.sleep(1)

    messagebox.showerror(title, message)
