from ui import ImageViewer_ui as ui
from PyQt5.QtWidgets import QWidget, QGraphicsScene
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QRectF

class ImageViewer(QWidget):
    def __init__(self, image_path: str, parent=None, showAnalysisPannel: bool = False):
        super().__init__(parent)
        self.setWindowFlag(Qt.Window)
        self.ui = ui.Ui_ImageViewer()
        self.ui.setupUi(self)
        
        initial_size =print(self.size())

        # Setup Scene
        self.scene = QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.scene)
        
        # Load Image
        self.pixmap = QPixmap(image_path)
        if not self.pixmap.isNull():

            target_width = self.width() 
            ratio = self.pixmap.height() / self.pixmap.width()
            target_height = int(target_width * ratio)

            if showAnalysisPannel:
                target_width += self.ui.analysisFrame.width()

            self.resize(target_width, target_height)


            self.image_item = self.scene.addPixmap(self.pixmap)
            self.scene.setSceneRect(QRectF(self.pixmap.rect()))
            
            # Initial fit (use a small delay or call after show() for best results)
            self.ui.graphicsView.fitInView(self.image_item, Qt.KeepAspectRatio)
        
        # UI State
        self.ui.analysisFrame.setHidden(not showAnalysisPannel)

    def showEvent(self, event):
        if (self.image_item):
            # This ensures the fitInView works once the geometry is calculated
            self.ui.graphicsView.fitInView(self.image_item, Qt.KeepAspectRatio)
            super().showEvent(event)

    def resizeEvent(self, event):
        if (self.image_item):
            super().resizeEvent(event)
            self.ui.graphicsView.fitInView(self.image_item, Qt.KeepAspectRatio)