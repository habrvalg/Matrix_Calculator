import numpy as np
import tkinter as tk
from tkinter import ttk


class MatrixCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Матричный калькулятор")

        self.create_widgets()

    def create_widgets(self):
        self.operation_var = tk.StringVar()
        self.operation_var.set("Сложение")

        operation_label = tk.Label(self.root, text="Выберите операцию:")
        operation_label.pack(pady=10)

        operation_menu = ttk.Combobox(self.root, textvariable=self.operation_var,
                                      values=["Сложение", "Вычитание", "Умножение на число", "Умножение"])
        operation_menu.pack()

        matrix1_label = tk.Label(self.root, text="Введите матрицу 1:")
        matrix1_label.pack(pady=10)

        self.matrix1_entry = tk.Text(self.root, height=5, width=20)
        self.matrix1_entry.pack()

        matrix2_label = tk.Label(self.root, text="Введите матрицу 2:")
        matrix2_label.pack(pady=10)

        self.matrix2_entry = tk.Text(self.root, height=5, width=20)
        self.matrix2_entry.pack()

        calculate_button = tk.Button(self.root, text="Вычислить", command=self.calculate)
        calculate_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="Результат:")
        self.result_label.pack()

    def calculate(self):
        operation = self.operation_var.get()
        matrix1 = np.array([[float(entry) for entry in row.split()] for row in
                            self.matrix1_entry.get("1.0", "end").strip().split("\n")])
        matrix2 = np.array([[float(entry) for entry in row.split()] for row in
                            self.matrix2_entry.get("1.0", "end").strip().split("\n")])

        if operation == "Сложение":
            result = np.add(matrix1, matrix2)
        elif operation == "Вычитание":
            result = np.subtract(matrix1, matrix2)
        elif operation == "Умножение на число":
            scalar = float(input("Введите число для умножения: "))
            result = np.multiply(scalar, matrix1)
        elif operation == "Умножение":
            result = np.dot(matrix1, matrix2)

        self.result_label.config(text="Результат:\n" + str(result))


if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixCalculatorApp(root)
    root.mainloop()
