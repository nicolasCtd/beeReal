from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from dataStruct import dataStructure as DS
from PyQt5.QtCore import Qt, QFileInfo

def getStatusItemWithIcon(statusTreated):
    statusItem = QStandardItem()
    statusItem.setText("") 
    statusIcon = None
    if statusTreated:
        statusIcon = QIcon(":images/checkmark-32.png")
    else:
        statusIcon = QIcon(":images/x-mark-32.png")

    statusItem.setIcon(statusIcon)
    statusItem.setData(statusTreated, Qt.UserRole)    
    return statusItem

class BeeItemModel(QStandardItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setHorizontalHeaderLabels(["name", "Status"])
        return 

    def appendMeasure(self, measure : DS.Measure):
        imagePath = str(measure.image)        

        nameItem = QStandardItem(QFileInfo(imagePath).fileName())
        nameItem.setEditable(False)

        statusItem = getStatusItemWithIcon(measure.treated)
        self.appendRow([nameItem, statusItem])

        return
    