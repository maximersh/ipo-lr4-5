def calculate_sum(numbers_list):
    total_sum = 0  # Инициализируем переменную для хранения суммы.
    for number in numbers_list:  # Проходим по каждому числу в списке.
        total_sum += number  # Добавляем текущее число к общей сумме.
    return total_sum  # Возвращаем общую сумму.
numbers_list = [1, 2, 3, 4, 5]  # списoк чисел.
print(calculate_sum(numbers_list))  # Выводим сумму всех чисел в списке.