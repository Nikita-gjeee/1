from tasks import TaskManager
from utils import display_menu

def main():
    manager = TaskManager()
    
    while True:
        display_menu()
        choice = input("Выберите действие: ")
        
        if choice == "1":
            task = input("Введите задачу: ")
            manager.add_task(task)
            print("Задача добавлена!")
        elif choice == "2":
            manager.show_tasks()
        elif choice == "3":
            task_num = int(input("Номер задачи для удаления: "))
            manager.remove_task(task_num)
            print("Задача удалена!")
        elif choice == "4":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()