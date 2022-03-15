# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formKaHVmQ.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import Icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(911, 552)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setStyleSheet(u"\n"
"	border:none;\n"
"\n"
"\n"
"background-color: rgb(17, 33, 68);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 8, 0, 0)
        self.header_left_fram = QFrame(self.header_frame)
        self.header_left_fram.setObjectName(u"header_left_fram")
        self.header_left_fram.setMinimumSize(QSize(0, 0))
        self.header_left_fram.setFrameShape(QFrame.StyledPanel)
        self.header_left_fram.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_fram)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(8, 0, 0, 0)
        self.menu_button = QPushButton(self.header_left_fram)
        self.menu_button.setObjectName(u"menu_button")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.menu_button.setFont(font)
        self.menu_button.setAutoFillBackground(False)
        self.menu_button.setStyleSheet(u"color: rgb(0, 0, 0);")
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/out/align-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_button.setIcon(icon)
        self.menu_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.menu_button)


        self.horizontalLayout.addWidget(self.header_left_fram, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setAutoFillBackground(False)
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.header_icon = QLabel(self.header_center_frame)
        self.header_icon.setObjectName(u"header_icon")
        font1 = QFont()
        font1.setPointSize(10)
        self.header_icon.setFont(font1)
        self.header_icon.setPixmap(QPixmap(u":/icons/assets/icons/out/airplay.png"))
        self.header_icon.setScaledContents(False)
        self.header_icon.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.header_icon, 0, Qt.AlignLeft)

        self.header_text = QLabel(self.header_center_frame)
        self.header_text.setObjectName(u"header_text")
        font2 = QFont()
        font2.setFamilies([u"a Another Tag"])
        font2.setPointSize(50)
        font2.setBold(False)
        font2.setItalic(False)
        self.header_text.setFont(font2)
        self.header_text.setStyleSheet(u"font: 50pt \"a Another Tag\";\n"
"color: rgb(2, 17, 31);")
        self.header_text.setMidLineWidth(0)
        self.header_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.header_text, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.header_center_frame, 0, Qt.AlignTop)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        font3 = QFont()
        font3.setPointSize(8)
        self.header_right_frame.setFont(font3)
        self.header_right_frame.setStyleSheet(u"*{border:none;}")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.minimize_window_btn = QPushButton(self.header_right_frame)
        self.minimize_window_btn.setObjectName(u"minimize_window_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/icons/out/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_btn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.minimize_window_btn)

        self.maximize_window_btn = QPushButton(self.header_right_frame)
        self.maximize_window_btn.setObjectName(u"maximize_window_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons_svg/assets/icons/svg/chevrons-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_window_btn.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.maximize_window_btn)

        self.close_window_btn = QPushButton(self.header_right_frame)
        self.close_window_btn.setObjectName(u"close_window_btn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/icons/out/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_btn.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.close_window_btn)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_7 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.main_menu_con = QFrame(self.main_frame)
        self.main_menu_con.setObjectName(u"main_menu_con")
        sizePolicy.setHeightForWidth(self.main_menu_con.sizePolicy().hasHeightForWidth())
        self.main_menu_con.setSizePolicy(sizePolicy)
        self.main_menu_con.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.main_menu_con.setFrameShape(QFrame.StyledPanel)
        self.main_menu_con.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.main_menu_con)
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 0, 0, 0)
        self.menu_frame = QFrame(self.main_menu_con)
        self.menu_frame.setObjectName(u"menu_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menu_frame.sizePolicy().hasHeightForWidth())
        self.menu_frame.setSizePolicy(sizePolicy1)
        self.menu_frame.setMinimumSize(QSize(40, 0))
        self.menu_frame.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_20 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.cpu_button = QPushButton(self.menu_frame)
        self.cpu_button.setObjectName(u"cpu_button")
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/icons/out/cpu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cpu_button.setIcon(icon4)
        self.cpu_button.setIconSize(QSize(32, 32))

        self.verticalLayout_20.addWidget(self.cpu_button)

        self.harddrive_button = QPushButton(self.menu_frame)
        self.harddrive_button.setObjectName(u"harddrive_button")
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/icons/out/database.png", QSize(), QIcon.Normal, QIcon.Off)
        self.harddrive_button.setIcon(icon5)
        self.harddrive_button.setIconSize(QSize(32, 32))

        self.verticalLayout_20.addWidget(self.harddrive_button)

        self.power_button = QPushButton(self.menu_frame)
        self.power_button.setObjectName(u"power_button")
        icon6 = QIcon()
        icon6.addFile(u":/icons/assets/icons/out/battery-charging.png", QSize(), QIcon.Normal, QIcon.Off)
        self.power_button.setIcon(icon6)
        self.power_button.setIconSize(QSize(32, 32))

        self.verticalLayout_20.addWidget(self.power_button)

        self.resource_button = QPushButton(self.menu_frame)
        self.resource_button.setObjectName(u"resource_button")
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/icons/out/activity.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resource_button.setIcon(icon7)
        self.resource_button.setIconSize(QSize(32, 32))

        self.verticalLayout_20.addWidget(self.resource_button)

        self.display_button = QPushButton(self.menu_frame)
        self.display_button.setObjectName(u"display_button")
        self.display_button.setMinimumSize(QSize(40, 0))
        icon8 = QIcon()
        icon8.addFile(u":/icons/assets/icons/out/monitor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.display_button.setIcon(icon8)
        self.display_button.setIconSize(QSize(32, 32))

        self.verticalLayout_20.addWidget(self.display_button)

        self.network_button = QPushButton(self.menu_frame)
        self.network_button.setObjectName(u"network_button")
        icon9 = QIcon()
        icon9.addFile(u":/icons/assets/icons/out/wifi.png", QSize(), QIcon.Normal, QIcon.Off)
        self.network_button.setIcon(icon9)
        self.network_button.setIconSize(QSize(32, 32))

        self.verticalLayout_20.addWidget(self.network_button)


        self.horizontalLayout_8.addWidget(self.menu_frame, 0, Qt.AlignLeft)

        self.menu_slider = QFrame(self.main_menu_con)
        self.menu_slider.setObjectName(u"menu_slider")
        sizePolicy1.setHeightForWidth(self.menu_slider.sizePolicy().hasHeightForWidth())
        self.menu_slider.setSizePolicy(sizePolicy1)
        self.menu_slider.setMinimumSize(QSize(0, 0))
        self.menu_slider.setMaximumSize(QSize(0, 600))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.menu_slider.setFont(font4)
        self.menu_slider.setFrameShape(QFrame.StyledPanel)
        self.menu_slider.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.menu_slider)
        self.verticalLayout_19.setSpacing(35)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.menu_slider)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(0, 0))
        self.label_3.setSizeIncrement(QSize(200, 204))
        self.label_3.setBaseSize(QSize(0, 0))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setKerning(True)
        self.label_3.setFont(font5)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_19.addWidget(self.label_3)

        self.label_58 = QLabel(self.menu_slider)
        self.label_58.setObjectName(u"label_58")
        font6 = QFont()
        font6.setBold(True)
        self.label_58.setFont(font6)

        self.verticalLayout_19.addWidget(self.label_58)

        self.label_5 = QLabel(self.menu_slider)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setSizeIncrement(QSize(200, 200))
        self.label_5.setBaseSize(QSize(200, 200))
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setKerning(True)
        self.label_5.setFont(font7)
        self.label_5.setScaledContents(False)

        self.verticalLayout_19.addWidget(self.label_5)

        self.label_4 = QLabel(self.menu_slider)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 0))
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setSizeIncrement(QSize(200, 200))
        self.label_4.setBaseSize(QSize(200, 200))
        self.label_4.setFont(font7)
        self.label_4.setScaledContents(False)

        self.verticalLayout_19.addWidget(self.label_4)

        self.label_7 = QLabel(self.menu_slider)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setSizeIncrement(QSize(200, 200))
        self.label_7.setBaseSize(QSize(200, 200))
        self.label_7.setFont(font7)
        self.label_7.setScaledContents(False)

        self.verticalLayout_19.addWidget(self.label_7)

        self.label_6 = QLabel(self.menu_slider)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 0))
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6.setSizeIncrement(QSize(200, 200))
        self.label_6.setBaseSize(QSize(200, 200))
        self.label_6.setFont(font7)
        self.label_6.setScaledContents(False)

        self.verticalLayout_19.addWidget(self.label_6)

        self.label_10 = QLabel(self.menu_slider)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 0))
        self.label_10.setMaximumSize(QSize(16777215, 16777215))
        self.label_10.setSizeIncrement(QSize(0, 0))
        self.label_10.setBaseSize(QSize(200, 200))
        self.label_10.setFont(font7)
        self.label_10.setMidLineWidth(-1)
        self.label_10.setScaledContents(False)

        self.verticalLayout_19.addWidget(self.label_10)


        self.horizontalLayout_8.addWidget(self.menu_slider, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.main_menu_con, 0, Qt.AlignLeft)

        self.main_content = QFrame(self.main_frame)
        self.main_content.setObjectName(u"main_content")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_content.sizePolicy().hasHeightForWidth())
        self.main_content.setSizePolicy(sizePolicy2)
        self.main_content.setFrameShape(QFrame.StyledPanel)
        self.main_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main_content)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"color: rgb(153, 193, 241);")
        self.cpu_memory = QWidget()
        self.cpu_memory.setObjectName(u"cpu_memory")
        self.verticalLayout_5 = QVBoxLayout(self.cpu_memory)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_35 = QLabel(self.cpu_memory)
        self.label_35.setObjectName(u"label_35")
        font8 = QFont()
        font8.setPointSize(16)
        font8.setBold(True)
        font8.setItalic(True)
        self.label_35.setFont(font8)

        self.verticalLayout_5.addWidget(self.label_35)

        self.cpu_info_frame = QFrame(self.cpu_memory)
        self.cpu_info_frame.setObjectName(u"cpu_info_frame")
        sizePolicy2.setHeightForWidth(self.cpu_info_frame.sizePolicy().hasHeightForWidth())
        self.cpu_info_frame.setSizePolicy(sizePolicy2)
        self.cpu_info_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.cpu_info_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(50)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cpu_per_bar = QProgressBar(self.cpu_info_frame)
        self.cpu_per_bar.setObjectName(u"cpu_per_bar")
        self.cpu_per_bar.setValue(24)

        self.gridLayout_2.addWidget(self.cpu_per_bar, 9, 2, 1, 1)

        self.label_13 = QLabel(self.cpu_info_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font6)

        self.gridLayout_2.addWidget(self.label_13, 9, 0, 1, 1, Qt.AlignBottom)

        self.cpu_per_text = QLabel(self.cpu_info_frame)
        self.cpu_per_text.setObjectName(u"cpu_per_text")

        self.gridLayout_2.addWidget(self.cpu_per_text, 8, 1, 1, 1)

        self.cpu_cour_bar = QProgressBar(self.cpu_info_frame)
        self.cpu_cour_bar.setObjectName(u"cpu_cour_bar")
        self.cpu_cour_bar.setValue(24)

        self.gridLayout_2.addWidget(self.cpu_cour_bar, 8, 2, 1, 1)

        self.label_14 = QLabel(self.cpu_info_frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font6)

        self.gridLayout_2.addWidget(self.label_14, 8, 0, 1, 1)

        self.cpu_main_txt = QLabel(self.cpu_info_frame)
        self.cpu_main_txt.setObjectName(u"cpu_main_txt")

        self.gridLayout_2.addWidget(self.cpu_main_txt, 9, 1, 1, 1, Qt.AlignLeft|Qt.AlignBottom)

        self.cpu_cour_text = QLabel(self.cpu_info_frame)
        self.cpu_cour_text.setObjectName(u"cpu_cour_text")

        self.gridLayout_2.addWidget(self.cpu_cour_text, 7, 1, 1, 1, Qt.AlignBottom)

        self.label_11 = QLabel(self.cpu_info_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font6)

        self.gridLayout_2.addWidget(self.label_11, 7, 0, 1, 1, Qt.AlignBottom)


        self.verticalLayout_5.addWidget(self.cpu_info_frame)

        self.ram_frame = QFrame(self.cpu_memory)
        self.ram_frame.setObjectName(u"ram_frame")
        self.ram_frame.setLayoutDirection(Qt.LeftToRight)
        self.ram_frame.setFrameShape(QFrame.StyledPanel)
        self.ram_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.ram_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(55)
        self.ram_available_text = QLabel(self.ram_frame)
        self.ram_available_text.setObjectName(u"ram_available_text")

        self.gridLayout_3.addWidget(self.ram_available_text, 1, 1, 1, 1)

        self.ram_used_text = QLabel(self.ram_frame)
        self.ram_used_text.setObjectName(u"ram_used_text")

        self.gridLayout_3.addWidget(self.ram_used_text, 2, 1, 1, 1)

        self.label_17 = QLabel(self.ram_frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font6)

        self.gridLayout_3.addWidget(self.label_17, 0, 0, 1, 1)

        self.label_20 = QLabel(self.ram_frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font6)

        self.gridLayout_3.addWidget(self.label_20, 3, 0, 1, 1)

        self.ram_usage_text = QLabel(self.ram_frame)
        self.ram_usage_text.setObjectName(u"ram_usage_text")

        self.gridLayout_3.addWidget(self.ram_usage_text, 4, 1, 1, 1)

        self.ram_free_text = QLabel(self.ram_frame)
        self.ram_free_text.setObjectName(u"ram_free_text")

        self.gridLayout_3.addWidget(self.ram_free_text, 3, 1, 1, 1)

        self.label_18 = QLabel(self.ram_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font6)

        self.gridLayout_3.addWidget(self.label_18, 1, 0, 1, 1)

        self.label_25 = QLabel(self.ram_frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font6)

        self.gridLayout_3.addWidget(self.label_25, 4, 0, 1, 1)

        self.label_19 = QLabel(self.ram_frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font6)

        self.gridLayout_3.addWidget(self.label_19, 2, 0, 1, 1)

        self.ram_total_text = QLabel(self.ram_frame)
        self.ram_total_text.setObjectName(u"ram_total_text")

        self.gridLayout_3.addWidget(self.ram_total_text, 0, 1, 1, 1)

        self.ram_total_bar = QProgressBar(self.ram_frame)
        self.ram_total_bar.setObjectName(u"ram_total_bar")
        self.ram_total_bar.setValue(24)

        self.gridLayout_3.addWidget(self.ram_total_bar, 0, 2, 1, 1)

        self.ram_avail_bar = QProgressBar(self.ram_frame)
        self.ram_avail_bar.setObjectName(u"ram_avail_bar")
        self.ram_avail_bar.setValue(24)

        self.gridLayout_3.addWidget(self.ram_avail_bar, 1, 2, 1, 1)

        self.ram_used_bar = QProgressBar(self.ram_frame)
        self.ram_used_bar.setObjectName(u"ram_used_bar")
        self.ram_used_bar.setValue(24)

        self.gridLayout_3.addWidget(self.ram_used_bar, 2, 2, 1, 1)

        self.ram_free_bar = QProgressBar(self.ram_frame)
        self.ram_free_bar.setObjectName(u"ram_free_bar")
        self.ram_free_bar.setValue(24)

        self.gridLayout_3.addWidget(self.ram_free_bar, 3, 2, 1, 1)

        self.ram_use_bar = QProgressBar(self.ram_frame)
        self.ram_use_bar.setObjectName(u"ram_use_bar")
        self.ram_use_bar.setValue(24)

        self.gridLayout_3.addWidget(self.ram_use_bar, 4, 2, 1, 1)


        self.verticalLayout_5.addWidget(self.ram_frame)

        self.stackedWidget.addWidget(self.cpu_memory)
        self.battery_frame = QWidget()
        self.battery_frame.setObjectName(u"battery_frame")
        sizePolicy1.setHeightForWidth(self.battery_frame.sizePolicy().hasHeightForWidth())
        self.battery_frame.setSizePolicy(sizePolicy1)
        self.battery_frame.setMinimumSize(QSize(727, 0))
        self.verticalLayout_6 = QVBoxLayout(self.battery_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 2, 5, 2)
        self.label_36 = QLabel(self.battery_frame)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font8)

        self.verticalLayout_6.addWidget(self.label_36, 0, Qt.AlignVCenter)

        self.battery_info = QFrame(self.battery_frame)
        self.battery_info.setObjectName(u"battery_info")
        sizePolicy.setHeightForWidth(self.battery_info.sizePolicy().hasHeightForWidth())
        self.battery_info.setSizePolicy(sizePolicy)
        self.battery_info.setFrameShape(QFrame.StyledPanel)
        self.battery_info.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.battery_info)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(60)
        self.gridLayout_4.setVerticalSpacing(20)
        self.bat_charge_txt = QLabel(self.battery_info)
        self.bat_charge_txt.setObjectName(u"bat_charge_txt")
        self.bat_charge_txt.setFont(font1)

        self.gridLayout_4.addWidget(self.bat_charge_txt, 6, 1, 1, 1)

        self.bat_lefttime_text = QLabel(self.battery_info)
        self.bat_lefttime_text.setObjectName(u"bat_lefttime_text")
        self.bat_lefttime_text.setFont(font1)

        self.gridLayout_4.addWidget(self.bat_lefttime_text, 7, 1, 1, 1)

        self.label_27 = QLabel(self.battery_info)
        self.label_27.setObjectName(u"label_27")
        font9 = QFont()
        font9.setPointSize(10)
        font9.setBold(True)
        self.label_27.setFont(font9)

        self.gridLayout_4.addWidget(self.label_27, 6, 0, 1, 1)

        self.bat_charge_bar = QProgressBar(self.battery_info)
        self.bat_charge_bar.setObjectName(u"bat_charge_bar")
        self.bat_charge_bar.setValue(24)

        self.gridLayout_4.addWidget(self.bat_charge_bar, 6, 3, 1, 1)

        self.label_28 = QLabel(self.battery_info)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font9)

        self.gridLayout_4.addWidget(self.label_28, 4, 0, 1, 1)

        self.label_29 = QLabel(self.battery_info)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font9)

        self.gridLayout_4.addWidget(self.label_29, 7, 0, 1, 1)

        self.bat_timeleft_bar = QProgressBar(self.battery_info)
        self.bat_timeleft_bar.setObjectName(u"bat_timeleft_bar")
        self.bat_timeleft_bar.setValue(24)

        self.gridLayout_4.addWidget(self.bat_timeleft_bar, 7, 3, 1, 1)

        self.label_30 = QLabel(self.battery_info)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font9)

        self.gridLayout_4.addWidget(self.label_30, 5, 0, 1, 1, Qt.AlignTop)

        self.bat_status_text = QLabel(self.battery_info)
        self.bat_status_text.setObjectName(u"bat_status_text")
        self.bat_status_text.setFont(font1)

        self.gridLayout_4.addWidget(self.bat_status_text, 4, 1, 1, 1)

        self.bat_plug_text = QLabel(self.battery_info)
        self.bat_plug_text.setObjectName(u"bat_plug_text")
        self.bat_plug_text.setFont(font1)

        self.gridLayout_4.addWidget(self.bat_plug_text, 5, 1, 1, 1, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.battery_info, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.battery_frame)
        self.harddrive = QWidget()
        self.harddrive.setObjectName(u"harddrive")
        self.verticalLayout_10 = QVBoxLayout(self.harddrive)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_51 = QLabel(self.harddrive)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font8)

        self.verticalLayout_10.addWidget(self.label_51, 0, Qt.AlignVCenter)

        self.storageTable = QTableWidget(self.harddrive)
        if (self.storageTable.columnCount() < 8):
            self.storageTable.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.storageTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.storageTable.setObjectName(u"storageTable")

        self.verticalLayout_10.addWidget(self.storageTable)

        self.stackedWidget.addWidget(self.harddrive)
        self.system_monitor = QWidget()
        self.system_monitor.setObjectName(u"system_monitor")
        self.verticalLayout_7 = QVBoxLayout(self.system_monitor)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_41 = QLabel(self.system_monitor)
        self.label_41.setObjectName(u"label_41")
        font10 = QFont()
        font10.setFamilies([u"Cantarell"])
        font10.setPointSize(16)
        font10.setBold(True)
        font10.setItalic(True)
        self.label_41.setFont(font10)
        self.label_41.setStyleSheet(u"color: rgb(153, 193, 241);")

        self.verticalLayout_7.addWidget(self.label_41)

        self.system_info = QFrame(self.system_monitor)
        self.system_info.setObjectName(u"system_info")
        self.system_info.setFrameShape(QFrame.StyledPanel)
        self.system_info.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.system_info)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_46 = QLabel(self.system_info)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font9)

        self.gridLayout_5.addWidget(self.label_46, 2, 3, 1, 1)

        self.label_49 = QLabel(self.system_info)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font9)

        self.gridLayout_5.addWidget(self.label_49, 3, 3, 1, 1)

        self.sytem_date_text = QLabel(self.system_info)
        self.sytem_date_text.setObjectName(u"sytem_date_text")
        self.sytem_date_text.setFont(font1)

        self.gridLayout_5.addWidget(self.sytem_date_text, 3, 2, 1, 1)

        self.label_47 = QLabel(self.system_info)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font9)

        self.gridLayout_5.addWidget(self.label_47, 1, 3, 1, 1)

        self.system_machine_text = QLabel(self.system_info)
        self.system_machine_text.setObjectName(u"system_machine_text")
        self.system_machine_text.setFont(font1)

        self.gridLayout_5.addWidget(self.system_machine_text, 2, 4, 1, 1)

        self.label_37 = QLabel(self.system_info)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font9)

        self.gridLayout_5.addWidget(self.label_37, 3, 1, 1, 1)

        self.label_39 = QLabel(self.system_info)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font9)

        self.gridLayout_5.addWidget(self.label_39, 1, 1, 1, 1)

        self.system_plattform_text = QLabel(self.system_info)
        self.system_plattform_text.setObjectName(u"system_plattform_text")
        self.system_plattform_text.setFont(font1)

        self.gridLayout_5.addWidget(self.system_plattform_text, 1, 2, 1, 1)

        self.label_38 = QLabel(self.system_info)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font9)

        self.gridLayout_5.addWidget(self.label_38, 2, 1, 1, 1)

        self.system_cpu_text = QLabel(self.system_info)
        self.system_cpu_text.setObjectName(u"system_cpu_text")
        self.system_cpu_text.setFont(font1)

        self.gridLayout_5.addWidget(self.system_cpu_text, 1, 4, 1, 1)

        self.system_version_text = QLabel(self.system_info)
        self.system_version_text.setObjectName(u"system_version_text")
        self.system_version_text.setFont(font1)

        self.gridLayout_5.addWidget(self.system_version_text, 2, 2, 1, 1)

        self.sytem_time_text = QLabel(self.system_info)
        self.sytem_time_text.setObjectName(u"sytem_time_text")
        self.sytem_time_text.setFont(font1)

        self.gridLayout_5.addWidget(self.sytem_time_text, 3, 4, 1, 1)

        self.system_os_text = QLabel(self.system_info)
        self.system_os_text.setObjectName(u"system_os_text")
        self.system_os_text.setFont(font9)

        self.gridLayout_5.addWidget(self.system_os_text, 0, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.system_info)

        self.stackedWidget.addWidget(self.system_monitor)
        self.activities = QWidget()
        self.activities.setObjectName(u"activities")
        self.verticalLayout_8 = QVBoxLayout(self.activities)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_2 = QFrame(self.activities)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.frame_2)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font8)

        self.horizontalLayout_10.addWidget(self.label_50)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 0, 5, 0)
        self.activity_search = QLineEdit(self.frame_4)
        self.activity_search.setObjectName(u"activity_search")
        self.activity_search.setMinimumSize(QSize(300, 0))
        self.activity_search.setStyleSheet(u"background: #fff;")
        self.activity_search.setCursorPosition(0)
        self.activity_search.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.activity_search)

        self.searchbutton = QPushButton(self.frame_4)
        self.searchbutton.setObjectName(u"searchbutton")
        font11 = QFont()
        font11.setPointSize(12)
        font11.setBold(False)
        self.searchbutton.setFont(font11)
        icon10 = QIcon()
        icon10.addFile(u":/icons_svg/assets/icons/svg/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchbutton.setIcon(icon10)
        self.searchbutton.setIconSize(QSize(22, 22))

        self.horizontalLayout_9.addWidget(self.searchbutton)


        self.horizontalLayout_10.addWidget(self.frame_4, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.frame = QFrame(self.activities)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_9.addWidget(self.tableWidget)


        self.verticalLayout_8.addWidget(self.frame)

        self.frame_3 = QFrame(self.activities)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font9)
        self.pushButton_3.setStyleSheet(u"\n"
"color: rgb(0, 255, 255);")

        self.horizontalLayout_11.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font9)
        self.pushButton_4.setStyleSheet(u"\n"
"color: rgb(0, 255, 255);")

        self.horizontalLayout_11.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font9)
        self.pushButton_5.setStyleSheet(u"\n"
"color: rgb(0, 255, 255);")

        self.horizontalLayout_11.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font9)
        self.pushButton_6.setStyleSheet(u"\n"
"color: rgb(0, 255, 255);")

        self.horizontalLayout_11.addWidget(self.pushButton_6)


        self.verticalLayout_8.addWidget(self.frame_3, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.activities)
        self.networks = QWidget()
        self.networks.setObjectName(u"networks")
        self.verticalLayout_12 = QVBoxLayout(self.networks)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea = QScrollArea(self.networks)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 706, 458))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_13.setSpacing(20)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_9)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.frame_9)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font10)

        self.verticalLayout_18.addWidget(self.label_57, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_13.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_5)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.frame_5)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font)

        self.verticalLayout_14.addWidget(self.label_53)

        self.net_stats_table = QTableWidget(self.frame_5)
        if (self.net_stats_table.columnCount() < 6):
            self.net_stats_table.setColumnCount(6)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        self.net_stats_table.setObjectName(u"net_stats_table")

        self.verticalLayout_14.addWidget(self.net_stats_table)


        self.verticalLayout_13.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_6)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.frame_6)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font)

        self.verticalLayout_15.addWidget(self.label_54)

        self.net_io_table = QTableWidget(self.frame_6)
        if (self.net_io_table.columnCount() < 9):
            self.net_io_table.setColumnCount(9)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(5, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(6, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(7, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(8, __qtablewidgetitem30)
        self.net_io_table.setObjectName(u"net_io_table")

        self.verticalLayout_15.addWidget(self.net_io_table)


        self.verticalLayout_13.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_7)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.frame_7)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font)

        self.verticalLayout_16.addWidget(self.label_55)

        self.net_addresses_table = QTableWidget(self.frame_7)
        if (self.net_addresses_table.columnCount() < 5):
            self.net_addresses_table.setColumnCount(5)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.net_addresses_table.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        self.net_addresses_table.setObjectName(u"net_addresses_table")

        self.verticalLayout_16.addWidget(self.net_addresses_table)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_8)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.frame_8)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font)

        self.verticalLayout_17.addWidget(self.label_56)

        self.net_connections_table = QTableWidget(self.frame_8)
        if (self.net_connections_table.columnCount() < 7):
            self.net_connections_table.setColumnCount(7)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(3, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(4, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(5, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.net_connections_table.setHorizontalHeaderItem(6, __qtablewidgetitem42)
        self.net_connections_table.setObjectName(u"net_connections_table")

        self.verticalLayout_17.addWidget(self.net_connections_table)


        self.verticalLayout_13.addWidget(self.frame_8)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.networks)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_7.addWidget(self.main_content)

        self.rightfram = QFrame(self.main_frame)
        self.rightfram.setObjectName(u"rightfram")
        sizePolicy.setHeightForWidth(self.rightfram.sizePolicy().hasHeightForWidth())
        self.rightfram.setSizePolicy(sizePolicy)
        self.rightfram.setLayoutDirection(Qt.LeftToRight)
        self.rightfram.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.rightfram.setFrameShape(QFrame.StyledPanel)
        self.rightfram.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.rightfram)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.label = QLabel(self.rightfram)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(20, 20))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(2, 17, 31, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 170, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.label.setPalette(palette)
        font12 = QFont()
        font12.setFamilies([u"a Another Tag"])
        font12.setPointSize(40)
        font12.setBold(False)
        font12.setItalic(False)
        font12.setUnderline(False)
        self.label.setFont(font12)
        self.label.setStyleSheet(u"font: 40pt \"a Another Tag\";\n"
"color: rgb(2, 17, 31);")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignRight|Qt.AlignTop)

        self.frame_10 = QFrame(self.rightfram)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"color: black;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.git_btn = QPushButton(self.frame_10)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.git_btn)
        self.git_btn.setObjectName(u"git_btn")
        self.git_btn.setFont(font6)
        icon11 = QIcon()
        icon11.addFile(u":/icons_svg/assets/icons/svg/github.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.git_btn.setIcon(icon11)
        self.git_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_11.addWidget(self.git_btn, 0, Qt.AlignLeft)

        self.codepen_btn = QPushButton(self.frame_10)
        self.buttonGroup.addButton(self.codepen_btn)
        self.codepen_btn.setObjectName(u"codepen_btn")
        self.codepen_btn.setFont(font6)
        icon12 = QIcon()
        icon12.addFile(u":/icons_svg/assets/icons/svg/codepen.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.codepen_btn.setIcon(icon12)
        self.codepen_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_11.addWidget(self.codepen_btn, 0, Qt.AlignLeft)

        self.yt_btn = QPushButton(self.frame_10)
        self.buttonGroup.addButton(self.yt_btn)
        self.yt_btn.setObjectName(u"yt_btn")
        self.yt_btn.setFont(font6)
        icon13 = QIcon()
        icon13.addFile(u":/icons_svg/assets/icons/svg/youtube.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.yt_btn.setIcon(icon13)
        self.yt_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_11.addWidget(self.yt_btn, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.frame_10, 0, Qt.AlignLeft)

        self.label_2 = QLabel(self.rightfram)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font13 = QFont()
        font13.setFamilies([u"FontAwesome"])
        font13.setPointSize(11)
        font13.setBold(True)
        font13.setItalic(True)
        self.label_2.setFont(font13)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"color: rgb(212, 212, 212);\n"
"font: 700 italic 11pt \"FontAwesome\";")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setIndent(-1)

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignRight|Qt.AlignBottom)


        self.horizontalLayout_7.addWidget(self.rightfram)

        self.main_content.raise_()
        self.main_menu_con.raise_()
        self.rightfram.raise_()

        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.footer_left_frame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.footer_text = QLabel(self.footer_left_frame)
        self.footer_text.setObjectName(u"footer_text")
        font14 = QFont()
        font14.setFamilies([u"Bitstream Vera Sans"])
        font14.setPointSize(10)
        font14.setBold(True)
        font14.setItalic(True)
        self.footer_text.setFont(font14)
        self.footer_text.setStyleSheet(u"color: rgb(61, 56, 70);")
        self.footer_text.setMargin(10)

        self.verticalLayout_2.addWidget(self.footer_text)


        self.horizontalLayout_5.addWidget(self.footer_left_frame)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.footer_help_btn = QPushButton(self.footer_right_frame)
        self.footer_help_btn.setObjectName(u"footer_help_btn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/assets/icons/out/help-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.footer_help_btn.setIcon(icon14)
        self.footer_help_btn.setIconSize(QSize(28, 28))

        self.horizontalLayout_6.addWidget(self.footer_help_btn, 0, Qt.AlignRight|Qt.AlignBottom)


        self.horizontalLayout_5.addWidget(self.footer_right_frame, 0, Qt.AlignRight)

        self.size_grip = QWidget(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(0, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_button.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.header_icon.setText("")
        self.header_text.setText(QCoreApplication.translate("MainWindow", u"SYS MANAGER", None))
        self.minimize_window_btn.setText("")
        self.maximize_window_btn.setText("")
        self.close_window_btn.setText("")
        self.cpu_button.setText("")
        self.harddrive_button.setText("")
        self.power_button.setText("")
        self.resource_button.setText("")
        self.display_button.setText("")
        self.network_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tasks", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"CPU and Memory", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CPU MAIN", None))
        self.cpu_per_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"CPU PER", None))
        self.cpu_main_txt.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.cpu_cour_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CPU COUR", None))
        self.ram_available_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.ram_used_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Total RAM", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Free RAM", None))
        self.ram_usage_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.ram_free_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Avaible RAM", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"RAM Usage", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Used RAM", None))
        self.ram_total_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.bat_charge_txt.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.bat_lefttime_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Time Left", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Plugged In", None))
        self.bat_status_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.bat_plug_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"STORAGE", None))
        ___qtablewidgetitem = self.storageTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Device", None));
        ___qtablewidgetitem1 = self.storageTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Mount Point", None));
        ___qtablewidgetitem2 = self.storageTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"OPTS", None));
        ___qtablewidgetitem3 = self.storageTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Max File", None));
        ___qtablewidgetitem4 = self.storageTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Max Path", None));
        ___qtablewidgetitem5 = self.storageTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Total Storage", None));
        ___qtablewidgetitem6 = self.storageTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Used Storage", None));
        ___qtablewidgetitem7 = self.storageTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Free Storage", None));
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"System Time", None))
        self.sytem_date_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.system_machine_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"System Date", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Plattform", None))
        self.system_plattform_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.system_cpu_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_version_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.sytem_time_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_os_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Activies", None))
        self.activity_search.setInputMask("")
        self.activity_search.setText("")
        self.activity_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Serach for active Task", None))
        self.searchbutton.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"PROCESS ID", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"PROCESS NAME", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"PROCESS STATUS", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"STARTED", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"SUSPEND", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"RESUME", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"TERMINATE", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"KILL", None));
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"SUSPEND", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"RESUME", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"TERMINATE", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"KILL", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        ___qtablewidgetitem16 = self.net_stats_table.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"NAME", None));
        ___qtablewidgetitem17 = self.net_stats_table.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"x", None));
        ___qtablewidgetitem18 = self.net_stats_table.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"ISUP", None));
        ___qtablewidgetitem19 = self.net_stats_table.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"DUPLEX", None));
        ___qtablewidgetitem20 = self.net_stats_table.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"SPEED", None));
        ___qtablewidgetitem21 = self.net_stats_table.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"MTU", None));
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Network IO Counter", None))
        ___qtablewidgetitem22 = self.net_io_table.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"BYTES SEND", None));
        ___qtablewidgetitem23 = self.net_io_table.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"BYTES RECEIVED", None));
        ___qtablewidgetitem24 = self.net_io_table.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"PACKETS SEND", None));
        ___qtablewidgetitem25 = self.net_io_table.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"PACKETS RECEIVED", None));
        ___qtablewidgetitem26 = self.net_io_table.horizontalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem27 = self.net_io_table.horizontalHeaderItem(5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"ERR IN", None));
        ___qtablewidgetitem28 = self.net_io_table.horizontalHeaderItem(6)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"ERR OUT", None));
        ___qtablewidgetitem29 = self.net_io_table.horizontalHeaderItem(7)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"DROP IN", None));
        ___qtablewidgetitem30 = self.net_io_table.horizontalHeaderItem(8)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"DROP OUT", None));
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Network Adresses", None))
        ___qtablewidgetitem31 = self.net_addresses_table.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"FAMILY", None));
        ___qtablewidgetitem32 = self.net_addresses_table.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"ADDRESS", None));
        ___qtablewidgetitem33 = self.net_addresses_table.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"NETMASK", None));
        ___qtablewidgetitem34 = self.net_addresses_table.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"ROADCAS", None));
        ___qtablewidgetitem35 = self.net_addresses_table.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"PTP", None));
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Network Connections", None))
        ___qtablewidgetitem36 = self.net_connections_table.horizontalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"FD", None));
        ___qtablewidgetitem37 = self.net_connections_table.horizontalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"FAMILY", None));
        ___qtablewidgetitem38 = self.net_connections_table.horizontalHeaderItem(2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"FAMILY", None));
        ___qtablewidgetitem39 = self.net_connections_table.horizontalHeaderItem(3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"LADDR", None));
        ___qtablewidgetitem40 = self.net_connections_table.horizontalHeaderItem(4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"RADDR", None));
        ___qtablewidgetitem41 = self.net_connections_table.horizontalHeaderItem(5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem42 = self.net_connections_table.horizontalHeaderItem(6)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.git_btn.setText(QCoreApplication.translate("MainWindow", u"GITHUB", None))
        self.codepen_btn.setText(QCoreApplication.translate("MainWindow", u"CODEPEN", None))
        self.yt_btn.setText(QCoreApplication.translate("MainWindow", u"YOUTUBE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>App<br/>Designed And<br/>Developed By<br>&#169; S3R43o3</p></body></html>", None))
        self.footer_text.setText(QCoreApplication.translate("MainWindow", u"Version 0.8.4 | all Rights reserved 2021 - 2022 \u00a9 S3R43o3", None))
        self.footer_help_btn.setText("")
    # retranslateUi

