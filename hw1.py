from Models.fraction import Fraction

def get_fraction(prompt):
    while True:
        try:
            numerator, denominator = map(int, input(prompt).split())
            return Fraction(numerator, denominator)
        except Exception as e:
            print(f"Помилка вводу: {e}. Спробуйте ще раз.")


while True:
    try:
        print("\nОберіть операцію:")
        print("1. Додавання двох дробів")
        print("2. Віднімання двох дробів")
        print("3. Множення двох дробів")
        print("4. Ділення двох дробів")
        print("5. Показати кількість створених дробів")
        operation = input("Введіть номер операції: ")

        if operation in {'1', '2', '3', '4'}:
            fraction1 = get_fraction("Введіть чисельник та знаменник першого дробу через пробіл: ")
            fraction2 = get_fraction("Введіть чисельник та знаменник другого дробу через пробіл: ")

        if operation == '1':
            result = fraction1 + fraction2
            print("Результат додавання: ", result)
        elif operation == '2':
            result = fraction1 - fraction2
            print("Результат віднімання: ", result)
        elif operation == '3':
            result = fraction1 * fraction2
            print("Результат множення: ", result)
        elif operation == '4':
            result = fraction1 / fraction2
            print("Результат ділення: ", result)
        elif operation == '5':
            print(f"Кількість створених дробів: {Fraction.get_instance_count()}")
        else:
            print("Невідома операція.")
            continue

    except Exception as e:
        print(f"Сталася помилка: {e}")
        continue

    user_choice = input("\nНатисніть Enter, щоб продовжити, або будь-яку іншу клавішу, щоб вийти: ")
    if user_choice:
        break
