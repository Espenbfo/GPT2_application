import tkinter as tk
from generator import generate_text

text = ""
window = tk.Tk()
text_box = tk.Text()
text_box.pack()
text_box.insert("1.0", text)

def onclick():
    text = text_box.get("0.0", tk.END)
    text = text[:-1]
    prev_length = len(text)
    new_text = generate_text(text)
    print(new_text[prev_length: ])
    text_box.delete("0.0", tk.END)
    text_box.insert("0.0", new_text)

button = tk.Button(window, text="click me", command=onclick)
button.pack()
window.mainloop()
