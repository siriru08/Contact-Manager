import json

def load_contacts():
    try:
        with open("contacts.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Файл contacts.json повреждён.")
        return []

def save_contacts(contacts):
    with open("contacts.json", "w", encoding="utf-8") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=4)