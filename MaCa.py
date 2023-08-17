import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QMessageBox, QWidget


class MatrixCalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Матричный калькулятор")
        self.setGeometry(100, 100, 400, 400)

        self.init_ui()

    def init_ui(self):
        self.matrix1_label = QLabel("Введите матрицу 1 (разделяйте числа пробелами, строки - переносами):")
        self.matrix1_entry = QTextEdit()

        self.matrix2_label = QLabel("Введите матрицу 2 (разделяйте числа пробелами, строки - переносами):")
        self.matrix2_entry = QTextEdit()

        self.result_label = QLabel("Результат:")
        self.result_display = QTextEdit()

        self.addition_button = QPushButton("Сложение")
        self.addition_button.clicked.connect(self.calculate_addition)

        self.subtraction_button = QPushButton("Вычитание")
        self.subtraction_button.clicked.connect(self.calculate_subtraction)

        self.scalar_mult_button = QPushButton("Умножение на число")
        self.scalar_mult_button.clicked.connect(self.calculate_scalar_mult)

        self.matrix_mult_button = QPushButton("Умножение")
        self.matrix_mult_button.clicked.connect(self.calculate_matrix_mult)

        layout = QVBoxLayout()
        layout.addWidget(self.matrix1_label)
        layout.addWidget(self.matrix1_entry)
        layout.addWidget(self.matrix2_label)
        layout.addWidget(self.matrix2_entry)
        layout.addWidget(self.addition_button)
        layout.addWidget(self.subtraction_button)
        layout.addWidget(self.scalar_mult_button)
        layout.addWidget(self.matrix_mult_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_display)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_matrices(self):
        matrix1_text = self.matrix1_entry.toPlainText()
        matrix2_text = self.matrix2_entry.toPlainText()

        if not matrix1_text or not matrix2_text:
            self.show_error("Введите матрицу")
            return None, None

        matrix1 = np.array([[float(entry) for entry in row.split()] for row in matrix1_text.split("\n")])
        matrix2 = np.array([[float(entry) for entry in row.split()] for row in matrix2_text.split("\n")])
        return matrix1, matrix2

    def calculate_addition(self):
        matrix1, matrix2 = self.get_matrices()
        if matrix1 is not None and matrix2 is not None:
            result = np.add(matrix1, matrix2)
            self.result_display.setText("Результат:\n" + str(result))

    def calculate_subtraction(self):
        matrix1, matrix2 = self.get_matrices()
        if matrix1 is not None and matrix2 is not None:
            result = np.subtract(matrix1, matrix2)
            self.result_display.setText("Результат:\n" + str(result))

    def calculate_scalar_mult(self):
        matrix1, _ = self.get_matrices()
        if matrix1 is not None:
            scalar = float(input("Введите число для умножения: "))
            result = np.multiply(scalar, matrix1)
            self.result_display.setText("Результат:\n" + str(result))

    def calculate_matrix_mult(self):
        matrix1, matrix2 = self.get_matrices()
        if matrix1 is not None and matrix2 is not None:
            result = np.dot(matrix1, matrix2)
            self.result_display.setText("Результат:\n" + str(result))

    def show_error(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("Ошибка")
        msg_box.setText(message)
        msg_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MatrixCalculatorApp()
    window.show()
    sys.exit(app.exec_())
