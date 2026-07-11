#Здесь находится вся логика.
import storage

# Увеличение контактов
def get_next_id(contacts):
    if not contacts:
        return 1
    return max(contact["id"] for contact in contacts) + 1

# Добавление контакта
def new_contacts(contacts):

    id_number = get_next_id(contacts)

    name = input("Введите имя контакта: ")
    number = int(input("Введите номер контакта: "))
    email = input("Введите почту контакта: ")
    address = input("Введите адрес контакта: ")
    favorite = input("Добавить этот контакт в избранные (да/нет): ")

    new_people = {
        "id": id_number,
        "name": name,
        "phone": number,
        "email": email,
        "address": address,
        "favorite": favorite
    }
    contacts.append(new_people)
    storage.save_contacts(contacts)

    return "Контакт успешно добавлен"

# Показ контактов
def list_contacts(contacts):
    if not contacts:
        print("""
========================
    Список пустой
========================""")
        return

    for contact in contacts:
        print(f"""
-----------------------------
ID: {contact["id"]}
Имя: {contact["name"]}
Телефон: +{contact["phone"]}
Email: {contact["email"]}
Адрес: {contact["address"]}
Избранный: {contact["favorite"]}
""")

    while True:
        command = input("0. Вернуться в главное меню: ")
        if command == "0":
            break
        print("Неизвестная команда")

# Поиск контактов
def search(contacts):
    while True:
        print("""Поиск:
========================
    1. Имя
    2. Телефон
    3. Email
    0. Назад
========================""")
        try:
            search_contacts = int(input("Введите действие: "))
        except ValueError:
            print("Введите число!")
            return

# Поиск по имени
        if search_contacts == 1:
            name_search = input("Введите имя: ")
            count_name = 0     #Счётчик найденных контактов
            for contact in contacts:
                if contact["name"] == name_search:
                    count_name += 1
                    print(f"""
ID: {contact["id"]}
Имя: {contact["name"]}
Телефон: {contact["phone"]}
Email: {contact["email"]}
Адрес: {contact["address"]}
Избранный: {contact["favorite"]}
-----------------------------""")

            if count_name == 0:
                print("Контакты не найдены!")
            else:
                print(f"Найдено контактов: {count_name}")

# Поиск по номеру
        elif search_contacts == 2:
            number_search = input("Введите номер: ")
            count_number = 0     #Счётчик найденных контактов
            for contact in contacts:
                if contact["phone"] == number_search:
                    count_number += 1
                    print(f"""
ID: {contact["id"]}
Имя: {contact["name"]}
Телефон: +{contact["phone"]}
Email: {contact["email"]}
Адрес: {contact["address"]}
Избранный: {contact["favorite"]}
-----------------------------""")

            if count_number == 0:
                print("Контакты не найдены!")
            else:
                print(f"Найдено контактов: {count_number}")

# Поиск по email
        elif search_contacts == 3:
            email_search = input("Введите email: ").lower()
            count_email = 0     #Счётчик найденных контактов
            for contact in contacts:
                if contact["email"] == email_search:
                    count_email += 1
                    print(f"""
ID: {contact["id"]}
Имя: {contact["name"]}
Телефон: +{contact["phone"]}
Email: {contact["email"]}
Адрес: {contact["address"]}
Избранный: {contact["favorite"]}
-----------------------------""")

            if count_email == 0:    # Проверка на наличие контактов
                print("Контакты не найдены!")
            else:
                print(f"Найдено контактов: {count_email}")

        elif search_contacts == 0:
            break


    
def delete_contacts(contacts):
    try:
        delete_id = int(input("Введите ID: "))
    except ValueError:
        print("ID должен быть числом!")
        return
    found = False

    for contact in contacts:
        if contact["id"] == delete_id:
            contacts.remove(contact)
            found = True
            break

    if found:
        print("Контакт удалён")
    else:
        print("Контакт не найден")

    while True:
        try:
            command = input("0. Вернуться в главное меню: ")
        except ValueError:
            print("Введите число 0")
            return
        if command == "0":
            break

        print("Неизвестная команда")

