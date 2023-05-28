# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchEngine.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction,QMessageBox
from UI.CustomElements.Popup import CustomPopup



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)

        MainWindow.setFixedSize(922, 713)
        cols = ['SKU_ID', 'Sku', 'Product_line', 'Brand', 'Sales', 'Price']
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 30, 921, 180))
        
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(cols)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.setVerticalHeaderLabels(["","","","",""])
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 250, 921, 180))
        self.tableWidget_2.setRowCount(5)
        self.tableWidget_2.setVerticalHeaderLabels(["","","","",""])
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setHorizontalHeaderLabels(cols)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(150)
        
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 480, 921, 201))
        self.tableWidget_3.setRowCount(5)
        self.tableWidget_3.setVerticalHeaderLabels(["","","","",""])
        self.tableWidget_3.setColumnCount(6)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setHorizontalHeaderLabels(cols)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(150)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1001, 31))
        self.label.setLineWidth(10)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 220, 1001, 31))
        self.label_2.setLineWidth(10)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 450, 1001, 31))
        self.label_3.setLineWidth(10)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 922, 22))
        self.menubar.setObjectName("menubar")
        self.menuSearch = QtWidgets.QMenu(self.menubar)
        self.menuSearch.setObjectName("menuSearch")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar.addAction(self.menuSearch.menuAction())

        self.label.setText("Top Sales")
        self.label_2.setText("Highest Sales")
        self.label_3.setText("Lowest Sales")
        self.menuSearch.setTitle("Search")
        self.toolBar.setWindowTitle("toolBar")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def setData(self):
        pass
    def popup(self):
        popup = CustomPopup(self)
        popup.exec_()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Search Engine")
        qAction = QAction("popup",MainWindow)
        qAction.triggered.connect(self.popup)
        self.menuSearch.addAction(qAction)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
