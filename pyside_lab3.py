import sys
from PySide6.QtWidgets import *
class myApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(320, 240) # กาํหนดขนาดของหนา้ต่างโปรแกรม
        self.setWindowTitle("Hello, World!") # กาํหนดชืÉอตรงหัวโปรแกรม
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())