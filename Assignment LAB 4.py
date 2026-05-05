import sys
from PySide6.QtWidgets import (QApplication, QWidget, QGridLayout, 
                             QLineEdit, QPushButton, QVBoxLayout)
from PySide6.QtCore import Qt

class CalculatorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        
        main_layout = QVBoxLayout()
        
        self.display = QLineEdit('0')
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(35)
        main_layout.addWidget(self.display)

        grid_layout = QGridLayout()

        buttons = [
            ('Backspace', 0, 0, 1, 2), ('Clear', 0, 2, 1, 2), ('Clear All', 0, 4, 1, 2),
            
            ('MC', 1, 0), ('7', 1, 1), ('8', 1, 2), ('9', 1, 3), ('/', 1, 4), ('Sqrt', 1, 5),
            ('MR', 2, 0), ('4', 2, 1), ('5', 2, 2), ('6', 2, 3), ('*', 2, 4), ('x²', 2, 5),
            ('MS', 3, 0), ('1', 3, 1), ('2', 3, 2), ('3', 3, 3), ('-', 3, 4), ('1/x', 3, 5),
            ('M+', 4, 0), ('0', 4, 1), ('.', 4, 2), ('±', 4, 3), ('+', 4, 4), ('=', 4, 5),
        ]

        for btn_info in buttons:
            text = btn_info[0]
            row = btn_info[1]
            col = btn_info[2]
            
            button = QPushButton(text)
            button.setFixedSize(60, 40)
            
            if len(btn_info) > 3:
                row_span = btn_info[3]
                col_span = btn_info[4]
                grid_layout.addWidget(button, row, col, row_span, col_span)
                button.setFixedWidth(125) 
            else:
                grid_layout.addWidget(button, row, col)

        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = CalculatorUI()
    calc.show()
    sys.exit(app.exec())