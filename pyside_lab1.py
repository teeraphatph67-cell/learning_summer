import sys
from PySide6.QtWidgets import *

app = QApplication(sys.argv)

label = QLabel("Hello World")
label.show()

app.exec()
sys.exit()
