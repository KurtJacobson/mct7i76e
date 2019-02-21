# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mct7i76e.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 781, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.machineTab = QtWidgets.QWidget()
        self.machineTab.setObjectName("machineTab")
        self.tabWidget.addTab(self.machineTab, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tabWidget.addTab(self.tab_1, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionCheck = QtWidgets.QAction(MainWindow)
        self.actionCheck.setObjectName("actionCheck")
        self.actionBuild = QtWidgets.QAction(MainWindow)
        self.actionBuild.setObjectName("actionBuild")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionGeneralHelp = QtWidgets.QAction(MainWindow)
        self.actionGeneralHelp.setObjectName("actionGeneralHelp")
        self.actionTabHelp = QtWidgets.QAction(MainWindow)
        self.actionTabHelp.setObjectName("actionTabHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionCheck)
        self.menuFile.addAction(self.actionBuild)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionGeneralHelp)
        self.menuHelp.addAction(self.actionTabHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionCheck)
        self.toolBar.addAction(self.actionBuild)
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.machineTab), _translate("MainWindow", "Machine"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionCheck.setText(_translate("MainWindow", "Check"))
        self.actionBuild.setText(_translate("MainWindow", "Build"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionGeneralHelp.setText(_translate("MainWindow", "General Help"))
        self.actionTabHelp.setText(_translate("MainWindow", "Tab Help"))
        self.actionTabHelp.setShortcut(_translate("MainWindow", "F1"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

