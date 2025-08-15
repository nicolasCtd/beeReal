import os
import pathlib

here = os.path.dirname(pathlib.Path(__file__))
space = "    "
enter = "\n"

file = open(f"{here}{os.sep}buttons_browse.py", "w")

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
    file.write(f"def browseFile{fn}(TABs):" + enter)
    file.write(space + "options = QFileDialog.Options()" + enter)
    file.write(space + "options |= QFileDialog.DontUseNativeDialog" + enter)
    file.write(space + f"TABs.fileName{fn}, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)" + enter)
    file.write(space + f"buttons.save_image(TABs.fileName{fn}, TABs.in_, {fn})" + enter)
    file.write(space + f"if TABs.fileName{fn} != '':" + enter)
    file.write(space + space + f"pixmap = QPixmap(TABs.in_ + os.sep + '{fn}_in.jpg')" + enter)
    file.write(space + space + f"pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)" + enter)
    file.write(space + space + f"TABs.label_left[{fn-1}].setPixmap(pixmap)" + enter)
    file.write(space + space + f"globals.loaded[{fn}] = 1" + enter)
    file.write(space + "else:" + enter)
    file.write(space + space + "pass" + enter)
    file.write(enter)

# file.write("def save_image(nameFile, destination, num):" + enter)
# file.write(space + "img = Image.open(nameFile)" + enter)
# file.write(space + "img.save(destination + os.sep + f'{num}_in.jpg')" + enter)
# file.write(space + "logging.info(f'Image {num} : ' + destination + os.sep + f'{num}_in.jpg')")