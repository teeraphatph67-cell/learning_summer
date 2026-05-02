import sys
from PySide6.QtWidgets import *
class myApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(320, 240) # กาํหนดขนาดของหนา้ต่างโปรแกรม
        self.setWindowTitle("Hello, World!") # กาํหนดชืÉอตรงหัวโปรแกรม
        layout = QVBoxLayout()
        self.setLayout(layout)
        hello = QPushButton("Hello world!") # กาํหนดขอ้ความในปุ่ม
        hello.resize(100, 30) # กาํหนดขนาดของปุ่ม
        layout.addWidget(hello)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())