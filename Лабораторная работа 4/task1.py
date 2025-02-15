if __name__ == "__main__":
    class Vehicle:
        """
        Базовый класс для транспортных средств.
        """

        def __init__(self, make: str, model: str, year: int) -> None:
            """
            Инициализация объекта транспортного средства.

            :param make: Производитель транспортного средства
            :param model: Модель транспортного средства
            :param year: Год выпуска транспортного средства
            """
            self.make = make
            self.model = model
            self.year = year

        def __str__(self) -> str:
            """
            Возвращает строковое представление транспортного средства.
            """
            return f"{self.year} {self.make} {self.model}"

        def __repr__(self) -> str:
            """
            Возвращает официальное строковое представление объекта.
            """
            return f"Vehicle(make='{self.make}', model='{self.model}', year={self.year})"


    class Car(Vehicle):
        """
        Класс легкового автомобиля, наследующий от Vehicle.
        """

        def __init__(self, make: str, model: str, year: int, doors: int) -> None:
            """
            Инициализация легкового автомобиля.

            :param make: Производитель легкового автомобиля
            :param model: Модель легкового автомобиля
            :param year: Год выпуска легкового автомобиля
            :param doors: Количество дверей в легковом автомобиле
            """
            super().__init__(make, model, year)
            self._doors = doors  # Количество дверей сделано непубличным

        def __str__(self) -> str:
            """
            Возвращает строковое представление легкового автомобиля.
            В отличие от базового класса, добавляет количество дверей.
            """
            return f"{super().__str__()} with {self._doors} doors"

        def __repr__(self) -> str:
            """
            Возвращает официальное строковое представление легкового автомобиля.
            """
            return f"Car(make='{self.make}', model='{self.model}', year={self.year}, doors={self._doors})"

        def drive(self) -> str:
            """
            Симулирует движение автомобиля.

            :return: Сообщение о том, что автомобиль движется.
            """
            return f"The {self.make} {self.model} is now driving."

        def drive(self) -> str:
            """
            Перегруженный метод для симуляции движения автомобиля.
            Добавляет дополнительное сообщение с количеством дверей.

            :return: Сообщение о том, что автомобиль движется.
            """
            return f"The {self.make} {self.model} with {self._doors} doors is now driving."
    pass