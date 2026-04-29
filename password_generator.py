import secrets
import string
import tkinter as tk
from tkinter import messagebox

SPECIAL_CHARS = "!@#$%^&*"

# ── Generate Password ───────────────────
def generate_password(length):
    if length < 4:
        raise ValueError("Minimum length is 4")
    if length > 128:
        raise ValueError("Maximum length is 128")

    chars = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        SPECIAL_CHARS
    )

    while True:
        pwd = ''.join(secrets.choice(chars) for _ in range(length))

        if (any(c.islower() for c in pwd) and
            any(c.isupper() for c in pwd) and
            any(c.isdigit() for c in pwd) and
            any(c in SPECIAL_CHARS for c in pwd)):
            return pwd


# ── Generate Button Action ─────────────────────────────
def generate():
    try:
        length = int(length_entry.get())
        pwd = generate_password(length)
    except (ValueError, TypeError):
        messagebox.showerror("Error", "Enter valid number (4–128)")
        return

    password_var.set(pwd)


# ── Copy Password ──────────────────────────────────────
def copy_password():
    pwd = password_var.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied!")


# ── GUI Setup ──────────────────────────────────────────
root = tk.Tk()
root.title("Password Generator")
root.geometry("380x280")
root.config(bg="#1e1e1e")

password_var = tk.StringVar()

# Title
tk.Label(root, text="🔐 Password Generator",
         font=("Arial", 16, "bold"),
         bg="#1e1e1e", fg="cyan").pack(pady=10)

# Length input
tk.Label(root, text="Password Length:",
         bg="#1e1e1e", fg="white").pack()

length_entry = tk.Entry(root, justify="center")
length_entry.insert(0, "12")
length_entry.pack(pady=5)

# Generate button
tk.Button(root, text="Generate Password",
          command=generate,
          bg="cyan", fg="black").pack(pady=10)

# Output
tk.Entry(root, textvariable=password_var,
         width=30, justify="center",
         state="readonly",
         bg="#333", fg="black").pack(pady=5)

# Copy button
tk.Button(root, text="Copy",
          command=copy_password,
          bg="green", fg="white").pack(pady=10)

# Run app
root.mainloop()