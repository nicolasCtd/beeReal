from PyQt5.QtWidgets import QListWidget, QListWidgetItem

def isImageFile(path):
    """True if image file"""
    ext = path.lower().split('.')[-1]
    return ext in ('jpg', 'jpeg', 'png')

class SpecializedListWidget(QListWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(False)  # Only a receiver for instance
        return 
    

    def dragEnterEvent(self, event):
        """When entering the widgets"""
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            # Vérifie si au moins un fichier correspond à une image valide
            if any(isImageFile(url.toLocalFile()) for url in urls):
                event.acceptProposedAction()
            else:
                event.ignore()
        else:
            event.ignore()    
    
    def dragMoveEvent(self, event):
        """Important : Qt need to check acceptance at each move"""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()


    def dropEvent(self, event):
        """On drop"""
        for url in event.mimeData().urls():
            chemin = url.toLocalFile()
            if isImageFile(chemin):
                self.addItem(QListWidgetItem(chemin))
        event.acceptProposedAction()
        return