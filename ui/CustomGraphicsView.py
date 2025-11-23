from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import Qt


class CustomGraphicsView(QGraphicsView):
    def __init__(self, parent=None) :
        super().__init__(parent)

        # No anchor to avoid default repositionning to override user move
        self.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.setResizeAnchor(QGraphicsView.NoAnchor)

        # Activate scrollbars actives
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.zoom_factor = 1.25

    def wheelEvent(self, event):
        # TODO: limit zoom level

        old_pos = self.mapToScene(event.pos())

        if event.angleDelta().y() > 0:
            factor = self.zoom_factor
        else:
            factor = 1 / self.zoom_factor

        self.scale(factor, factor)

        new_pos = self.mapToScene(event.pos())
        delta = new_pos - old_pos

        # Compensation X + Y
        self.translate(delta.x(), delta.y())

        event.accept()

