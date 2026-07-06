from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class PhotoViewer(QWidget):
    def __init__(self, image_path):
        super().__init__()

        self.setWindowTitle("Photo Viewer")
        self.resize(900, 700)

        layout = QVBoxLayout()

        self.image = QLabel()
        self.image.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap(image_path)

        if not pixmap.isNull():
            pixmap = pixmap.scaled(
                850,
                650,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )

        self.image.setPixmap(pixmap)

        layout.addWidget(self.image)

        self.setLayout(layout)