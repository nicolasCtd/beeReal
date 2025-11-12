from PyQt5.QtWidgets import QListWidget

class SpecializedListWidget(QListWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        print("Initializing specializedListWidget")
        #self.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        return 