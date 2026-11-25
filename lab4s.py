import random

# Создаём массив из 10 случайных чисел
numbers = [random.randint(-20, 20) for i in range(10)]

# Выводим исходный массив
print("Исходный массив:", numbers)

# Подсчитываем положительные, отрицательные числа и нули
positive = 0
negative = 0
zeros = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zeros += 1

# Выводим количество элементов
print("Положительных чисел:", positive)
print("Отрицательных чисел:", negative)
print("Нулей:", zeros)

# Находим минимальный и максимальный элементы
min_num = min(numbers)
max_num = max(numbers)

# Меняем минимальный и максимальный элементы местами
min_index = numbers.index(min_num)
max_index = numbers.index(max_num)

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

# Выводим изменённый массив
print("Массив после обмена min и max:", numbers)