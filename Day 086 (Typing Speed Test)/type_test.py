import tkinter as tk
import time

def start_typing():
    start_time = time.time()

    def check_typing(event):
        typed_text = text_entry.get("1.0", "end-1c")
        elapsed_time = time.time() - start_time
        words_per_minute = len(typed_text.split()) / (elapsed_time / 60)
        result_label.config(text=f"Your typing speed: {words_per_minute:.2f} words per minute")

    text_entry.bind("<KeyRelease>", check_typing)

root = tk.Tk()
root.title("Typing Speed Test")

text_entry = tk.Text(root, height=10, width=50)
text_entry.pack()

start_button = tk.Button(root, text="Start Typing", command=start_typing)
start_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
