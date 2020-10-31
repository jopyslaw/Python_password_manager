import sqlite3
from crypt import Code



class Database():
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
    
    def create_table(self):
        query = "CREATE TABLE login_data (id INTEGER PRIMARY KEY AUTOINCREMENT, nazwa_portalu TEXT, login TEXT, password TEXT)"
        self.cursor.execute(query)
        self.connection.commit()
    
    def add_data(self, portal_name: str, login: str, password: str):
        code = Code()
        query = f"INSERT INTO login_data VALUES (NULL, '{portal_name}', '{login}','{code.code(password)}')"
        self.cursor.execute(query) 
        self.connection.commit()
        

    def read_data(self):
        code = Code()
        query = "SELECT * FROM login_data"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        new = []
        i = 0
        decode_pass = ''
        for password in result:
            new.append([password[0], password[1], password[2], password[3]])
        
        for passwd in new:
            decode_pass = code.decode(passwd[3])
            new[i][3] = decode_pass
            i += 1
        return new

    def delete_data(self, id):
        query = f"DELETE FROM login_data WHERE id = '{id}'"
        self.cursor.execute(query)
        self.connection.commit()
    
    def change_data(self, new_login, new_password, id):
        code = Code()
        query = f"UPDATE login_data SET login = '{new_login}', password = '{code.code(new_password)}' WHERE id = {id}"
        self.cursor.execute(query)
        self.connection.commit()

    def __del__(self):
        self.connection.close()