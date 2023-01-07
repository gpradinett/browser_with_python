#!/usr/bin/python3


import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

app = QApplication(sys.argv)
view = QWebEngineView()
view.load(QUrl("https://www.google.com"))
view.show()
sys.exit(app.exec_())

