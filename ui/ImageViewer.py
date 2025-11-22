from ui import ImageViewer_ui as ui
from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ImageViewer(QWidget):
    def __init__(self, image_path : str, parent=None):
        super().__init__(parent)
        self.ui = ui.Ui_ImageViewer()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene(self.ui.graphicsView)
        self.ui.graphicsView.setScene(self.scene)

        self.pixmap = QPixmap(image_path)
        self.image_item = self.scene.addPixmap(self.pixmap)

        # Adapt view to image
        img_w = self.pixmap.width()
        img_h = self.pixmap.height()

        self.ui.graphicsView.setMinimumSize(img_w, img_h)

        # Optionnal: Drag
        self.ui.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)


    def showEvent(self, a0):        
        # fit viewer to image
        self.ui.graphicsView.fitInView(self.image_item, Qt.KeepAspectRatio)
        return super().showEvent(a0)

    

