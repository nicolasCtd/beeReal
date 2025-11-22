from PyQt5.QtWidgets import QTableView, QMenu
from PyQt5.QtCore import QPoint, Qt, pyqtSignal, pyqtSlot, QModelIndex
from dataStruct import dataStructure as DS
from pathlib import Path
from ui.ImageViewer import ImageViewer 


def is_image_file(path):
    ext = path.lower().split('.')[-1]
    return ext in ('jpg', 'jpeg', 'png')

class BeeTableView(QTableView):

    measureAdded = pyqtSignal(DS.Measure)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.openMenu)
        self.doubleClicked.connect(self.slotItemDoulbeClicked)

        return

    def openMenu(self, pos: QPoint):
        index = self.indexAt(pos)
        if not index.isValid():
            return

        row = index.row()

        # menu
        menu = QMenu(self)

        act_view = menu.addAction("Voir l'image")
        act_mark = menu.addAction("Marquer pour retraiter")
        act_delete = menu.addAction("Supprimer")

        action = menu.exec_(self.mapToGlobal(pos))
        if action is None:
            return

        #if action == act_view:
            #self.parent().viewImage(row)

        #elif action == act_mark:
            #self.parent().markRowForRetry(row)

        #elif action == act_delete:
            #self.parent().deleteRow(row)


    def dragEnterEvent(self, event):
        # On accepte uniquement les fichiers
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

        return

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

        return
    

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            chemin = url.toLocalFile()
            if is_image_file(chemin):
                measure = DS.Measure("")
                measure.image = Path(chemin)
                self.model().appendMeasure(measure)
                self.measureAdded.emit(measure)
                


        event.acceptProposedAction()

    @pyqtSlot(QModelIndex)
    def slotItemDoulbeClicked(self, index : QModelIndex):
        imagePath = self.model().data(index, Qt.UserRole)
        self.viewer = ImageViewer(str(imagePath))
        self.viewer.show()
        return


