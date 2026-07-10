from pathlib import Path
from ui.photo_graphics_view import PhotoGraphicsView

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGraphicsScene,
    QGraphicsPixmapItem,
)

class PhotoViewer(QWidget):
    def __init__(self, photos, current_index):
        super().__init__()

        
        self.resize(1200, 800)
        self.setStyleSheet("""
QWidget {
    background-color: #1b1b1b;
}

""")
        layout = QVBoxLayout()

        self.scene = QGraphicsScene()

        self.view = PhotoGraphicsView(self.scene)
        
        self.photo_item = QGraphicsPixmapItem()

        self.scene.addItem(self.photo_item)

        layout.addWidget(self.view)

        self.photos = photos
        self.current_index = current_index

        self.load_photo()
        

        self.setLayout(layout)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setFocus()

    def load_photo(self):
        image_path = self.photos[self.current_index]
        self.setWindowTitle(Path(image_path).name)
        self.pixmap = QPixmap(str(image_path))
        self.update_image()

    def update_image(self):
        if self.pixmap.isNull():
            return

        self.photo_item.setPixmap(self.pixmap)

        # adjust view to fit the new image
        self.fit_image()

    def resizeEvent(self, event):
        self.update_image()
        super().resizeEvent(event)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Right:
            if self.current_index < len(self.photos) - 1:
                self.current_index += 1
                self.load_photo()
        elif key == Qt.Key_Left:
            if self.current_index > 0:
                self.current_index -= 1
                self.load_photo()
        elif key == Qt.Key_Escape:
            self.close()
        else:
            super().keyPressEvent(event)

    def fit_image(self):
        self.view.resetTransform()
        self.view.zoom = 0

        self.view.fitInView(
            self.photo_item,
            Qt.KeepAspectRatio,
        )