def favorite_contacts(contacts):
    if not contacts:
        print("Избранных контактов нету")
    else:
        for contact in contacts:
            if contact["favorite"]:
                print(f"""
----------------------------- 
ID: {contact["id"]}
Имя: {contact["name"]}
Телефон: +{contact["phone"]}
Email: {contact["email"]}
Адрес: {contact["address"]}
Избранный: {contact["favorite"]}
-----------------------------
                    """)
    while True:
        try:
            command = input("0. Вернуться в главное меню: ")
        except ValueError:
            print("Введите число 0")
            return
        if command == "0":
            break

        print("Неизвестная команда")

def edit_contacts(contacts):
    found = False

    try:
        contact_id = int(input("Введите номер ID: "))
    except ValueError:
        print("ID должен быть числом!")


    for contact in contacts:
        if contact["id"] == contact_id:
            found = True

            print(f"""
----------------------------- 
Имя: {contact["name"]}
Телефон: {contact["phone"]}
Email: {contact["email"]}
Адрес: {contact["address"]}
Избранный: {contact["favorite"]}
-----------------------------
""")
            edit_word = input("""
========================
    Что изменить?
======================== 
1. Имя
2. Телефон
3. Email
4. Адрес
5. Избранное
0. Назад
========================
Выберите действие: """)

            if edit_word == "1":
                new_name = input("Введите новое имя: ")
                contact["name"] = new_name
                print("Контакт изменен!")
                storage.save_contacts(contacts)
            elif edit_word == "2":
                new_phone = input("Введите новый телефон: ")
                contact["phone"] = new_phone
                print("Контакт изменен!")
                storage.save_contacts(contacts)
            elif edit_word == "3":
                new_email = input("Введите новый email: ")
                contact["email"] = new_email
                print("Контакт изменен!")
                storage.save_contacts(contacts)
            elif edit_word == "4":
                new_address = input("Введите новый адрес: ")
                contact["address"] = new_address
                print("Контакт изменен!")
                storage.save_contacts(contacts)
            elif edit_word == "5":
                favorite = input("Добавить в избранное? (да/нет): ").lower()
                if favorite == "да":
                    contact["favorite"] = "✅"
                    storage.save_contacts(contacts)
                elif favorite == "нет":
                    contact["favorite"] = "❌"
                    storage.save_contacts(contacts)
                else:
                    print("Неизвестная команда")
            elif edit_word == "0":
                return
            else:
                print("Такой команды нет")
            break

    if found == False:
        print("Контакт с таким ID не найден")

    while True:
        command = input("0. Вернуться в главное меню: ")
        if command == "0":
            break
        print("Неизвестная команда")

def show_contact(contact):
    print(f"""
-----------------------------
ID: {contact["id"]}
Имя: {contact["name"]}
Телефон: {contact["phone"]}
Email: {contact["email"]}
Адрес: {contact["address"]}
Избранный: {contact["favorite"]}
-----------------------------
""")
    
    
# Сортировка по имени
def sorted_contacts(contacts):
    print("""
===================
Сортировка
===================

1. По имени
2. По ID
3. По избранным
0. Назад""")


    word_sort = input("Введите действие: ")

    if word_sort == "1":
        result = sorted(contacts, key=lambda contact: contact["name"])
        for contact in result:
            show_contact(contact)

    elif word_sort == "2":
        result = sorted(contacts, key=lambda contact: contact["id"])
        for contact in result:
            show_contact(contact)

    elif word_sort == "3":
        result_favorite = sorted(contacts, key=lambda contact: contact["favorite"], reverse=True)
        for contact in result_favorite:
            show_contact(contact)

    elif word_sort == "0":
        return

    else:
        print("Неизвестная команда")

    while True:
        command = input("0. Вернуться в главное меню: ")
        if command == "0":
            break
        print("Неизвестная команда")