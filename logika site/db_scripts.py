import sqlite3


class DatabaseManager:
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()
        self.dbname= dbname
    def open(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_image(self):
        self.open()
        self.cursor.execute("""SELECT image FROM main""")
        data = self.cursor.fetchone()
        self.close()
        return data