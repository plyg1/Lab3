import numpy as np


# Завдання 1: Функція для правого циклічного зсуву
def shift_right3(A, B, C):
    A, B, C = C, A, B
    return A, B, C
def task_1():
    # Введення чисел
    A1 = float(input("Введіть A1: "))
    B1 = float(input("Введіть B1: "))
    C1 = float(input("Введіть C1: "))
    A2 = float(input("Введіть A2: "))
    B2 = float(input("Введіть B2: "))
    C2 = float(input("Введіть C2: "))

    print("\nЗавдання 1: Правий циклічний зсув")

    # Виконання правого циклічного зсуву для двох наборів
    A1, B1, C1 = shift_right3(A1, B1, C1)
    A2, B2, C2 = shift_right3(A2, B2, C2)

    # Виведення результатів
    print(f"Після зсуву для першого набору: A1 = {A1}, B1 = {B1}, C1 = {C1}")
    print(f"Після зсуву для другого набору: A2 = {A2}, B2 = {B2}, C2 = {C2}")


# Завдання 2: Функція для обробки матриці
def process_matrix():
    def matrix_operations(file_name):
        # Читання матриці з файлу
        matrix = np.loadtxt(file_name, delimiter=',')

        # Знаходження мінімальних і максимальних елементів у кожному рядку
        min_in_rows = np.min(matrix, axis=1)
        max_in_rows = np.max(matrix, axis=1)

        # Знаходження індексів рядків з максимальним і мінімальним елементом
        row_with_max_max = np.argmax(max_in_rows)
        row_with_min_min = np.argmin(min_in_rows)

        # Виведення індексів та значень
        print(
            f"Рядок з максимальним елементом: {row_with_max_max}, максимальний елемент: {max_in_rows[row_with_max_max]}")
        print(
            f"Рядок з мінімальним елементом: {row_with_min_min}, мінімальний елемент: {min_in_rows[row_with_min_min]}")

        # Обмін рядків місцями
        matrix[[row_with_max_max, row_with_min_min]] = matrix[[row_with_min_min, row_with_max_max]]

        return matrix

    # Введення імені файлу
    file_name = input("Введіть ім'я файлу з матрицею: ")

    # Виклик внутрішньої функції для обробки матриці
    transformed_matrix = matrix_operations(file_name)

    # Виведення перетвореної матриці
    print("Перетворена матриця після обміну рядків:")
    print(transformed_matrix)


# Головне меню
def main_menu():
    while True:
        print("\nГоловне меню:")
        print("1. Завдання 1: Правий циклічний зсув")
        print("2. Завдання 2: Обробка матриці")
        print("3. Вихід")

        choice = input("Виберіть завдання (1, 2 або 3): ")

        if choice == '1':
            task_1()
        elif choice == '2':
            process_matrix()
        elif choice == '3':
            print("Вихід з програми...")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


# Виклик головного меню
main_menu()
