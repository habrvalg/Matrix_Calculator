import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget


class MatrixCalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Матричный калькулятор")
        self.setGeometry(100, 100, 400, 400)

        self.init_ui()

    def init_ui(self):
        self.operation_label = QLabel("Выберите операцию:")
        self.operation_menu = QLineEdit()
        self.operation_menu.setPlaceholderText("Сложение / Вычитание / Умножение на число / Умножение")

        self.matrix1_label = QLabel("Введите матрицу 1:")
        self.matrix1_entry = QTextEdit()

        self.matrix2_label = QLabel("Введите матрицу 2:")
        self.matrix2_entry = QTextEdit()

        self.calculate_button = QPushButton("Вычислить")
        self.calculate_button.clicked.connect(self.calculate)

        self.result_label = QLabel("Результат:")
        self.result_display = QTextEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.operation_label)
        layout.addWidget(self.operation_menu)
        layout.addWidget(self.matrix1_label)
        layout.addWidget(self.matrix1_entry)
        layout.addWidget(self.matrix2_label)
        layout.addWidget(self.matrix2_entry)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_display)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def calculate(self):
        operation = self.operation_menu.text()
        matrix1 = np.array(
            [[float(entry) for entry in row.split()] for row in self.matrix1_entry.toPlainText().split("\n")])
        matrix2 = np.array(
            [[float(entry) for entry in row.split()] for row in self.matrix2_entry.toPlainText().split("\n")])

        if operation == "Сложение":
            result = np.add(matrix1, matrix2)
        elif operation == "Вычитание":
            result = np.subtract(matrix1, matrix2)
        elif operation == "Умножение на число":
            scalar = float(input("Введите число для умножения: "))
            result = np.multiply(scalar, matrix1)
        elif operation == "Умножение":
            result = np.dot(matrix1, matrix2)

        self.result_display.setText("Результат:\n" + str(result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MatrixCalculatorApp()
    window.show()
    sys.exit(app.exec_())
