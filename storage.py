import json
import os

# Путь считается от папки проекта, поэтому не зависит от того, откуда запущена программа
DATABASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database")
FILE_PATH = os.path.join(DATABASE_DIR, "db_contacts.json")


def normalize(contact):
    """Приводит старые записи к единому формату: телефон - строка, избранное - True/False."""
    contact["phone"] = str(contact.get("phone", ""))
    favorite = contact.get("favorite", False)
    if isinstance(favorite, str):
        favorite = favorite.strip().lower() in ("да", "✅", "yes", "true")
    contact["favorite"] = bool(favorite)
    return contact


def load_contacts():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return [normalize(contact) for contact in json.load(file)]

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Файл db_contacts.json повреждён.")
        return []


def save_contacts(contacts):
    os.makedirs(DATABASE_DIR, exist_ok=True)  # создаст папку, если её нет
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=4)
