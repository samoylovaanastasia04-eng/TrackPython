"""
Модуль с примером наследования классов на примере транспортных средств.
"""

from typing import Optional, Union


class Vehicle:
    """
    Базовый класс, представляющий транспортное средство.

    Атрибуты:
        make (str): Марка транспортного средства.
        model (str): Модель транспортного средства.
        year (int): Год выпуска.
        _speed (float): Текущая скорость (непубличный атрибут, км/ч).
        _max_speed (float): Максимальная скорость (непубличный атрибут, км/ч).

    Инкапсуляция скорости обеспечивает контроль её изменения через методы,
    предотвращая прямое присваивание некорректных значений.
    """

    def __init__(self, make: str, model: str, year: int, max_speed: float = 180.0) -> None:
        """
        Инициализирует транспортное средство.

        Аргументы:
            make: Марка.
            model: Модель.
            year: Год выпуска.
            max_speed: Максимальная скорость (по умолчанию 180 км/ч).
        """
        self.make = make
        self.model = model
        self.year = year
        self._max_speed = max_speed
        self._speed = 0.0  # начальная скорость

    def __str__(self) -> str:
        """Возвращает краткое строковое представление транспортного средства."""
        return f"{self.make} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """Возвращает валидное Python-выражение для создания копии объекта."""
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, year={self.year}, max_speed={self._max_speed})"

    def start(self) -> str:
        """
        Запускает двигатель.

        Возвращает:
            Строку с сообщением о запуске.
        """
        return f"Двигатель {self.make} {self.model} запущен."

    def stop(self) -> str:
        """
        Останавливает двигатель и обнуляет скорость.

        Возвращает:
            Строку с сообщением об остановке.
        """
        self._speed = 0.0
        return f"Двигатель {self.make} {self.model} остановлен."

    def accelerate(self, delta: float) -> str:
        """
        Увеличивает скорость на указанную величину, но не выше максимальной.

        Аргументы:
            delta: Приращение скорости (км/ч).

        Возвращает:
            Строку с сообщением о новой скорости.

        Примечание:
            Если после увеличения скорость превышает максимальную,
            она устанавливается равной максимальной.
        """
        new_speed = self._speed + delta
        if new_speed > self._max_speed:
            self._speed = self._max_speed
            return f"Скорость достигла максимума: {self._speed} км/ч."
        self._speed = new_speed
        return f"Текущая скорость: {self._speed} км/ч."

    def get_speed(self) -> float:
        """Возвращает текущую скорость (км/ч)."""
        return self._speed


class Car(Vehicle):
    """
    Класс легкового автомобиля, наследующий Vehicle.

    Добавляет атрибут количества дверей.

    Атрибуты:
        doors (int): Количество дверей.
    """

    def __init__(self, make: str, model: str, year: int, doors: int, max_speed: float = 200.0) -> None:
        """
        Инициализирует легковой автомобиль.

        Расширяет конструктор базового класса, добавляя количество дверей.

        Аргументы:
            make: Марка.
            model: Модель.
            year: Год выпуска.
            doors: Количество дверей.
            max_speed: Максимальная скорость (по умолчанию 200 км/ч для легковых авто).
        """
        super().__init__(make, model, year, max_speed)
        self.doors = doors

    def __str__(self) -> str:
        """Перегружает строковое представление, добавляя информацию о дверях."""
        return f"{super().__str__()}, {self.doors} двери"

    def __repr__(self) -> str:
        """Перегружает repr для включения аргумента doors."""
        return (f"Car(make={self.make!r}, model={self.model!r}, year={self.year}, "
                f"doors={self.doors}, max_speed={self._max_speed})")

    # Наследуем метод start() без изменений (указано для демонстрации наследования)
    # def start(self) -> str:
    #     return super().start()

    def accelerate(self, delta: float) -> str:
        """
        Перегружает метод accelerate для легкового автомобиля.

        Причина перегрузки: легковые автомобили обычно имеют более плавный разгон,
        поэтому здесь добавлено ограничение на максимальное изменение скорости за один вызов (10 км/ч),
        что делает ускорение более реалистичным.

        Аргументы:
            delta: Желаемое приращение скорости.

        Возвращает:
            Строку с сообщением о новой скорости.
        """
        # Ограничиваем изменение скорости, чтобы симулировать плавность
        max_delta = 10.0
        if delta > max_delta:
            delta = max_delta
            print(f"Ускорение ограничено {max_delta} км/ч за шаг.")
        return super().accelerate(delta)


if __name__ == "__main__":
    # Демонстрация работы классов
    vehicle = Vehicle("Toyota", "Camry", 2020)
    print(vehicle)
    print(repr(vehicle))
    print(vehicle.start())
    print(vehicle.accelerate(30))
    print(vehicle.accelerate(200))
    print(vehicle.stop())

    print("-" * 30)

    car = Car("Honda", "Civic", 2021, doors=4)
    print(car)
    print(repr(car))
    print(car.start())
    print(car.accelerate(15))  # Будет ограничено до 10
    print(car.accelerate(5))
    print(car.stop())