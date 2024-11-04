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
url = input("Input url without http://: ")
url = "http://"+url
app = QApplication(sys.argv)
browser = Browser()
browser.load(url)
sys.exit(app.exec_())
