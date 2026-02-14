class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Название книги (только для чтения)."""
        return self._name

    @property
    def author(self) -> str:
        """Автор книги (только для чтения)."""
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Бумажная книга."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # используем сеттер для проверки

    @property
    def pages(self) -> int:
        """Количество страниц."""
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value

    def __str__(self) -> str:
        # Добавляем информацию о страницах
        return f"Книга {self.name}. Автор {self.author}. {self.pages} стр."

    def __repr__(self) -> str:
        # Полное представление с учётом pages
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, pages={self.pages!r})")


class AudioBook(Book):
    """Аудиокнига."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # используем сеттер для проверки

    @property
    def duration(self) -> float:
        """Длительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError("Длительность должна быть числом")
        # Приводим к float для единообразия
        value = float(value)
        if value <= 0:
            raise ValueError("Длительность должна быть положительной")
        self._duration = value

    def __str__(self) -> str:
        # Добавляем информацию о длительности
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration} ч."

    def __repr__(self) -> str:
        # Полное представление с учётом duration
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, duration={self.duration!r})")