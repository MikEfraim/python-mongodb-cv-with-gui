from PyQt5 import QtWidgets, QtGui, QtCore, Qt, uic
from pathlib import Path

from customwidget import MyCustomWidget

import os
import sys
import time
import copy


print("PyQt version:", Qt.PYQT_VERSION_STR)
# cwd = os.getcwd()
# print('working directory:', cwd)
guiFolder = Path(__file__).resolve().parent
# print('guiFolder is:', guiFolder)
uiFilePath = guiFolder.__str__() + \
    '/raw_gui_latest.ui'
print('uiFilePath= ', uiFilePath)


class Ui(QtWidgets.QMainWindow):
    def __init__(self):

        super(Ui, self).__init__()
        # print('\npath of parent folder:\n ',Path(__file__).resolve().parent)

        uic.loadUi(uiFilePath, self)
        # initialize some variables so the autocomplete recognizes them

        self.ButtonAddUser: QtWidgets.QPushButton
        self.ButtonAddUser = self.findChild(
            QtWidgets.QPushButton, 'PushButton_AddUser')  # Find the Tbutton
        # Remember to pass the definition/method, not the return value!
        self.ButtonAddUser.clicked.connect(self.AddUser)

        self.ButtonAddImageCV: QtWidgets.QPushButton
        self.ButtonAddImageCV = self.findChild(
            QtWidgets.QPushButton, 'PushButton_AddImage')
        self.ButtonAddImageCV.clicked.connect(self.SelectImageCV)

        self.CVDescription: QtWidgets.QTextEdit
        self.CVDescription = self.findChild(
            QtWidgets.QTextEdit, 'CVUserDescription')

        self.CVUserName: QtWidgets.QTextEdit
        self.CVUserName = self.findChild(QtWidgets.QTextEdit, 'CVUserName')

        self.CVImage: QtWidgets.QLabel
        self.CVImage = self.findChild(QtWidgets.QLabel, 'CVImage')

        self.QListWidgetCVList: QtWidgets.QListWidget
        self.QListWidgetCVList = self.findChild(
            QtWidgets.QListWidget, 'QListWidgetCVList')

        self.show()
        # print('type is:',type(self.CVImage))
        self.counter = 0

    def AddUser(self):
        # check if all inputs are given
        print('type is: ', type(self.CVImage.pixmap()))
        if (not self.CVImage.pixmap()):
            print('no image set')
            return 0
        if (not self.CVUserName.toPlainText()):
            print('no name set')
            return 0
        if (not self.CVDescription.toPlainText()):
            print('no description set')
            return 0

        # set parent? of item
        item = QtWidgets.QListWidgetItem(self.QListWidgetCVList)

        # create a new custom widget
        customWidget = MyCustomWidget(self.fileNameLastImageUsed,
                                      self.tmpPixmap,
                                      self.CVUserName.toPlainText(),
                                      self.CVDescription.toPlainText(),
                                      item,
                                      self.QListWidgetCVList)

        # set the item to the sizehint of the custom widget
        item.setSizeHint(customWidget.sizeHint())

        # add item to the list
        self.QListWidgetCVList.addItem(item)

        # change item to custom widget
        self.QListWidgetCVList.setItemWidget(item, customWidget)

        # print('CVlist count: ', self.QListWidgetCVList.count())

        # clear user input
        self.CVDescription.clear()
        self.CVUserName.clear()
        self.CVImage.clear()

    def FlashButtonAsGreen(self, name, user_description):
        # color from 0,255,0 (pure green) to 255,255,255 (pure white)
        print('added:', user, ' with profile description: ', user_description)
        # flash the button

    def SelectImageCV(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Image", "", "Image Files (*.png *.jpg *jpeg  *.bpm)")

        self.fileNameLastImageUsed = fileName
        print(self.fileNameLastImageUsed)
        if fileName:

            pixmap = QtGui.QPixmap(fileName)

            pixmap = pixmap.scaled(self.CVImage.width(),
                                   self.CVImage.height(),
                                   QtCore.Qt.IgnoreAspectRatio)
            self.tmpPixmap = pixmap
            print('pixmap is: ', self.tmpPixmap)
            self.CVImage.setPixmap(pixmap)

            self.CVImage.setAlignment(QtCore.Qt.AlignCenter)


def RunGraphics():
    app = QtWidgets.QApplication(sys.argv)
    return app


if __name__ == "__main__":
    # app =
    tmp_app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    tmp_app.exec_()
