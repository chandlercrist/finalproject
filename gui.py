# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 500)  # Adjusted window size
        MainWindow.setMinimumSize(QtCore.QSize(750, 500))
        MainWindow.setMaximumSize(QtCore.QSize(750, 500))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.voting_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.voting_label.setGeometry(QtCore.QRect(320, 30, 151, 16))
        self.voting_label.setObjectName("voting_label")


        self.id_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(300, 70, 60, 16))
        self.id_label.setObjectName("id_label")


        self.id_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.id_input.setGeometry(QtCore.QRect(320, 70, 151, 21))
        self.id_input.setObjectName("id_input")


        self.candidates_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.candidates_label.setGeometry(QtCore.QRect(360, 120, 81, 16))
        self.candidates_label.setObjectName("candidates_label")


        self.candidate_one = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.candidate_one.setGeometry(QtCore.QRect(360, 140, 100, 20))
        self.candidate_one.setObjectName("candidate_one")


        self.candidate_two = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.candidate_two.setGeometry(QtCore.QRect(360, 170, 100, 20))
        self.candidate_two.setObjectName("candidate_two")


        self.submit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(330, 210, 113, 32))
        self.submit_button.setObjectName("submit_button")


        self.delete_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(330, 250, 113, 32))
        self.delete_button.setObjectName("delete_button")


        self.already_voted_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.already_voted_label.setGeometry(QtCore.QRect(320, 290, 151, 16))  # Adjusted position
        self.already_voted_label.setObjectName("already_voted_label")
        self.already_voted_label.setStyleSheet("color: red")
        self.already_voted_label.setText("Already Voted")
        self.already_voted_label.hide()

        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 24))
        self.menubar.setObjectName("menubar")
        self.menuTest_10 = QtWidgets.QMenu(parent=self.menubar)
        self.menuTest_10.setObjectName("menuTest_10")
        MainWindow.setMenuBar(self.menubar)


        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTest_10.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.voting_label.setText(_translate("MainWindow", "VOTING APPLICATION"))
        self.id_label.setText(_translate("MainWindow", "ID"))
        self.candidates_label.setText(_translate("MainWindow", "Candidates"))
        self.candidate_one.setText(_translate("MainWindow", "Jane"))
        self.candidate_two.setText(_translate("MainWindow", "John"))
        self.submit_button.setText(_translate("MainWindow", "SUBMIT"))
        self.delete_button.setText(_translate("MainWindow", "DELETE"))
        self.menuTest_10.setTitle(_translate("MainWindow", "Final Project"))
