class InformationSystem:
    def __init__(self):
        self.data = {}

    def add_user(self, user_name):
        if user_name not in self.data:
            self.data[user_name] = []
        else:
            print(f"Користувач з іменем {user_name} вже існує.")

    def add_contact(self, user_name, contact):
        if user_name in self.data:
            if contact not in self.data[user_name]:
                self.data[user_name].append(contact)
            else:
                print(f"Контакт {contact} вже існує у списку користувача {user_name}.")
        else:
            print(f"Користувач з іменем {user_name} не знайдений.")

    def remove_user(self, user_name):
        if user_name in self.data:
            del self.data[user_name]
        else:
            print(f"Користувача з іменем {user_name} не існує.")

    def remove_contact(self, user_name, contact):
        if user_name in self.data:
            if contact in self.data[user_name]:
                self.data[user_name].remove(contact)
            else:
                print(f"Контакт {contact} не знайдений у списку користувача {user_name}.")
        else:
            print(f"Користувач з іменем {user_name} не знайдений.")

    def edit_user(self, old_user_name, new_user_name):
        if old_user_name in self.data:
            if new_user_name not in self.data:
                self.data[new_user_name] = self.data[old_user_name]
                del self.data[old_user_name]
            else:
                print(f"Користувач з іменем {new_user_name} вже існує.")
        else:
            print(f"Користувача з іменем {old_user_name} не існує.")

    def edit_contact(self, user_name, old_contact, new_contact):
        if user_name in self.data:
            if old_contact in self.data[user_name]:
                if new_contact not in self.data[user_name]:
                    index = self.data[user_name].index(old_contact)
                    self.data[user_name][index] = new_contact
                else:
                    print(f"Контакт {new_contact} вже існує у списку користувача {user_name}.")
            else:
                print(f"Контакт {old_contact} не знайдений у списку користувача {user_name}.")
        else:
            print(f"Користувач з іменем {user_name} не знайдений.")

    def print_all_users(self):
        if self.data:
            for user, contacts in self.data.items():
                print(f"Користувач: {user}, Контакти: {', '.join(contacts) if contacts else 'Немає контактів'}")
        else:
            print("Немає користувачів в системі.")

    def print_user_contacts(self, user_name):
        if user_name in self.data:
            contacts = self.data[user_name]
            print(f"Користувач: {user_name}, Контакти: {', '.join(contacts) if contacts else 'Немає контактів'}")
        else:
            print(f"Користувач з іменем {user_name} не знайдений.")
