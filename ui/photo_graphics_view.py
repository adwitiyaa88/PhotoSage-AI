from PySide6.QtWidgets import QGraphicsView
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter

class PhotoGraphicsView(QGraphicsView):

    def __init__(self, scene):
        super().__init__(scene)

        self.zoom = 0

        self.setTransformationAnchor(
            QGraphicsView.AnchorUnderMouse
        )

        self.setResizeAnchor(
            QGraphicsView.AnchorViewCenter
        )

        self.setDragMode(
            QGraphicsView.ScrollHandDrag
        )

        self.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

        self.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )
        # enable antialiasing and smooth pixmap transform for better rendering
        self.setRenderHints(
            QPainter.Antialiasing |
            QPainter.SmoothPixmapTransform
        )
    def wheelEvent(self, event):

        if event.angleDelta().y() > 0:
            factor = 1.25
            self.zoom += 1
        else:
            factor = 0.8
            self.zoom -= 1

        if -10 <= self.zoom <= 20:
            self.scale(factor, factor)

        elif self.zoom < -10:
            self.zoom = -10

        else:
            self.zoom = 20

    def mouseDoubleClickEvent(self, event):
        self.parent().fit_image()