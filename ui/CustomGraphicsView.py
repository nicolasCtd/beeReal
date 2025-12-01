from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import Qt

# Some local constants constants
zoomFactor = 1.25
maxZoomLevel = 10

class CustomGraphicsView(QGraphicsView):
    def __init__(self, parent=None) :
        super().__init__(parent)

        # No anchor to avoid default repositionning to override user move
        self.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.setResizeAnchor(QGraphicsView.NoAnchor)

        # Activate scrollbars actives
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.zoomLevel = 0
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)    
        


    def wheelEvent(self, event):
        # TODO: limit zoom level

        if self.zoomLevel > maxZoomLevel or self.zoomLevel < 0 :
            event.accept()
            return

        old_pos = self.mapToScene(event.pos())

        factor = 1.

        if event.angleDelta().y() > 0:
            # ZOOM
            if self.zoomLevel < maxZoomLevel:                
                factor = zoomFactor
                self.zoomLevel+=1            
        else:
            # UNZOOM
            if self.zoomLevel > 0:                
                factor = 1. / zoomFactor
                self.zoomLevel-=1




        self.scale(factor, factor)

        new_pos = self.mapToScene(event.pos())
        delta = new_pos - old_pos

        # Compensation X + Y
        self.translate(delta.x(), delta.y())

        event.accept()

