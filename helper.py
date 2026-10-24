# Вспомогательные функции для приложения

def greet_user(name):
    print(f"Привет, {name}! Добро пожаловать в приложение.")

def get_date():
    from datetime import datetime
    return datetime.now().strftime("%d.%m.%Y %H:%M")