from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "postgresql://n_dasha:24465336Kotiki@localhost:5432/librar")
Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True)
    first_name = Column(String(length=255))
    last_name = Column(String(length=255))

    def __repr__(self):
        return "<Author(auther_id='{0}',first_name='{1}', last_name='{2}'>".format(self.author_id, self.first_name, self.last_name)


class Book(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    title = Column(String(length=255))
    number_of_pages = Column(Integer)

    def __repr__(self):
        return "<Book(book_id='{0}',title='{1}', number_of_pages='{2}'>".format(self.book_id, self.title, self.number_of_pages)


class BookAuthor(Base):
    __tablename__ = 'bookauthors'
    bookauthor_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.author_id'))
    book_id = Column(Integer, ForeignKey('books.book_id'))

    author = relationship('Author')
    book = relationship('Book')

    def __repr__(self):
        return "<BookAuthor(bookauther_id='{0}',author_first_name='{1}', author_last_name='{2}',book_title='{3}'>".format(self.bookauthor_id, self.author.first_name, self.author.last_name, self.book.title)


Base.metadata.create_all(engine)


def create_session():
    session = sessionmaker(bind=engine)
    return session()


def add_book(title, number_of_pages, first_name, last_name):
    book = Book(title=title, number_of_pages=number_of_pages)
    session = create_session()
    try:
        existing_author = session.query(Author).filter(
            Author.first_name == first_name, Author.last_name == last_name).first()
        session.add(book)
        if existing_author is not None:
            session.flush()
            pairing = BookAuthor(
                author_id=existing_author.author_id, book_id=book.book_id)
        else:
            author = Author(first_name=first_name, last_name=last_name)
            session.add(author)
            session.flush()
            pairing = BookAuthor(
                author_id=author.author_id, book_id=book.book_id)
        session.add(pairing)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == '__main__':
    title = input('What is the title of the book? ')
    number_of_pages = int(input('How many pages does it have? '))
    first_name = input('What is the first name of the author? ')
    last_name = input('What is the last name of the author? ')
    add_book(title, number_of_pages, first_name, last_name)
