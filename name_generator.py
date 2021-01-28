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
        self.title = tk.Label(self, text="Generator imion")
        self.title.grid(row=0, column=0, columnspan=2)

        self.name_label = tk.Label(self, text="Imię...")
        self.name_label.grid(row=1, column=0)

        #self.radiobutton_var = tk.StringVar()
        self.f_radio = tk.Radiobutton(self, text="damskie", value=1)
        self.f_radio.grid(row=2, column=0)
        self.m_radio = tk.Radiobutton(self, text="męskie", value=2)
        self.m_radio.grid(row=3, column=0)

        self.draw_button = tk.Button(self, text="Losuj", command=self.draw_name)
        self.draw_button.grid(row=4, column=0)

        self.name_var = tk.StringVar()
        self.name_entry = tk.Entry(self, text=self.name_var)
        self.name_entry.grid(row=1, column=1)


    def draw_name(self):
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
                    "Ł", "M", "N", "O", "P", "R", "S", "T", "U", "W", "Z", "Ż"]
        #print(len(letters))
        letter = choice(letters)
        #print(letter)
        names = []

        with open('female_names.csv', 'r') as female_names:
            reader = csv.DictReader(female_names, delimiter=';')

            for row in reader:
                #print(row[letter])
                if row[letter] != '':
                    names.append(row[letter])
                else:
                    break

        #print(names)
        #print(len(names))

        self.name = choice(names)
        #print(self.name)
        self.name_var.set(self.name)


root = tk.Tk()
name_generator = NameGenerator(master=root)
name_generator.mainloop()