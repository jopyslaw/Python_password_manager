from dotenv import load_dotenv
from os import getenv, listdir
from database import Database
from interface import Mygui
from tkinter import *


load_dotenv()
dir_list = listdir()
db = Database(getenv("DB_NAME"))
root = Tk()
root.title("Menedżer haseł")
root.geometry("570x512")
gui = Mygui(root)

root.mainloop()





