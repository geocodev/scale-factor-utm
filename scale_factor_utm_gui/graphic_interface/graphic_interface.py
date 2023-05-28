import tkinter as tk
from PIL import ImageTk, Image

class TkinterApp:
    def __init__(self):
        self.root=tk.Tk()

    def create_button(self, value, function):
        button = tk.Button(self.root, text=value, command=function)
        button.pack()

    def create_window(self, Title, Width, Height):
        self.root.title(Title)
        self.root.geometry(f'{Width}x{Height}')


    def create_frame(self):
        frame = tk.Frame(self.root)
        frame.pack()
        return frame

    def create_entry(self, Var=None, Justify=''):
        entry = tk.Entry(self.root, textvariable=Var, justify=Justify)
        entry.pack()

    def create_label(self, Text):
        label_text = tk.Label(self.root, text=Text)
        label_text.pack()

    def insert_image(self, pathimage):
        logo = Image.open(pathimage)
        logo = ImageTk.PhotoImage(logo)
        label_logo = tk.Label(self.root, image=logo)
        label_logo.pack()

    def run_app(self):
        self.root.mainloop()

