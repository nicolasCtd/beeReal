from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel
from core import common
import os
from PyQt5.QtCore import Qt
import numpy as np
from PIL import Image
import logging
from modules import globals

def turnToGrayImages(TABs, num):
    a = TABs.label_left[num-1].grab()                       # get QPixmap
    b = a.toImage()                                         # convert to QImage
    b = b.convertToFormat(QImage.Format_Grayscale8)         # turn to gray
    c = QPixmap.fromImage(b)                                # go back to QPixmap
    TABs.label_left[num-1].setPixmap(c)

    a = TABs.label_right[num-1].grab()
    b = a.toImage()
    b = b.convertToFormat(QImage.Format_Grayscale8)
    c = QPixmap.fromImage(b)
    TABs.label_right[num-1].setPixmap(c)

    num_grid = (num-1) // 5
    darda = globals.media + "dardagnan2_bw.png"
    pixmap = QPixmap(darda)
    label1 = QLabel()
    label2 = QLabel()
    label1.setPixmap(pixmap)
    label2.setPixmap(pixmap)
    TABs.grids[num_grid].addWidget(label1, np.mod(num-1, 5), 1)
    TABs.grids[num_grid].addWidget(label2, np.mod(num-1, 5), 8)

    # change color of button (from green to red)
    btn_onoff = TABs.grids[num_grid].itemAtPosition(np.mod(num-1, 5), 0).widget()
    btn_onoff.setStyleSheet("background-color: darksalmon")

    # disable buttons
    btn_load = TABs.grids[num_grid].itemAtPosition(np.mod(num-1, 5), 2).widget()
    btn_load.setEnabled(False)
    btn_edit = TABs.grids[num_grid].itemAtPosition(np.mod(num-1, 5), 4).widget()
    btn_edit.setEnabled(False)
    btn_visu = TABs.grids[num_grid].itemAtPosition(np.mod(num-1, 5), 6).widget()
    btn_visu.setEnabled(False)

    # change color of the text (black -> grey)
    TXT = TABs.grids[num_grid].itemAtPosition(np.mod(num-1, 5), 7).widget()
    TXT.setStyleSheet("color: grey; font-size: 22px")
    TXT.setText(TXT.text())

    return 0

def turnToRGBImages(TABs, num):

    # reset image on the left
    if os.path.exists(os.sep.join([TABs.out, f"{num}_out.jpg"])):
        img_in =os.sep.join([TABs.in_, f"{num}_in.jpg"])
    else:
        img_in = os.sep.join([TABs.path, "media", f"im{num}.png"])
    pixmap_in = QPixmap(img_in)
    pixmap_in = pixmap_in.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
    TABs.label_left[num-1].setPixmap(pixmap_in)

    # reset image on the right
    if os.path.exists(os.sep.join([TABs.out, f"{num}_out.jpg"])):
        img_out = os.sep.join([TABs.out, f"{num}_out.jpg"])
    else:
        img_out = os.sep.join([TABs.path, "media", f"im{num}.png"])
    pixmap_out = QPixmap(img_out)
    pixmap_out = pixmap_out.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
    TABs.label_right[num-1].setPixmap(pixmap_out)

    # reset Dardagnan in full colors
    num_grid = (num - 1) // 5
    darda = os.sep.join([TABs.path, "media", "dardagnan2.png"])
    pixmap = QPixmap(darda)
    label1 = QLabel()
    label2 = QLabel()
    label1.setPixmap(pixmap)
    label2.setPixmap(pixmap)
    TABs.grids[num_grid].addWidget(label1, np.mod(num-1, 5), 1)
    TABs.grids[num_grid].addWidget(label2, np.mod(num-1, 5), 8)

    # change color of button (from red to green)
    btn_onoff = TABs.grids[num_grid].itemAtPosition(np.mod(num-1, 5), 0).widget()
    btn_onoff.setStyleSheet("background-color: aquamarine")

    # enable buttons
    btn_load = TABs.grids[num_grid].itemAtPosition(np.mod(num-1, 5), 2).widget()
    btn_load.setEnabled(True)
    btn_edit = TABs.grids[num_grid].itemAtPosition(np.mod(num-1, 5), 4).widget()
    btn_edit.setEnabled(True)
    btn_visu = TABs.grids[num_grid].itemAtPosition(np.mod(num-1, 5), 6).widget()
    btn_visu.setEnabled(True)

    # change color of the text (grey -> black)
    TXT = TABs.grids[num_grid].itemAtPosition(np.mod(num-1, 5), 7).widget()
    TXT.setStyleSheet("color: black; font-size: 22px")
    TXT.setText(TXT.text())

    return 0

def save_image(nameFile, destination, num):
    print(f'Image {num} : ' + destination + os.sep + f'{num}_in.jpg')
    img = Image.open(nameFile)
    img.save(destination + os.sep + f'{num}_in.jpg')
    logging.info(f'Image {num} : ' + destination + os.sep + f'{num}_in.jpg')