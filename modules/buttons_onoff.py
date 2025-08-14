from modules import globals
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel
from core import common
import os
from PyQt5.QtCore import Qt

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

    num_grid = num // 5
    darda = common.resource_path(f"media{os.sep}dardagnan2_bw.png")
    pixmap = QPixmap(darda)
    label1 = QLabel()
    label2 = QLabel()
    label1.setPixmap(pixmap)
    label2.setPixmap(pixmap)
    TABs.grids[num_grid].addWidget(label1, num-1, 1)
    TABs.grids[num_grid].addWidget(label2, num-1, 8)

    # change color of button (from green to red)
    btn_onoff = TABs.grids[num_grid].itemAtPosition(num-1, 0).widget()
    btn_onoff.setStyleSheet("background-color: darksalmon")
    return 0

def turnToRGBImages(TABs, num):

    # reset image on the left
    img_in =os.sep.join([TABs.in_, f"{num}_in.jpg"])
    pixmap_in = QPixmap(img_in)
    pixmap_in = pixmap_in.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
    TABs.label_left[num-1].setPixmap(pixmap_in)

    # reset image on the right
    img_out = os.sep.join([TABs.out, f"{num}_out.jpg"])
    pixmap_out = QPixmap(img_out)
    pixmap_out = pixmap_out.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
    TABs.label_right[num-1].setPixmap(pixmap_out)

    # reset Dardagnan in full colors
    num_grid = num // 5
    darda = os.sep.join([TABs.path, "media", "dardagnan2.png"])
    pixmap = QPixmap(darda)
    label1 = QLabel()
    label2 = QLabel()
    label1.setPixmap(pixmap)
    label2.setPixmap(pixmap)
    TABs.grids[num_grid].addWidget(label1, num-1, 1)
    TABs.grids[num_grid].addWidget(label2, num-1, 8)

    # change color of button (from red to green)
    btn_onoff = TABs.grids[num_grid].itemAtPosition(num-1, 0).widget()
    btn_onoff.setStyleSheet("background-color: aquamarine")

    return 0

def onoff1(TABs):

    print("activate/deactivate image 1")
    
    num_line = np.mod(1, 5)

    if globals.enabled[1]:
        print("image 1 is enabled. Now it will be disabled")
        globals.enabled[1] = 0

        turnToGrayImages(TABs, 1)

    else:
        print("image 1 is disabled. Now it will be enabled")
        globals.enabled[1] = 1
        turnToRGBImages(TABs, 1)

    return 0
def onoff2(TAB):
    print("activate/deactivate image 2")
    return 0
def onoff3(TAB):
    print("activate/deactivate image 3")
    return 0
def onoff4(TAB):
    print("activate/deactivate image 4")
    return 0
def onoff5(TAB):
    print("activate/deactivate image 5")
    return 0
def onoff5(TAB):
    print("activate/deactivate image 5")
    return 0
def onoff6(TAB):
    return 0
def onoff7(TAB):
    return 0
def onoff8(TAB):
    return 0
def onoff9(TAB):
    return 0
def onoff10(TAB):
    return 0
def onoff11(TAB):
    return 0
def onoff12(TAB):
    return 0
def onoff13(TAB):
    return 0
def onoff14(TAB):
    return 0
def onoff15(TAB):
    return 0
def onoff16(TAB):
    return 0
def onoff17(TAB):
    return 0
def onoff18(TAB):
    return 0
def onoff19(TAB):
    return 0
def onoff20(TAB):
    return 0
def onoff21(TAB):
    return 0
def onoff22(TAB):
    return 0
def onoff23(TAB):
    return 0
def onoff24(TAB):
    return 0
def onoff25(TAB):
    return 0
def onoff26(TAB):
    return 0
def onoff27(TAB):
    return 0
def onoff28(TAB):
    return 0
def onoff29(TAB):
    return 0
def onoff30(TAB):
    return 0
def onoff31(TAB):
    return 0
def onoff32(TAB):
    return 0
def onoff33(TAB):
    return 0
def onoff34(TAB):
    return 0
def onoff35(TAB):
    return 0
def onoff36(TAB):
    return 0
def onoff37(TAB):
    return 0
def onoff38(TAB):
    return 0
def onoff39(TAB):
    return 0
def onoff40(TAB):
    return 0
def onoff41(TAB):
    return 0
def onoff42(TAB):
    return 0
def onoff43(TAB):
    return 0
def onoff44(TAB):
    return 0
def onoff45(TAB):
    return 0
def onoff46(TAB):
    return 0
def onoff47(TAB):
    return 0
def onoff48(TAB):
    return 0
def onoff49(TAB):
    return 0
def onoff50(TAB):
    return 0
def onoff51(TAB):
    return 0
def onoff52(TAB):
    return 0
def onoff53(TAB):
    return 0
def onoff54(TAB):
    return 0
def onoff55(TAB):
    return 0
def onoff56(TAB):
    return 0
def onoff57(TAB):
    return 0
def onoff58(TAB):
    return 0
def onoff59(TAB):
    return 0
def onoff60(TAB):
    return 0
def onoff61(TAB):
    return 0
def onoff62(TAB):
    return 0
def onoff63(TAB):
    return 0
def onoff64(TAB):
    return 0
def onoff65(TAB):
    return 0
def onoff66(TAB):
    return 0
def onoff67(TAB):
    return 0
def onoff68(TAB):
    return 0
def onoff69(TAB):
    return 0
def onoff70(TAB):
    return 0
def onoff71(TAB):
    return 0
def onoff72(TAB):
    return 0
def onoff73(TAB):
    return 0
def onoff74(TAB):
    return 0
def onoff75(TAB):
    return 0
def onoff76(TAB):
    return 0
def onoff77(TAB):
    return 0
def onoff78(TAB):
    return 0
def onoff79(TAB):
    return 0
def onoff80(TAB):
    return 0
def onoff81(TAB):
    return 0
def onoff82(TAB):
    return 0
def onoff83(TAB):
    return 0
def onoff84(TAB):
    return 0
def onoff85(TAB):
    return 0
def onoff86(TAB):
    return 0
def onoff87(TAB):
    return 0
def onoff88(TAB):
    return 0
def onoff89(TAB):
    return 0
def onoff90(TAB):
    return 0