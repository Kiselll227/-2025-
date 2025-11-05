from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
import sys
class ImageConverterUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Программа для выбора файла')
        self.layout = QVBoxLayout()
        self.label = QLabel('Файл не выбран')
        self.button = QPushButton('Выбрать файл')
        self.button.clicked.connect(self.select_file)
        self.layout.addWidget(self.button)
        self.file_path = None
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageConverterUI()
    window.show()
    sys.exit(app.exec())



