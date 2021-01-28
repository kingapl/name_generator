import tkinter as tk

class NameGenerator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("400x400")
        self.master.title("Name generator")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self, text="Generator imion")
        self.title.grid(row=0, column=0, columnspan=2)

        self.name_label = tk.Label(self, text="Imię...")
        self.name_label.grid(row=1, column=0)

        #self.radiobutton_var = tk.StringVar()
        self.f_radio = tk.Radiobutton(self, text="damskie", value=1)
        self.f_radio.grid(row=2, column=0)
        self.m_radio = tk.Radiobutton(self, text="męskie", value=2)
        self.m_radio.grid(row=3, column=0)

        self.draw_button = tk.Button(self, text="Losuj")
        self.draw_button.grid(row=4, column=0)

        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1)


root = tk.Tk()
name_generator = NameGenerator(master=root)
name_generator.mainloop()