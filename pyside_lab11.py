import sys
from PySide6.QtWidgets import *
class myMessageBox(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('กล่องขอ้ความ') #ชืÉอหัวของโปรแกรม

    def closeEvent(self, event): #กาํหนดการกระทาํ เมÉอืมีความตอ้งการปิดโปรแกรม
        reply = QMessageBox.question(self, 'Message',
            "คุณแน่ใจนะว่าคุณตอ้งการปิดโปรแกรม?", QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept() #ยนัยืนการกระทาํคือปิดโปรแกรมครบั
        else:
            event.ignore() #ไม่สนใจการกระทาํ คือไม่ปิดโปรแกรมครับ

app = QApplication(sys.argv)
qb = myMessageBox() #อา้งอิงคลาส MessageBox
qb.show() #แสดงผล
sys.exit(app.exec())