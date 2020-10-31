from tkinter import *
from database import Database
from dotenv import load_dotenv
from os import getenv

load_dotenv()

class Mygui():
    def __init__(self, master):
        #Stworzenie ramki
        self.app = Frame(master)
        self.app.grid()
        self.create_widgets()
    

    def create_widgets(self):
        #Główny tytuł
        self.main_label = Label(self.app, text = "Witaj w menedżerze haseł!")
        self.main_label.grid(row = 0, column = 1, sticky = N)
        #Następny tytuł
        self.instruction_label = Label(self.app, text="Podaj nazwę strony, login oraz hasło")
        self.instruction_label.grid(row = 1, column = 1, sticky = N)
        #Pola do wpisania 
        self.website_name = Entry(self.app)
        self.website_name.grid(row = 2, column = 0, sticky = W)

        self.login = Entry(self.app)
        self.login.grid(row = 2, column = 1, sticky = N)

        self.password = Entry(self.app)
        self.password.grid(row = 2, column = 2, sticky = N)


        #Przycisk do dodania nowych danych
        self.add_button = Button(self.app, text="Dodaj", command=self.return_values)
        self.add_button.grid(row = 2, column = 3, sticky = E)


        # Miejsce do wyświetlenia nowych danych
        self.radio_label = Label(self.app, text ="Wybierz")
        self.radio_label.grid(row = 3, column = 0, sticky = N)

        self.label_website = Label(self.app, text = "Nazwa strony")
        self.label_website.grid(row = 3, column = 1, sticky=N)

        self.label_login_1 = Label(self.app, text = "Login")
        self.label_login_1.grid(row = 3, column = 2, sticky = N)

        self.label_password_1 = Label(self.app, text = "Hasło")
        self.label_password_1.grid(row = 3, column = 3, sticky = N)

        self.bt = Button(self.app, text="Edytuj", command=self.edit)
        self.bt.grid(row = 2, column = 5, sticky = E)
        self.bt_2 = Button(self.app, text="Usuń", command=self.delete)
        self.bt_2.grid(row = 2, column = 6, sticky = E)

        self.display_data()
        


    def display_data(self):
        
        db = Database(getenv('DB_NAME'))
        row = 4
        column = 0
        self.radio_value = StringVar()
        self.radio_value.set(None)
        for data in db.read_data():
            Radiobutton(self.app, variable = self.radio_value, value = data[0]).grid(row = row, column = column)
            self.info_1 = Label(self.app, text = data[1])
            self.info_1.grid(row = row, column = column+1, sticky = N)
            self.info_2 = Label(self.app, text = data[2])
            self.info_2.grid(row = row, column = column+2, sticky = N)
            self.info_3 = Label(self.app, text = data[3])
            self.info_3.grid(row = row, column = column+3, sticky = N)
            row += 1



    def return_values(self):
        db = Database(getenv('DB_NAME'))
        db.add_data(self.website_name.get(), self.login.get(), self.password.get())
        self.website_name.delete(0,END)
        self.login.delete(0,END)
        self.password.delete(0,END)
        self.display_data()
    

    def edit(self):
        db = Database(getenv('DB_NAME'))
        db.change_data( self.login.get(), self.password.get(), self.radio_value.get())
        self.website_name.delete(0,END)
        self.login.delete(0,END)
        self.password.delete(0,END)
        self.display_data()

    def delete(self):
        db = Database(getenv('DB_NAME'))
        db.delete_data(self.radio_value.get())
        self.display_data()
    
    
