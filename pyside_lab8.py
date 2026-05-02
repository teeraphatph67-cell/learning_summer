import sys
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView
class myWeb(QWebEngineView):
    def __init__(self):
        super().__init__()
        img = open('images.png', 'rb').read() #ดึงไฟล์ 101_0336.png เขา้มาแลว้อ่าน
        #ดึงตวัแปร img ทีÉเก็บไฟลร์ูปภาพมาแสดง โดยมีการกาํหนด setContent เป็ น image/png
        self. setContent(img,"image/png")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    web = myWeb()
    web.show()
    sys.exit(app.exec())