numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

total_sum = sum(x for x in numbers if x is not None)

count = len(numbers)

average = total_sum / count

none_index = numbers.index(None)
numbers[none_index] = round(average, 2)

print("Измененный список:", numbers)

