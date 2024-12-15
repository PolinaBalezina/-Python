from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц в книге. Должно быть положительным целым числом.

        :raises ValueError: Если количество страниц не положительное.

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")

        self.title = title
        self.author = author
        self.pages = pages

    @abstractmethod
    def read_page(self) -> str:
        """
        Чтение одной страницы книги.

        :return: Страница книги.
        """


    @abstractmethod
    def get_summary(self) -> str:
        """
        Получение краткого содержания книги.

        :return: Краткое содержание.
        """


class Vehicle(ABC):
    def __init__(self, brand: str, model: str, year: int):
        """
        Создание и подготовка к работе объекта "Транспортное средство"

        :param brand: Бренд транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска. Должен быть положительным целым числом после 1885 года.

        :raises ValueError: Если год выпуска неверный.

        Примеры:
        >>> vehicle = Vehicle("Toyota", "Corolla", 2020)
        """
        if year < 1886:
            raise ValueError("Год выпуска должен быть 1886 или позже.")

        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def start(self) -> None:
        """
        Запуск двигателя транспортного средства.
        """


    @abstractmethod
    def stop(self) -> None:
        """
        Остановка двигателя транспортного средства.
        """


class Computer(ABC):
    def __init__(self, brand: str, processor: str, ram: int):
        """
        Создание и подготовка к работе объекта "Компьютер"

        :param brand: Бренд компьютера.
        :param processor: Процессор компьютера.
        :param ram: Объем оперативной памяти в гигабайтах. Должен быть положительным целым числом.

        :raises ValueError: Если объем памяти не положительный.

        Примеры:
        >>> computer = Computer("Apple", "M1", 16)
        """
        if ram <= 0:
            raise ValueError("Объем оперативной памяти должен быть положительным целым числом.")

        self.brand = brand
        self.processor = processor
        self.ram = ram

    @abstractmethod
    def power_on(self) -> None:
        """
        Включение компьютера.
        """


    @abstractmethod
    def power_off(self) -> None:
        """
        Выключение компьютера.
        """

if __name__ == "__main__":
    import doctest
    doctest.testmod()