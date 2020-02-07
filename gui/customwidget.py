from PyQt5 import QtWidgets, QtGui, QtCore, Qt, uic
from pathlib import Path
import os
import sys
import time
import copy

class MyCustomWidget(QtWidgets.QWidget):
    def __init__(self,
                 fileNameLastImageUsed: str,
                 pixmap: QtGui.QPixmap,
                 name: str,
                 itemReference: QtWidgets.QListWidgetItem,
                 parentList: QtWidgets.QListWidget,
                 parent=None):
        super(MyCustomWidget, self).__init__(parent)

        self.itemReference=itemReference
        print('item reference is: ',itemReference)
        self.row = QtWidgets.QHBoxLayout()
        # print('MyCustomWidget filename is:\n')
        # print(fileNameLastImageUsed)
        # print('MyCustomWidget ',pixmap)

        self.label_user_image = QtWidgets.QLabel()
        self.pixmap = pixmap.scaled(100, 100, QtCore.Qt.IgnoreAspectRatio)
        self.label_user_image.setPixmap(self.pixmap)
        self.QPushButtonDeleteUser = QtWidgets.QPushButton('delete')
        self.QPushButtonDeleteUser.clicked.connect(self.DeleteUser)

        self.parentList = parentList
        self.QPushButtonViewUser = QtWidgets.QPushButton('view profile')
        self.QPushButtonViewUser.clicked.connect(self.ViewUser)
        # construct custom widget
        self.row.addWidget(self.label_user_image)
        self.row.addWidget(QtWidgets.QLabel(name))
        self.row.addWidget(self.QPushButtonViewUser)
        self.row.addWidget(self.QPushButtonDeleteUser)

        self.setLayout(self.row)

    def ViewUser(self):
        print('CHANGE LATER:', self.parentList.count())

    def DeleteUser(self):
        itemRow= self.parentList.row(self.itemReference)
        self.parentList.takeItem(itemRow)
        print('new CVlist count:',self.parentList.count())
        # self.parentList.row()
        # self.parentList.removeItemWidget
        # self.parentList.takeItem()
