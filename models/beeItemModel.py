from PyQt5.QtGui import QStandardItemModel, QStandardItem
from dataStruct import dataStructure as DS
from PyQt5.QtCore import Qt

class BeeItemModel(QStandardItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setHorizontalHeaderLabels(["name", "Status"])
        return 

    def appendMeasure(self, measure : DS.Measure):
        imagePath = str(measure.image)
        
        if measure.treated:
            checkState = Qt.Checked
        else:
            checkState = Qt.Unchecked                

        nameItem = QStandardItem(imagePath)
        statusItem = QStandardItem()

        statusItem.setCheckable(True)          
        statusItem.setCheckState(checkState)
        self.appendRow([nameItem, statusItem])

        return