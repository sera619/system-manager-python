import sys
import traceback
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QSizeGrip,QPushButton, QProgressBar, QTableWidgetItem, QTableWidget
from PySide6.QtCore import *
from PySide6 import QtCore, QtGui
from PySide6 import *

from qt_material import *
import os, platform, shutil, psutil, datetime
from time import time, sleep
from multiprocessing import cpu_count
######################################## PRE-CONFIG #######################################
# UI IMPORTS
from ui_form import Ui_MainWindow

# GLOBALS 
plattform = {
    'linux' : 'Linux',
    'linux1': 'Linux',
    'linus2':'Linux',
    'darwin':'OS X',
    'wind32': 'Windows'
}

#############################################################################################

#################################### WORKER CONFIG ##########################################

class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)
    

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker,self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        
        self.kwargs['progress_callback'] = self.signals.progress
    
    @Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()        
        self.ui.setupUi(self)


        
        # Window Styling
        apply_stylesheet(app, theme="dark_cyan.xml")  
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowTitle('UTIL Manager')
        self.setWindowIcon(QtGui.QIcon(":/icons/assets/icons/out/airplay.png"))
        
        # Config Shadow
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setXOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
                
        # Window Controll Buttons
        self.ui.minimize_window_btn.clicked.connect(lambda: self.showMinimized())
        self.ui.maximize_window_btn.clicked.connect(lambda: self.restoreWindow())
        self.ui.close_window_btn.clicked.connect(lambda: self.close())
        
        # Page Controll Buttons
        self.ui.cpu_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cpu_memory))
        self.ui.harddrive_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.harddrive))
        self.ui.power_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.battery_frame))
        self.ui.display_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.system_monitor))
        self.ui.resource_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.activities))
        self.ui.network_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.networks))
    
        QSizeGrip(self.ui.size_grip)
        # Progressbar reset
        self.ui.bat_charge_bar.setValue(0)
        self.ui.bat_timeleft_bar.setValue(0)
        self.ui.cpu_per_bar.setValue(0)
        self.ui.cpu_cour_bar.setValue(0)
    
    
        # Window Controlls
        # Move Window
        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
                    
    
        self.ui.header_frame.mouseMoveEvent = moveWindow
        self.ui.menu_button.clicked.connect(lambda: self.slideLeftMenu())

        for w in self.ui.menu_frame.findChildren(QPushButton):
            w.clicked.connect(self.applyButtonStyle)
            
     
        self.threadpool= QtCore.QThreadPool()
        
        self.psutilThreat()
        self.system_info()
        self.processes()
        self.storage()
       # self.sensors()
        self.networks()
    ############################### PRE Config END ####################################
    
    def psutilThreat(self):
        worker = Worker(self.cpu_ram)
        worker.signals.result.connect(self.printOutput)
        worker.signals.finished.connect(self.threadComplete)
        worker.signals.progress.connect(self.progressFunc)
        
        self.threadpool.start(worker)
        
        """
        battery_worker = Worker(self.battery)
        battery_worker.signals.result.connect(self.printOutput)
        battery_worker.signals.finished.connect(self.threadComplete)
        battery_worker.signals.progress.connect(self.progressFunc)
        
        self.threadpool.start(battery_worker)
        """
    
    
    
    # Worker printer
    def printOutput(self, s):
        print(s)
            
    
    # Worker thread-complete
    def threadComplete(self):
        print('THRED COMPLETE')
    
    def progressFunc(self, n):
        # n = progress value
        print("%d%% done" % n)
        
    # Get Mouseevents
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
    
    
    # Menuslider 
    def slideLeftMenu(self):
        width = self.ui.menu_slider.width()
        if width == 0:
            newWidth = 75
            
        else:
            newWidth = 0
        self.animation = QPropertyAnimation(self.ui.menu_slider, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()    
    
    
    # Change maximize Icon
    def restoreWindow(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.maximize_window_btn.setIcon(QtGui.QIcon(u":/icons_svg/assets/icons/svg/chevrons-up.svg"))
        else:
            self.showMaximized()
            self.ui.maximize_window_btn.setIcon(QtGui.QIcon(u":/icons_svg/assets/icons/svg/chevrons-down.svg"))
    
    
    def applyButtonStyle(self):
        for w in self.ui.menu_frame.findChildren(QPushButton):
            if w.objectName() != self.sender().objectName():

                w.setStyleSheet("border-bottom: none;")

        self.sender().setStyleSheet("border-bottom: 2px solid")
        return
    
    
    # Get System Information
    def system_info(self):
        time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.ui.sytem_time_text.setText(str(time))  
        date = datetime.datetime.now().strftime("%Y-%m-%d")          
        self.ui.sytem_date_text.setText(str(date))

        
        self.ui.system_machine_text.setText(platform.machine())
        self.ui.system_version_text.setText(platform.version())
        self.ui.system_plattform_text.setText(platform.platform())
        self.ui.system_os_text.setText(platform.system())
        self.ui.system_cpu_text.setText(platform.processor())
        
    # Battery function
    def battery(self, progress_callback):
        while True:
            batt = psutil.sensors_battery()
            
            if not hasattr(psutil, "sensors_battery"):
                self.ui.bat_status_text.setText("Plattform not supported")
                
            if batt is None:
                self.ui.bat_status_text.setText("No battery installed")
            
            if batt.power_plugged:
                self.ui.bat_charge_txt.setText(str(round(batt.percent, 2))+" %")
                self.ui.bat_lefttime_text.setText("N/A")
                if batt.percent < 100:
                    self.ui.bat_status_text.setText("Charging")
                else:
                    self.ui.bat_status_text.setText("Fully Charged")
                
                self.ui.bat_plug_text.setText("Yes")
            
            else:
                self.ui.bat_charge_txt.setText(str(round(batt.percent, 2))+" %")
                self.ui.bat_lefttime_text.setText(self.secs2hours(batt.secsleft))
                if batt.percent < 100:
                    self.ui.bat_status_text.setText("Discharging")
                else:
                    self.ui.bat_status_text.setText("Fully Charged")
                self.ui.bat_plug_text.setText("No")
                
    def cpu_ram(self,progress_callback):
        while True:
            core = cpu_count()
            self.ui.cpu_cour_text.setText(str(core))
            
            totalRam = 1.0
            totalRam = psutil.virtual_memory()[0] * totalRam
            totalRam = totalRam / (1024 * 1024 * 1024)
            self.ui.ram_total_text.setText(str("{:.4f}".format(totalRam)+ ' GB'))
            self.ui.ram_total_bar.setValue(0)
            
            
            ramFree = 1.0  
            ramFree = psutil.virtual_memory()[1] * ramFree
            ramFree = ramFree / (1024 * 1024 * 1024)
            self.ui.ram_free_text.setText(str("{:.4f}".format(ramFree)+ ' GB'))
            self.ui.ram_free_bar.setMaximum(totalRam)
            self.ui.ram_free_bar.setValue(ramFree)
            
            ramUsed = 1.0
            ramUsed = psutil.virtual_memory()[3] * ramUsed
            ramUsed = ramUsed / (1024 * 1024 * 1024)
            self.ui.ram_usage_text.setText(str("{:.4f}".format(ramUsed)+ ' GB'))
            self.ui.ram_used_bar.setMaximum(totalRam)
            self.ui.ram_used_bar.setValue(ramUsed)
            
            
            availRam = 1.0
            availRam = psutil.virtual_memory()[4] * availRam
            availRam = availRam / (1024 * 1024 * 1024)
            self.ui.ram_available_text.setText(str("{:.4f}".format(availRam)+ ' GB'))
            self.ui.ram_avail_bar.setMaximum(totalRam)
            self.ui.ram_avail_bar.setValue(availRam)
                
            
            ramUsages = 1.0
            ramUsages = str(psutil.virtual_memory()[2]) + ' %'
            self.ui.ram_used_text.setText(str("{:.4f}".format(ramUsages) + ' GB'))
            self.ui.ram_use_bar.setValue(availRam)
            self.ui.ram_use_bar.setValue(ramUsages)
            #print(ramUsages)
            
            cpuPer = psutil.cpu_percent()
            self.ui.cpu_per_text.setText(str(cpuPer) + " %")
            self.ui.cpu_per_bar.setValue(cpuPer)

            cpuMainCore = psutil.cpu_count(logical=False)
            self.ui.cpu_main_txt.setText(str(cpuMainCore))
            

            sleep(1)
            
    def secs2hours(self, secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%d:%02d:%02d (H:M:S)" % (hh, mm, ss)
    
    def processes(self):
        for x in psutil.pids():
            # Create New Row
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)

            try:        
                process = psutil.Process(x)
                # # Create widget
                # print(process)
                # # rowPosition = row number
                # # x = column number
                    

                self.create_table_widget(rowPosition, 0, str(process.pid), "tableWidget")
                self.create_table_widget(rowPosition, 1, process.name(), "tableWidget")
                self.create_table_widget(rowPosition, 2, process.status(), "tableWidget")
                self.create_table_widget(rowPosition, 3, str(datetime.datetime.utcfromtimestamp(process.create_time()).strftime('%Y-%m-%d %H:%M:%S')), "tableWidget")

                # create an cell widget
                suspend_btn = QPushButton(self.ui.tableWidget)
                suspend_btn.setText('Suspend')
                suspend_btn.setStyleSheet("color: brown")
                self.ui.tableWidget.setCellWidget(rowPosition, 4, suspend_btn)

                resume_btn = QPushButton(self.ui.tableWidget)
                resume_btn.setText('Resume')
                resume_btn.setStyleSheet("color: green")
                self.ui.tableWidget.setCellWidget(rowPosition, 5, resume_btn)

                terminate_btn = QPushButton(self.ui.tableWidget)
                terminate_btn.setText('Terminate')
                terminate_btn.setStyleSheet("color: orange")
                self.ui.tableWidget.setCellWidget(rowPosition, 6, terminate_btn)

                kill_btn = QPushButton(self.ui.tableWidget)
                kill_btn.setText('Kill')
                kill_btn.setStyleSheet("color: red")
                self.ui.tableWidget.setCellWidget(rowPosition, 7, kill_btn)
            except Exception as e:
                print(e)

        # print(self.ui.tableWidget.findItems("sleeping", QtCore.Qt.MatchFlag.MatchRecursive|QtCore.Qt.MatchFlag.MatchExactly))
        self.ui.activity_search.textChanged.connect(self.findName)



    def findName(self):
        name = self.ui.activity_search.text().lower()
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 1)
            # if the search is *not* in the item's text *do not hide* the row
            self.ui.tableWidget.setRowHidden(row, name not in item.text().lower())


    # STORAGE PARTITIONS

    def storage(self):
        storage_device = psutil.disk_partitions(all=False)
        z = 0
        for x in storage_device:
            # print(x)
            # Create New Row
            rowPosition = self.ui.storageTable.rowCount()
            self.ui.storageTable.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, x.device, "storageTable")
            self.create_table_widget(rowPosition, 1, x.mountpoint, "storageTable")
            self.create_table_widget(rowPosition, 2, x.fstype, "storageTable")
            self.create_table_widget(rowPosition, 3, x.opts, "storageTable")

            if sys.platform == 'linux' or sys.platform == 'linux1' or sys.platform == 'linux2':
                self.create_table_widget(rowPosition, 4, str(x.maxfile), "storageTable")
                self.create_table_widget(rowPosition, 5, str(x.maxpath), "storageTable")
            else:
                self.create_table_widget(rowPosition, 4, "Function not available on " + platforms[sys.platform], "storageTable")
                self.create_table_widget(rowPosition, 5, "Function not available on " + platforms[sys.platform], "storageTable")

            # print(psutil.disk_usage(x.device))
            disk_usage = shutil.disk_usage(x.mountpoint)
            # print(disk_usage.total)
            self.create_table_widget(rowPosition, 6, str((disk_usage.total / (1024 * 1024 * 1024))) + " GB", "storageTable")
            self.create_table_widget(rowPosition, 7, str((disk_usage.free / (1024 * 1024 * 1024))) + " GB", "storageTable")
            #self.create_table_widget(rowPosition, 8, str((disk_usage.used / (1024 * 1024 * 1024))) + " GB", "storageTable")
            # print(shutil.disk_usage(x.mountpoint))

            full_disk = (disk_usage.used / disk_usage.total) * 100
            progressBar = QProgressBar(self.ui.storageTable)
            progressBar.setObjectName(u"progressBar")
            progressBar.setValue(full_disk)
            self.ui.storageTable.setCellWidget(rowPosition, 9, progressBar)

    # SENSORS INFORMATION
    def sensors(self):
        global platforms
        # PSUTIL Sensors urrently only works on linux platform
        if sys.platform == 'linux' or sys.platform == 'linux1' or sys.platform == 'linux2':           
            for x in psutil.sensors_temperatures():
                for y in psutil.sensors_temperatures()[x]:
                    # Create New Row
                    rowPosition = self.ui.sensorTable.rowCount()
                    self.ui.sensorTable.insertRow(rowPosition)

                    self.create_table_widget(rowPosition, 0, x, "sensorTable")
                    self.create_table_widget(rowPosition, 1, y.label, "sensorTable")
                    self.create_table_widget(rowPosition, 2, str(y.current), "sensorTable")
                    self.create_table_widget(rowPosition, 3, str(y.high), "sensorTable")
                    self.create_table_widget(rowPosition, 4, str(y.critical), "sensorTable")

                    temp_per = (y.current / y.high) * 100

                    progressBar = QProgressBar(self.ui.sensorTable)
                    progressBar.setObjectName(u"progressBar")
                    progressBar.setValue(temp_per)
                    self.ui.sensorTable.setCellWidget(rowPosition, 5, progressBar)
        else:
            global platforms
            # Create New Row
            rowPosition = self.ui.sensorTable.rowCount()
            self.ui.sensorTable.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, "Function not supported on " + platforms[sys.platform], "sensorTable")
            self.create_table_widget(rowPosition, 1, "N/A", "sensorTable")
            self.create_table_widget(rowPosition, 2, "N/A", "sensorTable")
            self.create_table_widget(rowPosition, 3, "N/A", "sensorTable")
            self.create_table_widget(rowPosition, 4, "N/A", "sensorTable")
            self.create_table_widget(rowPosition, 5, "N/A", "sensorTable")

    # A FUNCTION THAT CREATES TABLE WIDGETS
    def create_table_widget(self, rowPosition, columnPosition, text, tableName):
        qtablewidgetitem = QTableWidgetItem()
        getattr(self.ui, tableName).setItem(rowPosition, columnPosition, qtablewidgetitem)
        qtablewidgetitem = getattr(self.ui, tableName).item(rowPosition, columnPosition)

        qtablewidgetitem.setText(text);

    # NETWORKS FUNCTIONS 
    def networks(self):
        # NET STATS
        for x in psutil.net_if_stats():
            z = psutil.net_if_stats()
            # Create New Row
            rowPosition = self.ui.net_stats_table.rowCount()
            self.ui.net_stats_table.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, x, "net_stats_table")
            self.create_table_widget(rowPosition, 1, str(z[x].isup), "net_stats_table")
            self.create_table_widget(rowPosition, 2, str(z[x].duplex), "net_stats_table")
            self.create_table_widget(rowPosition, 3, str(z[x].speed), "net_stats_table")
            self.create_table_widget(rowPosition, 4, str(z[x].mtu), "net_stats_table")

        # NET IO COUNTERS
        for x in psutil.net_io_counters(pernic=True):
            z = psutil.net_io_counters(pernic=True)
            # Create New Row
            rowPosition = self.ui.net_io_table.rowCount()
            self.ui.net_io_table.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, x, "net_io_table")
            self.create_table_widget(rowPosition, 1, str(z[x].bytes_sent), "net_io_table")
            self.create_table_widget(rowPosition, 2, str(z[x].bytes_recv), "net_io_table")
            self.create_table_widget(rowPosition, 3, str(z[x].packets_sent), "net_io_table")
            self.create_table_widget(rowPosition, 4, str(z[x].packets_recv), "net_io_table")
            self.create_table_widget(rowPosition, 5, str(z[x].errin), "net_io_table")
            self.create_table_widget(rowPosition, 6, str(z[x].errout), "net_io_table")
            self.create_table_widget(rowPosition, 7, str(z[x].dropin), "net_io_table")
            self.create_table_widget(rowPosition, 8, str(z[x].dropout), "net_io_table")

        # NET ADDRESSES
        for x in psutil.net_if_addrs():
            z = psutil.net_if_addrs()
            # print(z)
            for y in z[x]:  
                # Create New Row
                rowPosition = self.ui.net_addresses_table.rowCount()
                self.ui.net_addresses_table.insertRow(rowPosition)

                self.create_table_widget(rowPosition, 0, str(x), "net_addresses_table")
                self.create_table_widget(rowPosition, 1, str(y.family), "net_addresses_table")
                self.create_table_widget(rowPosition, 2, str(y.address), "net_addresses_table")
                self.create_table_widget(rowPosition, 3, str(y.netmask), "net_addresses_table")
                self.create_table_widget(rowPosition, 4, str(y.broadcast), "net_addresses_table")


        # NET CONNECTIONS
        for x in psutil.net_connections():
            z = psutil.net_connections()
            # Create New Row
            rowPosition = self.ui.net_connections_table.rowCount()
            self.ui.net_connections_table.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, str(x.fd), "net_connections_table")
            self.create_table_widget(rowPosition, 1, str(x.family), "net_connections_table")
            self.create_table_widget(rowPosition, 2, str(x.type), "net_connections_table")
            self.create_table_widget(rowPosition, 3, str(x.laddr), "net_connections_table")
            self.create_table_widget(rowPosition, 4, str(x.raddr), "net_connections_table")
            self.create_table_widget(rowPosition, 5, str(x.status), "net_connections_table")
            self.create_table_widget(rowPosition, 6, str(x.pid), "net_connections_table")
            
    
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


    