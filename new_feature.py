# Новая функция: калькулятор
def calculator():
    print("=== Калькулятор ===")
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))
    operation = input("Операция (+, -, *, /): ")
    
    if operation == "+":
        print(f"Результат: {a + b}")
    elif operation == "-":
        print(f"Результат: {a - b}")
    elif operation == "*":
        print(f"Результат: {a * b}")
    elif operation == "/":
        if b != 0:
            print(f"Результат: {a / b}")
        else:
            print("Ошибка: деление на ноль!")
    else:
        print("Неизвестная операция")

if __name__ == "__main__":
    calculator()