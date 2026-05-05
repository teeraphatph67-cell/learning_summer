import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle("Calculator")
    grid = QGridLayout()

    button_data = [
            ["Cls", 0, 0], ["Bck", 0, 1], ["Close", 0, 3,app.quit],
            ["7", 1, 0], ["8", 1, 1], ["9", 1, 2], ["/", 1, 3],
            ["4", 2, 0], ["5", 2, 1], ["6", 2, 2], ["*", 2, 3],
            ["1", 3, 0], ["2", 3, 1], ["3", 3, 2], ["-", 3, 3],
            ["0", 4, 0], [".", 4, 1], ["=", 4, 2], ["+", 4, 3]
        ]

    for data in button_data:
        text = data[0]  
        row = data[1]    
        col = data[2]    
        
        button = QPushButton(text)        
        grid.addWidget(button, row, col)

        if len(data) > 3:
            func = data[3]
            button.clicked.connect(func)

    win.setLayout(grid) 
    win.show()         
    sys.exit(app.exec())

if __name__ == '__main__':
    window()