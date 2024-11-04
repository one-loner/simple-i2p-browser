import os
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar

# Устанавливаем переменные окружения для HTTP и HTTPS прокси
os.environ["http_proxy"] = "http://127.0.0.1:4444"
os.environ["https_proxy"] = "http://127.0.0.1:4444"

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем веб-просмотр
        self.view = QWebEngineView(self)

        # Создаем панель инструментов
        self.toolbar = QToolBar(self)
        self.addToolBar(self.toolbar)

        # Устанавливаем центральный виджет главного окна
        self.setCentralWidget(self.view)

        # Отображаем главное окно
        self.resize(800, 600)  # Размер окна браузера
        self.show()

    def load(self, url):
        self.view.load(QUrl(url))


# URL для загрузки
#url = "http://reg.i2p"
#url = "http://x4d22hk3d2gzk7vhv6gooobwllgy2yqe7bzuxt2cfyrqw5o5zhoq.b32.i2p"
#url = "http://trus.i2p/?i2paddresshelper=2Ls-kzoAXDZb4Rxqk19he5ra9~aQkVpDAMvMf3Ys-ujYuz6TOgBcNlvhHGqTX2F7mtr39pCRWkMAy8x~diz66Ni7PpM6AFw2W-EcapNfYXua2vf2kJFaQwDLzH92LPro2Ls-kzoAXDZb4Rxqk19he5ra9~aQkVpDAMvMf3Ys-ujYuz6TOgBcNlvhHGqTX2F7mtr39pCRWkMAy8x~diz66Ni7PpM6AFw2W-EcapNfYXua2vf2kJFaQwDLzH92LPro2Ls-kzoAXDZb4Rxqk19he5ra9~aQkVpDAMvMf3Ys-ujYuz6TOgBcNlvhHGqTX2F7mtr39pCRWkMAy8x~diz66Ni7PpM6AFw2W-EcapNfYXua2vf2kJFaQwDLzH92LPro2Ls-kzoAXDZb4Rxqk19he5ra9~aQkVpDAMvMf3Ys-ujYuz6TOgBcNlvhHGqTX2F7mtr39pCRWkMAy8x~diz66EDEV2hJYIMa1OJYclyJvCWyrmXIuAr6cfNmqWMvtQMUBQAEAAcAAA=="
#url = "http://trusishka.i2p/?i2paddresshelper=giJST7FEXa0ei84hbpQRRtX1xyhghz9CBh3wTcbFwKXUNXJmAuANYwhQS83A7q9JA8orOkSj1foFsVR9fMuXGbdTBxbkCCca8eLIZvguICLmL3OBuHjFc3RGpV7~rD1IGe20wIfxzdr3o5P0okeZHg7ZQI6arkH~c5E-8vLpsMjTqphIrTxR9gB8y85UCNN30uXdLf-2yA-3iLe81Gn~pVrOXj~yvfl3X-mOZ~rBJfWVMa~9YihTdVS2o6pSr8JEukeg7k8ZpZGAze41IFNgw6CnHwhc2rk1LU6YD-CTaVm9MBr8KmHaKDIDHFvr0pfTH4ZR8k77p7PCPDKJgjZXtOimQk9h~0MC5KBZc~yXF7yJGCVZG7fqWzDyatSQpFyHoed9Icq9bmBLnag6m-gnbA0aKanBMEJfHN3OmY6z1lbb2XhzPBY38oSthGudWzDHYe6oKpcXHBCw7UrakQlDCMiKM~EynHaxSZnLO5hZQZk11l8yoLWbYG-~a~xtz1XDBQAEAAcAAA=="
url = input("Input url without http://: ")
url = "http://"+url
app = QApplication(sys.argv)
browser = Browser()
browser.load(url)
sys.exit(app.exec_())
