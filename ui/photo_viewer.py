from pathlib import Path
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class PhotoViewer(QWidget):
    def __init__(self, photos, current_index):
        super().__init__()

        
        self.resize(1200, 800)
        self.setStyleSheet("""
QWidget {
    background-color: #1b1b1b;
}

QLabel {
    background-color: #1b1b1b;
}
""")
        layout = QVBoxLayout()

        self.image = QLabel()
        self.image.setAlignment(Qt.AlignCenter)

        self.photos = photos
        self.current_index = current_index

        self.zoom_factor = 1.0
        self.fit_to_window = True
        self.load_photo()
        


        layout.addWidget(self.image)

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

        if self.fit_to_window:
            scaled = self.pixmap.scaled(
                self.image.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
        else:
            width = int(self.pixmap.width() * self.zoom_factor)
            height = int(self.pixmap.height() * self.zoom_factor)

            scaled = self.pixmap.scaled(
                width,
                height,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )

        self.image.setPixmap(scaled)

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

    def wheelEvent(self, event):
        print(event.angleDelta().y())
        if event.angleDelta().y() > 0:
            self.zoom_factor *= 1.15
        else:
            self.zoom_factor /= 1.15

        # Limit zoom between 20% and 500%
        self.zoom_factor = max(0.2, min(self.zoom_factor, 5.0))

        self.fit_to_window = False
        self.update_image()