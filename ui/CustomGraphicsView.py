from PyQt5.QtWidgets import QGraphicsView, QGraphicsItem, QGraphicsTextItem, QGraphicsPixmapItem
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPixmap

# Some local constants constants
zoomFactor = 1.25
maxZoomLevel = 10
targetItemMidSize = 32 #pixels

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

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._panning = True
            self._last_mouse_pos = event.pos()
            event.accept()
        else:
            super().mousePressEvent(event)


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


    def mouseMoveEvent(self, event):
        if self._panning:
            old_scene_pos = self.mapToScene(self._last_mouse_pos)
            new_scene_pos = self.mapToScene(event.pos())
            delta = new_scene_pos - old_scene_pos
            self.translate(delta.x(), delta.y())
            self._last_mouse_pos = event.pos()
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            self._panning = False

        if event.modifiers() == addPointModifier:
            posImage = self.mapToScene(event.pos())                      
            plusImage = QPixmap(":images/plus.png").scaled(2*targetItemMidSize, 2*targetItemMidSize)
            item = QGraphicsPixmapItem(plusImage)
            item.setOffset(-targetItemMidSize, -targetItemMidSize)
            item.setPos(posImage.x(),posImage.y()) 
            item.setFlag(QGraphicsItem.ItemIgnoresTransformations)
            self.scene().addItem(item)
        
        return super().mouseReleaseEvent(event)
