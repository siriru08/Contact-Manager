# Проверка пользовательского ввода

def ask_phone(prompt):
    """Спрашивает телефон, пока не будет введено от 10 до 15 цифр. Возвращает строку."""
    while True:
        phone = input(prompt).strip().lstrip("+")
        if phone.isdigit() and 10 <= len(phone) <= 15:
            return phone
        print("Телефон должен содержать от 10 до 15 цифр.")


def ask_yes_no(prompt):
    """Спрашивает «да/нет», пока ответ не будет понятен. Возвращает True или False."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("да", "д", "yes", "y"):
            return True
        if answer in ("нет", "н", "no", "n"):
            return False
        print("Ответьте «да» или «нет».")
