import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("My App")

        self.label = tk.Label(master, text="Hello, world!")
        self.label.pack()

        self.button = tk.Button(master, text="Quit", command=master.quit)
        self.button.pack()

root = tk.Tk()
app = App(root)
root.mainloop()
