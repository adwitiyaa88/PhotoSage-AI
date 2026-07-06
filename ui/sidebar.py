from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
)


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(180)

        layout = QVBoxLayout()

        buttons = [
            "🏠 Dashboard",
            "📁 Albums",
            "📷 Duplicates",
            "🌫️ Blurry",
            "🎥 Videos",
            "🗑️ Trash",
            "⚙️ Settings",
        ]

        for text in buttons:
            button = QPushButton(text)
            button.setMinimumHeight(40)
            layout.addWidget(button)

        layout.addStretch()

        self.setLayout(layout)