from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class PhotoViewer(QWidget):
    def __init__(self, image_path):
        super().__init__()

        from pathlib import Path

        filename = Path(image_path).name
        self.setWindowTitle(filename)
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

        self.image_path = image_path
        self.pixmap = QPixmap(image_path)

        self.update_image()

        layout.addWidget(self.image)

        self.setLayout(layout)
    def update_image(self):
        if self.pixmap.isNull():
            return

        scaled = self.pixmap.scaled(
            self.image.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation,
        )

        self.image.setPixmap(scaled)

    def resizeEvent(self, event):
        self.update_image()
        super().resizeEvent(event)