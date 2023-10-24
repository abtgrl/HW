import os
from PIL import Image, ImageFilter, ImageOps
import threading
import tkinter as tk
from tkinter import filedialog


def edit_images(image_path, status, filters, saved):
    try:
        img = Image.open(image_path)
        filters_name = ''
        for filter in filters:
            img = filter(img)
            filters_name += '_' + filter.__name__

        _, file = os.path.split(image_path)
        file, extension = file.split('.')
        save_path = os.path.join(saved, f"{file}{filters_name}.{extension}")
        img.save(save_path)
    except:
        status.config(text='Ошибка', foreground='red')


def resize(img):
    width, height = img.size
    resized = (width // 2, height // 2)
    return img.resize(resized, Image.LANCZOS)


def sharp(img):
    return img.filter(ImageFilter.SHARPEN)


def sepia(img):
    return ImageOps.colorize(img.convert("L"), "#704238", "#C0B283")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.open_dir = None
        self.save_dir = None

        def open_images():
            self.open_dir = tk.filedialog.askdirectory()

        def save_images():
            self.save_dir = tk.filedialog.askdirectory()

        def process():
            if not self.open_dir:
                status.config(text='Исходная папка не выбрана', foreground='red')
            elif not self.save_dir:
                status.config(text='Папка для сохранения не выбрана', foreground='red')
            else:
                try:
                    image_paths = [os.path.join(self.open_dir, filename) for filename in os.listdir(self.open_dir)
                                   if filename.endswith(('.jpg', '.jpeg', '.png'))]

                    filters = []
                    if is_resize.get():
                        filters.append(resize)
                    if is_sharp.get():
                        filters.append(sharp)
                    if is_sepia.get():
                        filters.append(sepia)

                    threads = []
                    for image in image_paths:
                        thread = threading.Thread(target=edit_images, args=(image, status, filters, self.save_dir))
                        threads.append(thread)
                        thread.start()

                    for thread in threads:
                        thread.join()

                    status.config(text='Готово!', foreground='green')
                except:
                    status.config(text='Ошибка', foreground='red')

        self.title('Обработка изображений')
        self.geometry("480x220")
        self.resizable(False, False)

        file_frame = tk.Frame(self, pady=10, padx=10)
        file_frame.grid(row=0, column=0)

        tk.Label(file_frame, text='Выберите папку с исходными изображениями').grid(row=0, column=0)
        tk.Button(file_frame, text='Выбрать папку', command=open_images).grid(row=1, column=0)
        file_frame.rowconfigure(1, minsize=30)

        tk.Label(file_frame, text='''Выберите папку для сохранения
         обработанных изображений''').grid(row=2, column=0, sticky='s')
        tk.Button(file_frame, text='Выбрать папку', command=save_images).grid(row=3, column=0)
        file_frame.rowconfigure(2, minsize=40)
        file_frame.rowconfigure(3, minsize=30)

        filters_frame = tk.Frame(self, padx=30)
        filters_frame.grid(row=0, column=1)

        tk.Label(filters_frame, text='Выберите фильтры').grid(row=0, column=0)
        is_resize = tk.BooleanVar()
        is_sharp = tk.BooleanVar()
        is_sepia = tk.BooleanVar()
        resize_button = tk.Checkbutton(filters_frame, text='Уменьшение размера', variable=is_resize)
        resize_button.grid(row=1, column=0, sticky='w')
        sharp_button = tk.Checkbutton(filters_frame, text='Увеличение резкости', variable=is_sharp)
        sharp_button.grid(row=2, column=0, sticky='w')
        sepia_button = tk.Checkbutton(filters_frame, text='Сепия', variable=is_sepia)
        sepia_button.grid(row=3, column=0, sticky='w')

        tk.Button(self, text='Обработать', command=process).grid(row=2, column=0, columnspan=2)
        status = tk.Label(self, text='')
        status.grid(row=3, column=0, columnspan=2)
        self.rowconfigure(3, minsize=45)


if __name__ == "__main__":
    app = App()
    app.mainloop()
