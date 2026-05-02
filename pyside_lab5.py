import sys
from PySide6.QtWidgets import *
class myApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(320, 240) # กาํหนดขนาดของหนา้ต่างโปรแกรม
        self.setWindowTitle("Hello, World!") # กาํหนดชืÉอตรงหัวโปรแกรม
        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Hello World")

        label2 = QLabel("สวสัดี")
        label3 = QLabel("เพิÉงเริÉมตน้ เรียน PySide -..- จากผเู้ขียนบทความ")
        layout.addWidget(label)
        layout.addWidget(label2)
        layout.addWidget(label3)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())