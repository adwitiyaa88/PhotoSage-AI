from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
)

from ui.sidebar import Sidebar

from ui.dashboard import Dashboard


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PhotoSage AI")
        self.resize(1000, 650)

        layout = QHBoxLayout()

        self.sidebar = Sidebar()
        self.dashboard = Dashboard()

        layout.addWidget(self.sidebar)
        layout.addWidget(self.dashboard)

        self.setLayout(layout)