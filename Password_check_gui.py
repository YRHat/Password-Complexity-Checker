import tkinter as tk
import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Count how many rules are broken
    errors = sum([length_error, uppercase_error, lowercase_error, digit_error, special_error])

    if errors == 0:
        return "✅ Strong Password", "green", "#ccffcc"
    elif errors <= 2:
        return "⚠️ Medium Password", "orange", "#fff0b3"
    else:
        return "❌ Weak Password", "red", "#ffcccc"

def on_key_release(event):
    password = entry.get()
    message, text_color, bg_color = check_password_strength(password)
    result_label.config(text=message, fg=text_color)
    entry.config(bg=bg_color)

# GUI Setup
root = tk.Tk()
root.title("Live Password Strength Checker")
root.geometry("450x200")
root.resizable(False, False)

tk.Label(root, text="Type Your Password:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
entry.pack()
entry.bind("<KeyRelease>", on_key_release)  # Real-time feedback

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=15)

root.mainloop()
