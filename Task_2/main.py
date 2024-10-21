"""Створюємо функцію, яка буде аналізувати текст, ідентифікувати всі дійсні числа, 
що вважаються частинами доходів, і повертати їх як генератор.
Необхідно створити функцію generator_numbers, яка буде аналізувати текст, ідентифікувати всі дійсні числа, 
що вважаються частинами доходів, і повертати їх як генератор. Дійсні числа у тексті записані без помилок, 
чітко відокремлені пробілами з обох боків. Також потрібно реалізувати функцію sum_profit, 
яка буде використовувати generator_numbers для підсумовування цих чисел і обчислення загального прибутку.

Вимоги до завдання:

Функція generator_numbers(text: str) повинна приймати рядок як аргумент і повертати генератор, 
що ітерує по всіх дійсних числах у тексті. Дійсні числа у тексті вважаються записаними без помилок і 
чітко відокремлені пробілами з обох боків.
Функція sum_profit(text: str, func: Callable) має використовувати генератор generator_numbers 
для обчислення загальної суми чисел у вхідному рядку та приймати його як аргумент при виклику.

Рекомендації для виконання:

Використовуйте регулярні вирази для ідентифікації дійсних чисел у тексті, з урахуванням, 
що числа чітко відокремлені пробілами.
Застосуйте конструкцію yield у функції generator_numbers для створення генератора.
Переконайтеся, що sum_profit коректно обробляє дані від generator_numbers і підсумовує всі числа.

Критерії оцінювання:

Правильність визначення та повернення дійсних чисел функцією generator_numbers.
Коректність обчислення загальної суми в sum_profit.
Чистота коду, наявність коментарів та відповідність стилю кодування PEP8.

"""

# імпортуємо бібліотеку typing
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
