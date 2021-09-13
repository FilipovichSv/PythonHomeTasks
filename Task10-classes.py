from datetime import datetime


class Book:
    """Class about book."""

    __count = 0
    def __init__(self, id_book: int, title: str, authors: str, publishing_house: str, year: int, pages_number: int,
                 price: float, binding: str) -> None:
        """Initialization."""
        self.__id_book = id_book
        self.__title = title
        self.__authors = authors
        self.__publishing_house = publishing_house
        self.__year = year
        self.__pages_number = pages_number
        self.__price = price
        self.__binding = binding
        Book.__count += 1
        print("Создан экземпляр класса, показание счетчика экземпляров:", Book.__count)

    def __setattr__(self, key, value):
        """Redefinition __setattr__."""
        if key == '_Book__id_book':
            self.__dict__[key] = value
            print("Вы установили для поля {0}, значение {1}".format(key, value))
        elif key == '_Book__title':
            self.__dict__[key] = value
            print("Вы установили для поля {0}, значение {1}".format(key, value))
        elif key == '_Book__authors':
            self.__dict__[key] = value
            print("Вы установили для поля {0}, значение {1}".format(key, value))
        elif key == '_Book__publishing_house':
            self.__dict__[key] = value
            print("Вы установили для поля {0}, значение {1}".format(key, value))
        elif key == '_Book__year':
            self.__dict__[key] = value
            print("Вы установили для поля {0}, значение {1}".format(key, value))
        elif key == '_Book__pages_number':
            self.__dict__[key] = value
            print("Вы установили для поля {0}, значение {1}".format(key, value))
        elif key == '_Book__price':
            self.__dict__[key] = value
            print("Вы установили для поля {0}, значение {1}".format(key, value))
        elif key == '_Book__binding':
            self.__dict__[key] = value
            print("Вы установили для поля {0}, значение {1}".format(key, value))
        else:
            raise AttributeError

    def get_id_book(self) -> str:
        """Getter for id_book field."""
        return "Значение поля id_book, это :{}".format(self.__id_book)

    def get_title(self) -> str:
        """Getter for title field."""
        return "Значение поля title, это :{}".format(self.__title)

    def set_author(self, value: str) -> None:
        """Setter for authors field."""
        if isinstance(value, str):
            print("Устанавливаю полю authors значение:", value)
            self.__authors = value
        else:
            raise ValueError("Некорректное значение для поля authors.")

    def set_pages_number(self, value: int) -> None:
        """Setter for pages_number field."""
        if isinstance(value, int) and value > 0:
            print("Устанавливаю полю authors значение:", value)
            self.__pages_number = value
        else:
            raise ValueError("Некорректное значение для поля pages_number.")

    def set_year(self, value: int) -> None:
        """Setter for year field."""
        if isinstance(value, int) and value <= datetime.datetime.now().year:
            print("Устанавливаю полю year значение:", value)
            self.__year = value
        else:
            raise ValueError

    @property
    def full_info(self):
        """Return full info about book as attr(only for reading)."""
        return '{}, {}, {}, {}, {}, {}, {}, {}.'.format(self.__id_book, self.__title, self.__authors,
                                                        self.__publishing_house, self.__year, self.__pages_number,
                                                        self.__price, self.__binding)

    def __str__(self):
        """String representation of object."""
        return self.__title

    def __del__(self) -> None:
        """Object destruction."""
        Book.__count -= 1
        print("Удален экземпляр класса, показание счетчика экземпляров:", Book.__count)


a = Book(0, 'Война и мир', 'Лев Толстой', 'АВЕРСЭВ', 1880, 1000, 621, 'Твердая')
print(a.full_info)
a.set_author('5')
print(a.full_info)
