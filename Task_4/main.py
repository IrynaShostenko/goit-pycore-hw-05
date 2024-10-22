"""Пишемо консольного бота помічника, який розпізнаватиме команди, 
що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.
Дороблюємо консольного бота - додаємо обробку помилок за допомоги декораторів.
"""

# Додаємо декоратор для обробки помилок
def input_error(func):  
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError: 
            return "Контакт не знайдено. Введіть правильне ім'я."
        except ValueError: 
            return "Введіть ім'я та номер телефону, будь ласка."
        except IndexError:  
            return "Недостатньо аргументів для виконання команди."
    return inner

def parse_input(user_input):
    """
    Парсер команд. Повертає команду і список аргументів.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args
# додаємо декоратор для обробки помилок
@input_error
def add_contact(args, contacts):
    """
    Додає новий контакт до словника.
    """
    if len(args) < 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return f"Контакт {name} додано."

# додаємо декоратор для обробки помилок
@input_error
def change_contact(args, contacts):
    """
    Змінює існуючий контакт.
    """
    if len(args) < 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Контакт {name} оновлено."
    else:
        raise KeyError
    
# додаємо декоратор для обробки помилок
@input_error
def show_phone(args, contacts):
    """
    Показує номер телефону за ім'ям контакту.
    """
    if len(args) < 1:
        raise IndexError
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        raise KeyError

def show_all(contacts):
    """
    Виводить усі контакти.
    """
    if not contacts:
        return "Контакти відсутні."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Ласкаво просимо до бот-асистента!")

    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("До побачення!")
            break

        elif command == "hello":
            print("Як я можу допомогти?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Невірна команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
