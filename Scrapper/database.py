import sqlite3
import pandas as pd # Patogus konverteris

class BookDatabase:
    def __init__(self, db_name="books.db"):      # Inicializacija DB
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):                      # Vienkartinis veiksmas; paruošti lentelė; atliekama inicializacijos metu
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                price REAL NOT NULL,
                rating INTEGER,
                availability TEXT,
                category TEXT,
                scraped_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def insert_books(self, books_list):         # Patalpinimas knygos į DB
        query = """
            INSERT INTO books (title, price, rating, availability, category)
            VALUES (?, ?, ?, ?, ?)
        """
        data = [(b["title"], b["price"], b["rating"], b["availability"], b["category"]) for b in books_list]  # Lupinam DICT sąraša ir formuojam naują kortėžą "data".  
        self.cursor.executemany(query, data)                                                                  # executemany padeda į DB musų kortėžų paketą "data" visą iškart 
        self.conn.commit()                                                                                    # Fiksuojami tranzakcijos

    def export_to_csv(self, filename="books.csv"):
        df = pd.read_sql_query("SELECT * FROM books", self.conn)                   # Panda siunčia užklausą į DB ir iškart formuoja lentelę "df"
        df.to_csv(filename, index=False)                                           # Išsaugome "df" lentelę kaip CSV

    def get_statistics(self):
        stats = {}

        stats["total_books"] = self.cursor.execute("SELECT COUNT(*) FROM books").fetchone()[0]      # Iš užklausos paimam pirmą eilutę ir jos pirmą elementą
        stats["average_price"] = self.cursor.execute("SELECT AVG(price) FROM books").fetchone()[0]  # Iš užklausos paimam pirmą eilutę ir jos pirmą elementą
        stats["most_common_rating"] = self.cursor.execute("""
            SELECT rating, COUNT(*) as cnt FROM books GROUP BY rating ORDER BY cnt DESC LIMIT 1
        """).fetchone()                                                                             # Iš užklausos paimam pirmą eilutę

        stats["books_per_category"] = self.cursor.execute("""
            SELECT category, COUNT(*) FROM books GROUP BY category
        """).fetchall()                                                                             # Grąžinamas kortežų sąrašas (fetchall)

        return stats

    def close(self):
        self.conn.close()                                                                           # Susijungimo su DB uždarymas atlaisvima resursus.                        
