from Models.temperature_converter import TemperatureConverter

def get_temperature(prompt):
    while True:
        try:
            temperature = float(input(prompt))
            return temperature
        except ValueError as e:
            print(f"Помилка вводу: {e}. Будь ласка, введіть число.")

while True:
    try:
        print("\nОберіть операцію:")
        print("1. Конвертувати Цельсій у Фаренгейт")
        print("2. Конвертувати Фаренгейт у Цельсій")
        print("3. Показати кількість конвертацій")
        operation = input("Введіть номер операції: ")

        if operation == '1':
            temperature = get_temperature("Введіть температуру в Цельсіях: ")
            result = TemperatureConverter.celsius_to_fahrenheit(temperature)
            print(f"Результат конвертації: {result} Фаренгейт")
        elif operation == '2':
            temperature = get_temperature("Введіть температуру в Фаренгейтах: ")
            result = TemperatureConverter.fahrenheit_to_celsius(temperature)
            print(f"Результат конвертації: {result} Цельсій")
        elif operation == '3':
            print(f"Кількість конвертацій: {TemperatureConverter.get_conversion_count()}")
        else:
            print("Невідома операція.")
            continue

    except Exception as e:
        print(f"Сталася помилка: {e}")
        continue

    user_choice = input("\nНатисніть Enter, щоб продовжити, або будь-яку іншу клавішу, щоб вийти: ")
    if user_choice:
        break
