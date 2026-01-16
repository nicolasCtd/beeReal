# Ce script permet de générer buttons_edit.py

import os
import pathlib

here = os.path.dirname(pathlib.Path(__file__))
space = "    "
enter = "\n"

file = open(f"{here}{os.sep}buttons_load.py", "w", encoding='utf-8')

file.write("from PyQt5.QtWidgets import QFileDialog" + enter)
file.write("from PyQt5.QtGui import QPixmap" + enter)
file.write("from PyQt5.QtCore import Qt" + enter)
file.write("import os" + enter)
file.write("import logging" + enter)
file.write("from PIL import Image" + enter)
file.write("from modules import globals" + enter)
file.write("from modules import buttons" + enter)
file.write (enter)

for fn in range(1, 101, 1):  # function number
    file.write(f"def load{fn}(all_tabs):" + enter)
    file.write(space + f"\"\"\"Charge l'image numero {fn} dans l'interface.\"\"\"" + enter)
    file.write(space + "options = QFileDialog.Options()" + enter)
    file.write(space + "options |= QFileDialog.DontUseNativeDialog" + enter)
    file.write(space + f"all_tabs.fileName{fn}, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)" + enter)
    file.write(space + f"if all_tabs.fileName{fn} != '':" + enter)
    file.write(space + space + f"buttons.save_image(all_tabs.fileName{fn}, all_tabs.in_, {fn})" + enter)
    file.write(space + space + f"pixmap = QPixmap(all_tabs.in_ + os.sep + '{fn}_in.jpg')" + enter)
    file.write(space + space + f"pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)" + enter)
    file.write(space + space + f"all_tabs.label_left[{fn-1}].setPixmap(pixmap)" + enter)
    file.write(space + space + f"globals.loaded[{fn}] = 1" + enter)
    file.write(space + "else:" + enter)
    file.write(space + space + "pass" + enter)
    file.write(enter)

# file.write("def save_image(nameFile, destination, num):" + enter)
# file.write(space + "img = Image.open(nameFile)" + enter)
# file.write(space + "img.save(destination + os.sep + f'{num}_in.jpg')" + enter)
# file.write(space + "logging.info(f'Image {num} : ' + destination + os.sep + f'{num}_in.jpg')")