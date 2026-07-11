# Главное меню
import contacts
import storage

# Загрузка данных
contacts_base = storage.load_contacts()

while True:
    print("""
========================
    Contact Manager
========================

1. Добавить контакт
2. Показать контакты
3. Найти контакт
4. Удалить 
5. Избранные
6. Редактирование
7. Сортировка
0. Выход
========================
""")


    num = input("""
Выберите действие: """)


    if num == "1":
        contacts.new_contacts(contacts_base)

    elif num == "2":
        contacts.list_contacts(contacts_base)

    elif num == "3":
        contacts.search(contacts_base)

    elif num == "4":
        contacts.delete_contacts(contacts_base)

    elif num == "5":
        contacts.favorite_contacts(contacts_base)

    elif num == "6":
        contacts.edit_contacts(contacts_base)

    elif num == "7":
        contacts.sorted_contacts(contacts_base)

    elif num == "0":
        print("Программа завершена")
        break

    else:
        print("Неизвестная команда")