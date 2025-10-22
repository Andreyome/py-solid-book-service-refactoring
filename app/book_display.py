from abc import abstractmethod, ABC

from app.book import Book


class BaseDisplay(ABC):
    @abstractmethod
    def display(self, book: Book):
        pass


class ConsoleDisplay(BaseDisplay):
    def display(self, book: Book):
        print(book.content)


class ReverseDisplay(BaseDisplay):
    def display(self, book: Book):
        print(book.content[::-1])
