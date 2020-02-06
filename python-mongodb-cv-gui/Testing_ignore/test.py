from PyQt5 import QtWidgets
class MyCustomWidget(QWidget):
    def __init__(self, name, parent=None):
        super(MyCustomWidget, self).__init__(parent)

        self.row = QHBoxLayout()

        self.row.addWidget(QLabel(name))
        self.row.addWidget(QPushButton("view"))
        self.row.addWidget(QPushButton("select"))

        self.setLayout(self.row)

# Create the list
mylist = QListWidget()

# Add to list a new item (item is simply an entry in your list)
item = QListWidgetItem(mylist)
mylist.addItem(item)

# Instanciate a custom widget 
row = MyCustomWidget()
item.setSizeHint(row.minimumSizeHint())

# Associate the custom widget to the list entry
mylist.setItemWidget(item, row)