import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS numeros (id INTEGER PRIMARY KEY, data text, nivell text, alergens text, tebarat text, ebastel text, simptomes text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM numeros")
        rows = self.cur.fetchall()
        return rows

    def insert(self, data, nivell, alergens, tebarat, ebastel, simptomes):
        self.cur.execute("INSERT INTO numeros VALUES (NULL, ?, ?, ?, ?, ?, ?)",(data, nivell, alergens, tebarat, ebastel, simptomes))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM numeros WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, data, nivell, alergens, tebarat, ebastel, simptomes):
        self.cur.execute("UPDATE numeros SET data = ?, nivell = ?, alergens = ?, tebarat = ?, ebastel = ?, simptomes = ? WHERE id = ?", (data, nivell, alergens, tebarat, ebastel, simptomes, id))
        self.conn.commit()
    def __del__(self):
        self.conn.close()

# db = Database("proba.db")
#db.insert("04/05/2020", "Baix", "Àcars", "Sí", "No", "Nas")
#db.insert("04/05/2020", "Alt", "Àcars", "No", "No", "Ulls")
#db.insert("04/05/2020", "Molt Alt", "Humitat", "Sí", "Sí", "Ulls i Nas")
#db.insert("04/05/2020", "Baix", "Humitat", "Sí", "Sí", "Ulls i Nas")
