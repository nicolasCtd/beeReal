from ui import ImageViewer_ui as ui
from PyQt5.QtWidgets import QWidget, QGraphicsScene
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QRectF, pyqtSignal

class ImageViewer(QWidget):

    goNext = pyqtSignal()
    stopShow = pyqtSignal()

    def __init__(self, image_path: str, parent=None, showAnalysisPannel: bool = False):
        super().__init__(parent)
        self.setWindowFlag(Qt.Window)
        self.ui = ui.Ui_ImageViewer()
        self.ui.setupUi(self)
        self.showAnalysisPannel = showAnalysisPannel

        # Setup Scene
        self.scene = QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.scene)
        
        # Load Image
        self.image_item = None
        # remember the initial chosen width by the system
        self.initialWidth = self.width() 
        self.loadNewImage(image_path)
        
        # UI State
        self.ui.analysisFrame.setHidden(not showAnalysisPannel)

        # Connections
        self.ui.NextImagePushButton.released.connect(self.goNext.emit)
        self.ui.StopPushButton.released.connect(self.stopShow.emit)

    def loadNewImage(self, image_path: str):
        # Load Image
        self.pixmap = QPixmap(image_path)
        if not self.pixmap.isNull():

            target_width = self.initialWidth 
            ratio = self.pixmap.height() / self.pixmap.width()
            target_height = int(target_width * ratio)

            if self.showAnalysisPannel:
                target_width += self.ui.analysisFrame.width()

            self.resize(target_width, target_height)

            if (self.image_item):
                self.scene.removeItem(self.image_item)

            self.image_item = self.scene.addPixmap(self.pixmap)
            self.scene.setSceneRect(QRectF(self.pixmap.rect()))
            
            # Initial fit (use a small delay or call after show() for best results)
            self.ui.graphicsView.fitInView(self.image_item, Qt.KeepAspectRatio)
        return 

    def showEvent(self, event):
        if (self.image_item):
            # This ensures the fitInView works once the geometry is calculated
            self.ui.graphicsView.fitInView(self.image_item, Qt.KeepAspectRatio)
            super().showEvent(event)

    def resizeEvent(self, event):
        if (self.image_item):
            super().resizeEvent(event)
            self.ui.graphicsView.fitInView(self.image_item, Qt.KeepAspectRatio)