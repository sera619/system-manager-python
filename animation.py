import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QTimer, QObject, QPropertyAnimation
from PySide6.QtWidgets import QWidget, QPushButton
from time import strftime, localtime




class ContactButton(QPushButton):
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self,*args, **kwargs)
        self.anim = QPropertyAnimation(self, b'')