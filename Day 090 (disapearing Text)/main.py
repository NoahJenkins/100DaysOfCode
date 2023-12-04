import tkinter as tk

class TextDisappearApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Disappear App")

        self.text_label = tk.Label(root, text="Type something:")
        self.text_label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()
        self.entry.bind('<Key>', self.on_key_pressed)  # bind the key event

        self.text_timeout = None

    def on_key_pressed(self, event):
        # Reset the timeout each time a key is pressed
        if self.text_timeout:
            self.root.after_cancel(self.text_timeout)
        self.text_timeout = self.root.after(3000, self.clear_text)  # 3000 milliseconds = 3 seconds

    def clear_text(self):
        # Clear the text in the Entry widget after 3 seconds of inactivity
        self.entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = TextDisappearApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
