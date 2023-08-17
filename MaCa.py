import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QGridLayout, \
    QWidget, QLineEdit, QMessageBox


class MatrixCalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Матричный калькулятор")
        self.setGeometry(100, 100, 400, 400)

        self.init_ui()

    def init_ui(self):
        self.matrix_size_label = QLabel("Выберите размер матрицы:")
        self.matrix_size_input = QLineEdit()
        self.create_matrix_button = QPushButton("Создать матрицы")
        self.create_matrix_button.clicked.connect(self.create_matrices)

        self.matrix1_label = QLabel("Матрица 1:")
        self.matrix1_layout = QGridLayout()

        self.matrix2_label = QLabel("Матрица 2:")
        self.matrix2_layout = QGridLayout()

        self.scalar_label = QLabel("Введите число для умножения:")
        self.scalar_input = QLineEdit()

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
        layout.addWidget(self.matrix_size_label)
        layout.addWidget(self.matrix_size_input)
        layout.addWidget(self.create_matrix_button)
        layout.addWidget(self.matrix1_label)
        layout.addLayout(self.matrix1_layout)
        layout.addWidget(self.matrix2_label)
        layout.addLayout(self.matrix2_layout)
        layout.addWidget(self.scalar_label)
        layout.addWidget(self.scalar_input)
        layout.addWidget(self.addition_button)
        layout.addWidget(self.subtraction_button)
        layout.addWidget(self.scalar_mult_button)
        layout.addWidget(self.matrix_mult_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_display)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.matrix1 = None
        self.matrix2 = None
        self.matrix_input_fields1 = []
        self.matrix_input_fields2 = []

    def create_matrices(self):
        try:
            matrix_size = int(self.matrix_size_input.text())
            self.create_matrix_layout(self.matrix1_layout, matrix_size, self.matrix_input_fields1)
            self.create_matrix_layout(self.matrix2_layout, matrix_size, self.matrix_input_fields2)
        except ValueError:
            self.show_error("Введите корректный размер матрицы")

    def create_matrix_layout(self, layout, size, input_fields_list):
        for row in range(size):
            input_fields_row = []
            for col in range(size):
                entry = QLineEdit()
                layout.addWidget(entry, row, col)
                input_fields_row.append(entry)
            input_fields_list.append(input_fields_row)

    def get_matrices(self, input_fields_list):
        matrix = []
        for row_inputs in input_fields_list:
            row_entries = []
            for entry in row_inputs:
                if entry.text():
                    row_entries.append(float(entry.text()))
                else:
                    row_entries.append(0)
            matrix.append(row_entries)
        return np.array(matrix)

    def calculate_addition(self):
        matrix1 = self.get_matrices(self.matrix_input_fields1)
        matrix2 = self.get_matrices(self.matrix_input_fields2)
        if matrix1 is not None and matrix2 is not None:
            result = np.add(matrix1, matrix2)
            self.result_display.setText("Результат:\n" + str(result))

    def calculate_subtraction(self):
        matrix1 = self.get_matrices(self.matrix_input_fields1)
        matrix2 = self.get_matrices(self.matrix_input_fields2)
        if matrix1 is not None and matrix2 is not None:
            result = np.subtract(matrix1, matrix2)
            self.result_display.setText("Результат:\n" + str(result))

    def calculate_scalar_mult(self):
        matrix1 = self.get_matrices(self.matrix_input_fields1)
        scalar = float(self.scalar_input.text())
        if matrix1 is not None:
            result = np.multiply(scalar, matrix1)
            self.result_display.setText("Результат:\n" + str(result))

    def calculate_matrix_mult(self):
        matrix1 = self.get_matrices(self.matrix_input_fields1)
        matrix2 = self.get_matrices(self.matrix_input_fields2)
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
