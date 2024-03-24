from Models.unit_converter import UnitConverter
def get_length(prompt):
    while True:
        try:
            length = float(input(prompt))
            return length
        except ValueError as e:
            print(f"Помилка вводу: {e}. Будь ласка, введіть число.")


while True:
    try:
        print("\nОберіть операцію:")
        print("1. Конвертувати метри у фути")
        print("2. Конвертувати фути у метри")
        print("3. Вийти з програми")
        operation = input("Введіть номер операції: ")

        if operation == '1':
            length = get_length("Введіть довжину в метрах: ")
            result = UnitConverter.meters_to_feet(length)
            print(f"Результат конвертації: {result} футів")
        elif operation == '2':
            length = get_length("Введіть довжину в футах: ")
            result = UnitConverter.feet_to_meters(length)
            print(f"Результат конвертації: {result} метрів")
        elif operation == '3':
            print("Вихід з програми...")
            break
        else:
            print("Невідома операція.")
            continue

    except Exception as e:
        print(f"Сталася помилка: {e}")
        continue

    user_choice = input("\nНатисніть Enter, щоб продовжити, або будь-яку іншу клавішу, щоб вийти: ")
    if user_choice:
        break
