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