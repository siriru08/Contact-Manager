# Здесь находится вся логика работы с контактами.
import storage
import validators


# Новый ID = максимальный существующий + 1
def get_next_id(contacts):
    if not contacts:
        return 1
    return max(contact["id"] for contact in contacts) + 1


# Показ одного контакта (используется везде, чтобы вывод был одинаковым)
def show_contact(contact):
    favorite = "✅" if contact["favorite"] else "❌"
    print(f"""
-----------------------------
ID: {contact["id"]}
Имя: {contact["name"]}
Телефон: +{contact["phone"]}
Email: {contact["email"]}
Адрес: {contact["address"]}
Избранный: {favorite}
-----------------------------""")


# Ожидание команды возврата в главное меню
def wait_for_back():
    while True:
        command = input("0. Вернуться в главное меню: ")
        if command == "0":
            break
        print("Неизвестная команда")


# Добавление контакта
def new_contacts(contacts):
    id_number = get_next_id(contacts)

    name = input("Введите имя контакта: ").strip()
    phone = validators.ask_phone("Введите номер контакта: ")
    email = input("Введите почту контакта: ").strip().lower()
    address = input("Введите адрес контакта: ").strip()
    favorite = validators.ask_yes_no("Добавить этот контакт в избранные (да/нет): ")

    new_people = {
        "id": id_number,
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "favorite": favorite
    }
    contacts.append(new_people)
    storage.save_contacts(contacts)

    print("Контакт успешно добавлен")


# Показ контактов
def list_contacts(contacts):
    if not contacts:
        print("""
========================
    Список пустой
========================""")
        return

    for contact in contacts:
        show_contact(contact)

    wait_for_back()


# Вывод результатов поиска
def print_search_result(found):
    for contact in found:
        show_contact(contact)

    if found:
        print(f"Найдено контактов: {len(found)}")
    else:
        print("Контакты не найдены!")


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
            continue

        if search_contacts == 1:
            query = input("Введите имя: ").strip().lower()
            found = [c for c in contacts if c["name"].lower() == query]
        elif search_contacts == 2:
            query = input("Введите номер: ").strip().lstrip("+")
            found = [c for c in contacts if c["phone"] == query]
        elif search_contacts == 3:
            query = input("Введите email: ").strip().lower()
            found = [c for c in contacts if c["email"].lower() == query]
        elif search_contacts == 0:
            break
        else:
            print("Неизвестная команда")
            continue

        print_search_result(found)


# Удаление контакта
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
            storage.save_contacts(contacts)  # раньше удаление не сохранялось
            found = True
            break

    if found:
        print("Контакт удалён")
    else:
        print("Контакт не найден")

    wait_for_back()


# Избранные контакты
def favorite_contacts(contacts):
    favorites = [contact for contact in contacts if contact["favorite"]]

    if not favorites:
        print("Избранных контактов нет")

    for contact in favorites:
        show_contact(contact)

    wait_for_back()


# Редактирование контакта
def edit_contacts(contacts):
    try:
        contact_id = int(input("Введите номер ID: "))
    except ValueError:
        print("ID должен быть числом!")
        return

    contact = next((c for c in contacts if c["id"] == contact_id), None)

    if contact is None:
        print("Контакт с таким ID не найден")
        wait_for_back()
        return

    show_contact(contact)
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
        contact["name"] = input("Введите новое имя: ").strip()
    elif edit_word == "2":
        contact["phone"] = validators.ask_phone("Введите новый телефон: ")
    elif edit_word == "3":
        contact["email"] = input("Введите новый email: ").strip().lower()
    elif edit_word == "4":
        contact["address"] = input("Введите новый адрес: ").strip()
    elif edit_word == "5":
        contact["favorite"] = validators.ask_yes_no("Добавить в избранное? (да/нет): ")
    elif edit_word == "0":
        return
    else:
        print("Такой команды нет")
        wait_for_back()
        return

    storage.save_contacts(contacts)
    print("Контакт изменен!")
    wait_for_back()


# Сортировка контактов
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
        result = sorted(contacts, key=lambda contact: contact["name"].lower())
    elif word_sort == "2":
        result = sorted(contacts, key=lambda contact: contact["id"])
    elif word_sort == "3":
        result = sorted(contacts, key=lambda contact: contact["favorite"], reverse=True)
    elif word_sort == "0":
        return
    else:
        print("Неизвестная команда")
        wait_for_back()
        return

    for contact in result:
        show_contact(contact)

    wait_for_back()
