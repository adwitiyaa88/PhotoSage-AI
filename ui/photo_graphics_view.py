from PySide6.QtWidgets import QGraphicsView
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtCore import QEvent

class PhotoGraphicsView(QGraphicsView):

    def __init__(self, scene):
        super().__init__(scene)

        self.min_scale = 0.2
        self.max_scale = 5.0

        self.setTransformationAnchor(
            QGraphicsView.AnchorUnderMouse
        )

        self.setResizeAnchor(
            QGraphicsView.AnchorViewCenter
        )
        self.setAlignment(
            Qt.AlignCenter
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
        self.viewport().installEventFilter(self)

    def mouseDoubleClickEvent(self, event):
        self.parent().fit_image()
        super().mouseDoubleClickEvent(event)

    def eventFilter(self, obj, event):
        if obj == self.viewport() and event.type() == QEvent.Wheel:
            print(
                "Angle:", event.angleDelta(),
                "Pixel:", event.pixelDelta()
            )

            delta = event.angleDelta().y()

            if delta == 0:
                return True

            factor = 1 + (delta / 1200.0)

            current_scale = self.transform().m11()
            new_scale = current_scale * factor

            if self.min_scale <= new_scale <= self.max_scale:
                self.scale(factor, factor)

            event.accept()
            return True

        return super().eventFilter(obj, event)