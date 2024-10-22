# TODO Найдите количество книг, которое можно разместить на дискете
max_weight = 1440000
weight_symbol = 4
count_symbol_in_str = 25
count_str_in_page = 50
count_pages_in_book = 100
total_weight = weight_symbol * count_symbol_in_str * count_str_in_page * count_pages_in_book
count_books = max_weight // total_weight
print("Количество книг, помещающихся на дискету:", count_books)
