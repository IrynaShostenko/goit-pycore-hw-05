"""створюємо функцію caching_fibonacci, яка створює та використовує кеш 
для зберігання і повторного використання вже обчислених значень чисел Фібоначчі."""

def caching_fibonacci():
    # Створюємо кеш для збереження обчислених значень
    cache = {}

    # створюємо внутрішню функцію для обчислення числа Фібоначчі
    def fibonacci(n):
        # Якщо n менше або дорівнює 0, повертаємо 0
        if n <= 0:
            return 0
        # Якщо n дорівнює 1, повертаємо 1
        elif n == 1:
            return 1
        # Якщо значення для n вже є у кеші, повертаємо його
        if n in cache:
            return cache[n]

        # Якщо значення немає в кеші, обчислюємо його рекурсивно
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повертаємо внутрішню функцію fibonacci
    return fibonacci


# Приклад використання:
fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610