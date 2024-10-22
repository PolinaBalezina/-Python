numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers_first = [2, -93, -2, 8]
numbers_second = [-44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
count = len(numbers)
total_sum_ = sum(numbers_first) + sum(numbers_second)
average = total_sum_ / count
numbers [4] = average
print("Измененный список:", numbers)
