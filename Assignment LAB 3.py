import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, 
                             QLineEdit, QTextEdit, QFormLayout)

class ReviewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Review')
        self.setGeometry(300, 300, 400, 300)

        layout = QFormLayout()

        self.title_input = QLineEdit()
        self.author_input = QLineEdit()
        self.review_output = QTextEdit()
        
        self.review_output.setPlaceholderText("QTextEdit")

        layout.addRow("Title", self.title_input)
        layout.addRow("Author", self.author_input)
        layout.addRow("Review", self.review_output)

        self.title_input.textChanged.connect(self.update_window_title)
        
        self.author_input.textChanged.connect(self.update_review_text)

        self.setLayout(layout)

    def update_window_title(self, text):
        self.setWindowTitle(text if text else "Review")

    def update_review_text(self, text):
        self.review_output.setPlainText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ReviewWindow()
    ex.show()
    sys.exit(app.exec())