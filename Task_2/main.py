"""Створюємо функцію, яка буде аналізувати текст, ідентифікувати всі дійсні числа, 
що вважаються частинами доходів, і повертати їх як генератор.
"""

# імпортуємо бібліотеку typing та re
from typing import Callable
import re

# Функція для створення генератора чисел із тексту
def generator_numbers(text: str):
    # Використовуємо регулярний вираз для пошуку всіх дійсних чисел у тексті
    pattern = r"\d+\.\d+|\d+"
    matches = re.findall(pattern, text)

    # Повертаємо генератор, що ітерує по знайдених числах
    for match in matches:
        yield float(match)


# Функція для підсумовування всіх чисел з тексту
def sum_profit(text: str, func: Callable):
    return sum(func(text))

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")