from ui.photo_viewer import PhotoViewer
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
    QScrollArea,
    QGridLayout,
)

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from services.google_auth import authenticate
from services.local_photo_service import scan_folder
from services.apple_photos import find_library, get_original_photos


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.viewers = []
        layout = QVBoxLayout()

        title = QLabel("📷 Welcome to PhotoSage AI")
        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        subtitle = QLabel(
            "Clean and organize your Google Photos safely."
        )

        self.connect_button = QPushButton("Connect Google Photos")
        self.connect_button.setFixedHeight(45)
        self.connect_button.clicked.connect(self.connect_google)

        self.open_folder_button = QPushButton("📂 Open Folder")
        self.open_folder_button.setFixedHeight(45)
        self.open_folder_button.clicked.connect(self.open_folder)

        self.apple_button = QPushButton("🍎 Apple Photos Library")
        self.apple_button.setFixedHeight(45)
        self.apple_button.clicked.connect(self.connect_apple_photos)

        self.photo_count = QLabel("")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(25)
        layout.addWidget(self.connect_button)
        layout.addWidget(self.open_folder_button)
        layout.addWidget(self.apple_button)
        layout.addWidget(self.photo_count)

        self.scroll = QScrollArea()
        self.gallery = QWidget()
        self.grid = QGridLayout()

        self.gallery.setLayout(self.grid)
        self.scroll.setWidget(self.gallery)
        self.scroll.setWidgetResizable(True)

        layout.addWidget(self.scroll)
        layout.addStretch()

        self.setLayout(layout)

    def connect_google(self):
        creds = authenticate()

        if creds:
            print("Google Photos connected successfully!")
            self.connect_button.setText("✅ Connected")
            self.connect_button.setEnabled(False)

    def open_folder(self):
        folder = QFileDialog.getExistingDirectory(
        self,
        "Select Photo Folder"
    )

        if folder:
            print(f"\nSelected folder: {folder}")

            photos = scan_folder(folder)

            print(f"Found {len(photos)} photos.\n")

            for photo in photos[:10]:
                print(photo.name)
    
    def open_photo(self, image_path):
        viewer = PhotoViewer(image_path)
        viewer.show()
        self.viewers.append(viewer)

    def connect_apple_photos(self):
        library = find_library()

        if not library:
            print("Apple Photos Library not found.")
            return

        photos = get_original_photos()

        print(f"Found {len(photos)} photos.")

        self.apple_button.setText("✅ Apple Photos Found")
        self.apple_button.setEnabled(False)

        self.photo_count.setText(f"📸 {len(photos)} photos found")

        # Show first 20 thumbnails
        row = 0
        col = 0

        for photo in photos[:20]:
            button = QPushButton()
            button.setFixedSize(150, 150)

            pixmap = QPixmap(str(photo))
            print(photo)
            print("Loaded:", not pixmap.isNull())

            if not pixmap.isNull():
                pixmap = pixmap.scaled(
                    150,
                    150,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation,
                )

                button.setIcon(pixmap)
                button.setIconSize(pixmap.size())

            button.clicked.connect(
                lambda _checked=False, path=str(photo): self.open_photo(path)
            )

            self.grid.addWidget(button, row, col)
            print(f"Added thumbnail at Row={row}, Col={col}")
            col += 1

            if col == 4:
                col = 0
                row += 1