from PyQt5.QtWidgets import QGraphicsView, QGraphicsItem, QGraphicsTextItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor

# Some local constants constants
zoomFactor = 1.25
maxZoomLevel = 10

addPointModifier = Qt.ControlModifier


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


    def mouseReleaseEvent(self, event):

        if event.modifiers() == addPointModifier:
            posImage = self.mapToScene(event.pos())
            item = QGraphicsTextItem("+")                 
            serifFont = QFont("Times", 20, QFont.Bold)  
            item.setDefaultTextColor(QColor(0, 255, 0))
            brect = item.boundingRect()
            print(brect)
            item.setPos(posImage.x()-brect.width(),posImage.y()-brect.height() ) 
            item.setFont(serifFont)
            item.setFlag(QGraphicsItem.ItemIgnoresTransformations)
            self.scene().addItem(item)
            print(posImage)

        
        return super().mouseReleaseEvent(event)
