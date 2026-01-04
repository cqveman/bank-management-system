import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Central Bank of Yemen')
        self.geometry('1280x720')

        self.container = tk.Frame(self)
        self.container.pack(fill='both', expand=True)