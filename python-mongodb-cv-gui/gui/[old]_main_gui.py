# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(683, 711)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PushButton_AddImage = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_AddImage.setGeometry(QtCore.QRect(0, 70, 201, 91))
        self.PushButton_AddImage.setObjectName("PushButton_AddImage")
        self.CVDescription = QtWidgets.QTextEdit(self.centralwidget)
        self.CVDescription.setGeometry(QtCore.QRect(210, 180, 401, 211))
        self.CVDescription.setObjectName("CVDescription")
        self.CVImage = QtWidgets.QLabel(self.centralwidget)
        self.CVImage.setGeometry(QtCore.QRect(210, 70, 391, 91))
        self.CVImage.setFrameShape(QtWidgets.QFrame.Box)
        self.CVImage.setObjectName("CVImage")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(210, 410, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.PushButton_AddUser = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_AddUser.setGeometry(QtCore.QRect(0, 180, 201, 28))
        self.PushButton_AddUser.setObjectName("PushButton_AddUser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 683, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #     """my code"""
    #     self.PushButton_AddUser.clicked.connect(self.AddUserButton)
    #     self.PushButton_AddImage.clicked.connect(self.SetImageCV)
    # def AddUserButton(self):
    #     """
    #     adda user to the database
    #     """
    #     print('Added user!')

    # def SetImageCV(self):
    #     fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select Image","","Image Files (*.png *.jpg *jpeg  *.bpm)")
    #     if fileName:
    #         pixmap = QtGui.QPixmap(fileName)
    #         pixmap = pixmap.scaled(self.CVImage.width,self.CVImage.height,QtCore.Qt.KeepAspectRatio)
    #         self.CVImage.setPixmap(pixmap)
    #         self.CVImage.setAlignment(QtCore.Qt.AlignCenter)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PushButton_AddImage.setText(_translate("MainWindow", "Add Image"))
        self.CVDescription.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Insert CV description here</p></body></html>"))
        self.CVImage.setText(_translate("MainWindow", "Image Label"))
        self.PushButton_AddUser.setText(_translate("MainWindow", "Add User"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
