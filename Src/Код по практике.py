from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    QFileDialog, QLineEdit, QHBoxLayout, QRadioButton, QButtonGroup
)
from PIL import Image
import sys

class ImageEditorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Редактор изображений')
        self.layout = QVBoxLayout()
        self.label = QLabel('Файл не выбран')
        self.layout.addWidget(self.label)
        self.button = QPushButton('Выбрать изображение')
        self.button.clicked.connect(self.select_file)
        self.layout.addWidget(self.button)
        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel('Новая ширина:'))
        self.width_input = QLineEdit()
        size_layout.addWidget(self.width_input)
        size_layout.addWidget(QLabel('Новая высота:'))
        self.hight_input = QLineEdit()  
        size_layout.addWidget(self.hight_input)
        self.layout.addLayout(size_layout)
        rotate_layout = QHBoxLayout()
        rotate_layout.addWidget(QLabel('Поворот (градусы):'))
        self.rotate_input = QLineEdit()
        rotate_layout.addWidget(self.rotate_input)
        self.layout.addLayout(rotate_layout)
        self.radio_png = QRadioButton('PNG')
        self.radio_jpg = QRadioButton('JPG')
        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.radio_png)
        self.radio_group.addButton(self.radio_jpg)
        self.layout.addWidget(self.radio_png)
        self.layout.addWidget(self.radio_jpg)
        self.convert_btn = QPushButton('Конвертировать')
        self.convert_btn.clicked.connect(self.convert_image)
        self.layout.addWidget(self.convert_btn)
        self.result_label = QLabel('')
        self.layout.addWidget(self.result_label)
        self.setLayout(self.layout)
        self.filepath = None  
    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Выберите изображение', '', "Images (*.png *.jpg)")
        if file_path:
            self.filepath = file_path  
            self.label.setText('Выбран файл: ' + file_path)
    def convert_image(self):
        if not self.filepath:  
            self.result_label.setText('Выберите файл сначала!')
            return
        if not (self.radio_png.isChecked() or self.radio_jpg.isChecked()):
            self.result_label.setText('Выберите формат!')
            return
        try:
            width = int(self.width_input.text())
            height = int(self.hight_input.text())  
            angle = float(self.rotate_input.text())
        except ValueError:
            self.result_label.setText('Введите корректные размеры и угол!')
            return
        target_format = 'PNG' if self.radio_png.isChecked() else 'JPG'
        output_path = self.convert_image_file(self.filepath, target_format, width, height, angle)
        self.result_label.setText(f'Конвертация завершена: {output_path}')
    def convert_image_file(self, input_path, target_format, width, height, angle):
        img = Image.open(input_path)
        img = img.rotate(angle, expand=True)
        img = img.resize((width, height))
        if target_format == 'JPG':
            output_path = input_path.rsplit('.', 1)[0] + '.jpg'
            rgb_img = img.convert('RGB')  
            rgb_img.save(output_path, quality=95)
        else:
            output_path = input_path.rsplit('.', 1)[0] + '.png'
            img.save(output_path)
        return output_path
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageEditorUI()
    window.show()
    sys.exit(app.exec())

