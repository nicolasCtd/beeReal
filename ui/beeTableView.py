from PyQt5.QtWidgets import QTableView
from models.beeItemModel import BeeItemModel


def is_image_file(path):
    ext = path.lower().split('.')[-1]
    return ext in ('jpg', 'jpeg', 'png')

class BeeTableView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

        return

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
                model = self.model()
                model.addNewImage(chemin)


        event.acceptProposedAction()

