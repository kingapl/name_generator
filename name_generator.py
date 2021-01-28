import tkinter as tk
import csv
from random import choice

class NameGenerator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("400x400")
        self.master.title("Name generator")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self, text="Generator imion", font="Arial 20 bold", fg="#6f02a6", pady=20)
        self.title.grid(row=0, column=0, columnspan=2)

        self.name_label = tk.Label(self, text="Imię...", font="Arial 12", pady=10)
        self.name_label.grid(row=1, column=0)

        self.radiobutton = tk.StringVar()
        self.f_radio = tk.Radiobutton(self, text="damskie", value="female", variable=self.radiobutton)
        self.f_radio.grid(row=2, column=0)
        self.m_radio = tk.Radiobutton(self, text="męskie", value="male", variable=self.radiobutton)
        self.m_radio.grid(row=3, column=0)

        self.draw_button = tk.Button(self, text="Losuj", command=self.draw_name, font="Arial 12", bg="#6f02a6", fg="#e7e3e8")
        self.draw_button.grid(row=4, column=0, pady=10)

        self.name_var = tk.StringVar()
        self.name_entry = tk.Entry(self, text=self.name_var, font="Arial 12")
        self.name_entry.grid(row=1, column=1)


    def draw_name(self):
        r_btn = self.radiobutton.get()
        
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
                    "J", "K", "L", "Ł", "M", "N", "O", "P", 
                    "R", "S", "Ś", "T", "U", "W", "Z", "Ż"]

        letter = choice(letters)
        names = []

        if r_btn:
            with open(f'{r_btn}_names.csv', 'r') as names_file:
                reader = csv.DictReader(names_file, delimiter=';')

                for row in reader:
                    if row[letter] != '':
                        names.append(row[letter])
                    else:
                        break

            self.name = choice(names)
            self.name_var.set(self.name)


root = tk.Tk()
name_generator = NameGenerator(master=root)
name_generator.mainloop()