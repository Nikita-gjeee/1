def display_menu():
    print("\n=== Менеджер задач ===")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Удалить задачу")
    print("4. Выход")
    print("=====================")

def get_user_input(prompt):
    return input(prompt).strip()
# Новая функция, добавленная в 1
def show_version():
    print("Версия приложения: 1.0")