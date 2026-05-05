import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                               QHBoxLayout, QPushButton, QLabel)
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buttons")
        self.resize(480, 240)

        main_layout = QVBoxLayout()

        self.display_label = QLabel("") 
        main_layout.addWidget(self.display_label, alignment=Qt.AlignCenter)

        button_layout = QHBoxLayout()
        
        button_layout.addStretch() 
        
        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.show_message)
        
        btn_close = QPushButton("Close")
        btn_close.clicked.connect(self.close)
        
        button_layout.addWidget(btn_ok)
        button_layout.addWidget(btn_close)

        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def show_message(self):
        self.display_label.setText("Hello World")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
