from PyQt5 import QtWidgets,QtGui,QtCore,Qt, uic
from pathlib import Path
import os
import sys
import time
import copy



print("PyQt version:",Qt.PYQT_VERSION_STR)
cwd = os.getcwd()  # Get the current working directory (cwd)
print('working directory:',cwd)
# cwd = os.chdir()
guiFolder=Path(__file__).resolve().parent.parent
print('guiFolder is:',guiFolder,' type is:',type(guiFolder))
uiFileName='/home/mike/Downloads/python-testing/python-mongodb-cv-gui'+'/gui/raw_gui_latest.ui'
print('uiFileName= ',uiFileName)


class MyCustomWidget(QtWidgets.QWidget):
    def __init__(self,fileNameLastImageUsed,pixmap :QtGui.QPixmap ,name,parentList :QtWidgets.QListWidget,
     parent=None):
        super(MyCustomWidget, self).__init__(parent)

        self.row = QtWidgets.QHBoxLayout()
        # print('MyCustomWidget filename is:\n')
        # print(fileNameLastImageUsed)
        # print('MyCustomWidget ',pixmap)
        
        self.label_user_image=QtWidgets.QLabel()
        pixmap=pixmap.scaled(100,100,QtCore.Qt.IgnoreAspectRatio)
        self.label_user_image.setPixmap(pixmap)
        self.QPushButtonDeleteUser=QtWidgets.QPushButton('delete')  
        self.QPushButtonDeleteUser.clicked.connect(self.DeleteUser)

        self.parentList=parentList
        self.QPushButtonViewUser=QtWidgets.QPushButton('view profile')  
        self.QPushButtonViewUser.clicked.connect(self.ViewUser)
        #construct custom widget
        self.row.addWidget(self.label_user_image)
        self.row.addWidget(QtWidgets.QLabel(name))       
        self.row.addWidget(self.QPushButtonViewUser)
        self.row.addWidget(self.QPushButtonDeleteUser)

        self.setLayout(self.row)

    def ViewUser(self):
        print('CHANGE LATER:',self.parentList.count())
    def DeleteUser(self):
        print('attempting to delete user...')
        # self.parentList.row()
        # self.parentList.removeItemWidget
        # self.parentList.takeItem()

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        
        super(Ui, self).__init__()
        # print('\npath of parent folder:\n ',Path(__file__).resolve().parent)
        
        
        uic.loadUi(uiFileName, self)
        #initialize some variables so the autocomplete recognizes them
        

        self.ButtonAddUser : QtWidgets.QPushButton  
        self.ButtonAddUser = self.findChild(QtWidgets.QPushButton, 'PushButton_AddUser') # Find the Tbutton
        self.ButtonAddUser.clicked.connect(self.AddUser) # Remember to pass the definition/method, not the return value!
        
        self.ButtonAddImageCV : QtWidgets.QPushButton
        self.ButtonAddImageCV=self.findChild(QtWidgets.QPushButton, 'PushButton_AddImage')
        self.ButtonAddImageCV.clicked.connect(self.SelectImageCV)
        
        self.CVDescription :QtWidgets.QTextEdit
        self.CVDescription=self.findChild(QtWidgets.QTextEdit,'CVUserDescription')
        
        self.CVUserName : QtWidgets.QTextEdit
        self.CVUserName=self.findChild(QtWidgets.QTextEdit,'CVUserName')

        self.CVImage:QtWidgets.QLabel
        self.CVImage=self.findChild(QtWidgets.QLabel,'CVImage')
        
        self.QListWidgetCVList:QtWidgets.QListWidget
        self.QListWidgetCVList=self.findChild(QtWidgets.QListWidget,'QListWidgetCVList')

        self.show()
        # print('type is:',type(self.CVImage))
        self.counter=0


    def AddUser(self):
        #check if all inputs are given
        print('type is: ',type(self.CVImage.pixmap()))
        if (not self.CVImage.pixmap()):
            print('no image set')
            return 0
        if (not self.CVUserName.toPlainText()):
            print('no name set')
            return 0
        if (not self.CVDescription.toPlainText()):
            print('no description set')
            return 0

        # user_image_pixmap=self.CVImage.pixmap()
        # print('local filename ',self.fileNameLastImageUsed)
        # user_description=self.CVDescription.toPlainText()
        # user_name=self.CVUserName.toPlainText()
                
        #create a new custom widget
        customWidget = MyCustomWidget(self.fileNameLastImageUsed,self._pixmap,self.CVUserName.toPlainText(),
        self.QListWidgetCVList)

        #set parent? of item
        item = QtWidgets.QListWidgetItem(self.QListWidgetCVList)
        #customize the hint of the item
        item.setSizeHint(customWidget.sizeHint())

        #add item to the list
        self.QListWidgetCVList.addItem(item)

        #change item to custom widget
        self.QListWidgetCVList.setItemWidget(item,customWidget)

        print('CVlist count: ',self.QListWidgetCVList.count())

        self.CVDescription.clear()
        self.CVUserName.clear()
        self.CVImage.clear()


        
    def FlashButtonAsGreen(self,name,user_description):
        # color from 0,255,0 (pure green) to 255,255,255 (pure white)
        print('added:',user,' with profile description: ',user_description)
        #flash the button

    def FlashButtonAsRed(self):
        pass

    def SelectImageCV(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select Image","","Image Files (*.png *.jpg *jpeg  *.bpm)")
        
        self.fileNameLastImageUsed=fileName
        print(self.fileNameLastImageUsed)
        if fileName:
            
            pixmap = QtGui.QPixmap(fileName)

            pixmap = pixmap.scaled(self.CVImage.width(),self.CVImage.height(),QtCore.Qt.IgnoreAspectRatio)
            self._pixmap=pixmap
            print('pixmap is: ',self._pixmap)
            self.CVImage.setPixmap(pixmap)

            self.CVImage.setAlignment(QtCore.Qt.AlignCenter)

def RunGraphics():
    app = QtWidgets.QApplication(sys.argv)
    return app
if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    tmp_app=RunGraphics()
    window = Ui()
    tmp_app.exec_()