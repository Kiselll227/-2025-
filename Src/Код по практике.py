import tkinter as tk
from tkinter import filedialog
class ImageConverterUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Программа для выбора файла')
        self.label = tk.Label(self.root, text='Файл не выбран')
        self.label.pack()
        self.button = tk.Button(self.root, text='Выбрать файл', command=self.select_file)
        self.button.pack()
        self.file_path = None
    def select_file(self):
        self.file_path = filedialog.askopenfilename(
            title='Выберите файл',
            filetypes=(('Изображения', '*.png *.jpg *.bmp'), ('Все файлы', '*.*')))
        if self.file_path:
            self.label.config(text=f"Выбран файл: {self.file_path}")
if __name__ == '__main__':
    app = ImageConverterUI()
    app.root.mainloop()



