# TODO Найдите количество книг, которое можно разместить на дискете
# Расчет объема одной книги
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

# Объем одной книги в байтах
book_size_bytes = pages * lines_per_page * chars_per_line * bytes_per_char

# Объем дискеты в байтах (1,44 Мб = 1,44 * 1024 * 1024 байт)
floppy_size_bytes = 1.44 * 1024 * 1024

# Расчет количества книг
books_count = int(floppy_size_bytes // book_size_bytes)

print("Количество книг, помещающихся на дискету:", books_count)
