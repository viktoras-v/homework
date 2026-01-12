from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


# Setup Database
engine = create_engine("sqlite:///books.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define Book object
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer)

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}', year={self.year})>"

# Create table
Base.metadata.create_all(engine)

# 3. Functions add, update delete
def add_book(title, author, year):
    book = Book(title=title, author=author, year=year)
    session.add(book)
    session.commit()
    print(f"Added: {book}")


def view_books():
    books = session.query(Book).all()
    if not books:
        print("No books found.")
    for book in books:
        print(book)


def update_book(book_id, title=None, author=None, year=None):
    book = session.query(Book).filter_by(id=book_id).first()
    if not book:
        print(f"No book found with id {book_id}")
        return
    if title: book.title = title
    if author: book.author = author
    if year: book.year = year
    session.commit()
    print(f"Updated: {book}")


def delete_book(book_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if not book:
        print(f"No book found with id {book_id}")
        return
    session.delete(book)
    session.commit()
    print(f"Deleted book with id {book_id}")


# Example
if __name__ == "__main__":
    # Add book
    add_book("Brisiaus galas", "jjonas Biliunas", 1905)

    print("\nAll books:")
    view_books()

    # Update a book
    update_book(1, year=1906)

    print("\nBooks after update:")
    view_books()

    # Close session
    session.close()
