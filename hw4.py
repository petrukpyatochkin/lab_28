from Models.information_system import InformationSystem

info_system = InformationSystem()

while True:
    try:
        print("\nОберіть операцію:")
        print("1. Додати нового користувача")
        print("2. Додати контакт до користувача")
        print("3. Видалити користувача")
        print("4. Видалити контакт користувача")
        print("5. Редагувати ім'я користувача")
        print("6. Редагувати контакт користувача")
        print("7. Вивести всіх користувачів та їхні контакти")
        print("8. Вивести контакти конкретного користувача")
        print("9. Вийти з програми")
        operation = input("Введіть номер операції: ")

        if operation == '1':
            user_name = input("Введіть ім'я нового користувача: ")
            info_system.add_user(user_name)
        elif operation == '2':
            user_name = input("Введіть ім'я користувача для додавання контакту: ")
            contact = input("Введіть ім'я контакту: ")
            info_system.add_contact(user_name, contact)
        elif operation == '3':
            user_name = input("Введіть ім'я користувача для видалення: ")
            info_system.remove_user(user_name)
        elif operation == '4':
            user_name = input("Введіть ім'я користувача для видалення контакту: ")
            contact = input("Введіть ім'я контакту для видалення: ")
            info_system.remove_contact(user_name, contact)
        elif operation == '5':
            old_user_name = input("Введіть старе ім'я користувача: ")
            new_user_name = input("Введіть нове ім'я користувача: ")
            info_system.edit_user(old_user_name, new_user_name)
        elif operation == '6':
            user_name = input("Введіть ім'я користувача для редагування контакту: ")
            old_contact = input("Введіть старе ім'я контакту: ")
            new_contact = input("Введіть нове ім'я контакту: ")
            info_system.edit_contact(user_name, old_contact, new_contact)
        elif operation == '7':
            info_system.print_all_users()
        elif operation == '8':
            user_name = input("Введіть ім'я користувача для виводу його контактів: ")
            info_system.print_user_contacts(user_name)
        elif operation == '9':
            print("Вихід з програми...")
            break
        else:
            print("Невідома операція.")

    except Exception as e:
        print(f"Сталася помилка: {e}")
        continue

    user_choice = input("\nНатисніть Enter, щоб продовжити, або будь-яку іншу клавішу, щоб вийти: ")
    if user_choice:
        break
