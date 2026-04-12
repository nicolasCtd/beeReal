from ui import ImageViewer_ui as ui
from PyQt5.QtWidgets import QWidget, QGraphicsScene
from PyQt5.QtCore import Qt, pyqtSignal

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
        self.ui.analysisFrame.setHidden(not self.showAnalysisPannel)

        # Connections
        self.ui.NextImagePushButton.released.connect(self.goNext.emit)
        self.ui.StopPushButton.released.connect(self.stopShow.emit)

    def loadNewImage(self, image_path: str):
        # Load Image
        imageSize = self.ui.graphicsView.loadImage(image_path) 
        
        if not imageSize.isNull():
            target_width = self.initialWidth 
            ratio = imageSize.height() / imageSize.width()
            target_height = int(target_width * ratio)

            if self.showAnalysisPannel:
                target_width += self.ui.analysisFrame.width()

            self.resize(target_width, target_height)

        return