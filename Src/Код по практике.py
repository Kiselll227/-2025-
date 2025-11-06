from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    QFileDialog, QLineEdit, QHBoxLayout
)
from PIL import Image
import sys
class ImageEditorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Редактор изображений')
        self.layot = QVBoxLayout()
        self.labal = QLabel('Файл не выбран')
        self.layot.addWidget(self.labal)
        self.button = QPushButton('Выбрать изображение')
        self.button.clicked.connect(self.select_file)
        self.layot.addWidget(self.button)
        self.setLayout(self.layot)
        self.file_path = None
    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Выберите изображение', '', "Images (*.png *.jpg)")
        if file_path:
            self.file_path = file_path
            self.labal.setText('Выбран файл: ' + file_path)
        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel('Новая ширина:'))
        self.width_inpt = QLineEdit()
        size_layout.addWidget(self.width_inpt)
        size_layout.addWidget(QLabel('Новая высота:'))
        self.height_inpt = QLineEdit()
        size_layout.addWidget(self.height_inpt)
        self.layot.addLayout(size_layout)

        rotate_layout = QHBoxLayout()
        rotate_layout.addWidget(QLabel('Поворот (градусы):'))
        self.rotate_inpt = QLineEdit()
        rotate_layout.addWidget(self.rotate_inpt)
        self.layot.addLayout(rotate_layout)
