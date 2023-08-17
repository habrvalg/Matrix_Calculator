import numpy as np


def main():
    print("Матричный калькулятор")
    print("1. Сложение матриц")
    print("2. Вычитание матриц")
    print("3. Умножение матрицы на число")
    print("4. Умножение матриц")
    choice = int(input("Выберите операцию (1/2/3/4): "))

    if choice in [1, 2, 3, 4]:
        matrix1 = input_matrix("Введите первую матрицу:")
        if choice != 3:
            matrix2 = input_matrix("Введите вторую матрицу:")

        if choice == 1:
            result = matrix1 + matrix2
        elif choice == 2:
            result = matrix1 - matrix2
        elif choice == 3:
            scalar = float(input("Введите число для умножения: "))
            result = scalar * matrix1
        elif choice == 4:
            result = np.dot(matrix1, matrix2)

        print("Результат:")
        print(result)
    else:
        print("Некорректный выбор операции.")


def input_matrix(prompt):
    rows = int(input(prompt + " Количество строк: "))
    cols = int(input(prompt + " Количество столбцов: "))
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Элемент [{i}, {j}]: "))
            row.append(element)
        matrix.append(row)
    return np.array(matrix)


if __name__ == "__main__":
    main()
