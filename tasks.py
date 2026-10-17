class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks.pop(index - 1)
        else:
            print("Неверный номер задачи")
    
    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст")
        else:
            print("\nВаши задачи:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
            print()