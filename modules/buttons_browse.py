from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
import logging
from PIL import Image
from modules import globals
from modules import buttons

def browseFile1(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName1, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName1 != '':
        buttons.save_image(TABs.fileName1, TABs.in_, 1)
        pixmap = QPixmap(TABs.in_ + os.sep + '1_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[0].setPixmap(pixmap)
        globals.loaded[1] = 1
    else:
        pass

def browseFile2(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName2, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName2 != '':
        buttons.save_image(TABs.fileName2, TABs.in_, 2)
        pixmap = QPixmap(TABs.in_ + os.sep + '2_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[1].setPixmap(pixmap)
        globals.loaded[2] = 1
    else:
        pass

def browseFile3(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName3, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName3 != '':
        buttons.save_image(TABs.fileName3, TABs.in_, 3)
        pixmap = QPixmap(TABs.in_ + os.sep + '3_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[2].setPixmap(pixmap)
        globals.loaded[3] = 1
    else:
        pass

def browseFile4(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName4, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName4 != '':
        buttons.save_image(TABs.fileName4, TABs.in_, 4)
        pixmap = QPixmap(TABs.in_ + os.sep + '4_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[3].setPixmap(pixmap)
        globals.loaded[4] = 1
    else:
        pass

def browseFile5(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName5, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName5 != '':
        buttons.save_image(TABs.fileName5, TABs.in_, 5)
        pixmap = QPixmap(TABs.in_ + os.sep + '5_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[4].setPixmap(pixmap)
        globals.loaded[5] = 1
    else:
        pass

def browseFile6(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName6, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName6 != '':
        buttons.save_image(TABs.fileName6, TABs.in_, 6)
        pixmap = QPixmap(TABs.in_ + os.sep + '6_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[5].setPixmap(pixmap)
        globals.loaded[6] = 1
    else:
        pass

def browseFile7(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName7, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName7 != '':
        buttons.save_image(TABs.fileName7, TABs.in_, 7)
        pixmap = QPixmap(TABs.in_ + os.sep + '7_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[6].setPixmap(pixmap)
        globals.loaded[7] = 1
    else:
        pass

def browseFile8(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName8, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName8 != '':
        buttons.save_image(TABs.fileName8, TABs.in_, 8)
        pixmap = QPixmap(TABs.in_ + os.sep + '8_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[7].setPixmap(pixmap)
        globals.loaded[8] = 1
    else:
        pass

def browseFile9(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName9, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName9 != '':
        buttons.save_image(TABs.fileName9, TABs.in_, 9)
        pixmap = QPixmap(TABs.in_ + os.sep + '9_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[8].setPixmap(pixmap)
        globals.loaded[9] = 1
    else:
        pass

def browseFile10(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName10, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName10 != '':
        buttons.save_image(TABs.fileName10, TABs.in_, 10)
        pixmap = QPixmap(TABs.in_ + os.sep + '10_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[9].setPixmap(pixmap)
        globals.loaded[10] = 1
    else:
        pass

def browseFile11(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName11, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName11 != '':
        buttons.save_image(TABs.fileName11, TABs.in_, 11)
        pixmap = QPixmap(TABs.in_ + os.sep + '11_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[10].setPixmap(pixmap)
        globals.loaded[11] = 1
    else:
        pass

def browseFile12(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName12, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName12 != '':
        buttons.save_image(TABs.fileName12, TABs.in_, 12)
        pixmap = QPixmap(TABs.in_ + os.sep + '12_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[11].setPixmap(pixmap)
        globals.loaded[12] = 1
    else:
        pass

def browseFile13(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName13, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName13 != '':
        buttons.save_image(TABs.fileName13, TABs.in_, 13)
        pixmap = QPixmap(TABs.in_ + os.sep + '13_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[12].setPixmap(pixmap)
        globals.loaded[13] = 1
    else:
        pass

def browseFile14(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName14, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName14 != '':
        buttons.save_image(TABs.fileName14, TABs.in_, 14)
        pixmap = QPixmap(TABs.in_ + os.sep + '14_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[13].setPixmap(pixmap)
        globals.loaded[14] = 1
    else:
        pass

def browseFile15(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName15, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName15 != '':
        buttons.save_image(TABs.fileName15, TABs.in_, 15)
        pixmap = QPixmap(TABs.in_ + os.sep + '15_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[14].setPixmap(pixmap)
        globals.loaded[15] = 1
    else:
        pass

def browseFile16(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName16, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName16 != '':
        buttons.save_image(TABs.fileName16, TABs.in_, 16)
        pixmap = QPixmap(TABs.in_ + os.sep + '16_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[15].setPixmap(pixmap)
        globals.loaded[16] = 1
    else:
        pass

def browseFile17(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName17, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName17 != '':
        buttons.save_image(TABs.fileName17, TABs.in_, 17)
        pixmap = QPixmap(TABs.in_ + os.sep + '17_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[16].setPixmap(pixmap)
        globals.loaded[17] = 1
    else:
        pass

def browseFile18(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName18, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName18 != '':
        buttons.save_image(TABs.fileName18, TABs.in_, 18)
        pixmap = QPixmap(TABs.in_ + os.sep + '18_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[17].setPixmap(pixmap)
        globals.loaded[18] = 1
    else:
        pass

def browseFile19(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName19, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName19 != '':
        buttons.save_image(TABs.fileName19, TABs.in_, 19)
        pixmap = QPixmap(TABs.in_ + os.sep + '19_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[18].setPixmap(pixmap)
        globals.loaded[19] = 1
    else:
        pass

def browseFile20(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName20, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName20 != '':
        buttons.save_image(TABs.fileName20, TABs.in_, 20)
        pixmap = QPixmap(TABs.in_ + os.sep + '20_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[19].setPixmap(pixmap)
        globals.loaded[20] = 1
    else:
        pass

def browseFile21(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName21, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName21 != '':
        buttons.save_image(TABs.fileName21, TABs.in_, 21)
        pixmap = QPixmap(TABs.in_ + os.sep + '21_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[20].setPixmap(pixmap)
        globals.loaded[21] = 1
    else:
        pass

def browseFile22(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName22, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName22 != '':
        buttons.save_image(TABs.fileName22, TABs.in_, 22)
        pixmap = QPixmap(TABs.in_ + os.sep + '22_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[21].setPixmap(pixmap)
        globals.loaded[22] = 1
    else:
        pass

def browseFile23(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName23, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName23 != '':
        buttons.save_image(TABs.fileName23, TABs.in_, 23)
        pixmap = QPixmap(TABs.in_ + os.sep + '23_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[22].setPixmap(pixmap)
        globals.loaded[23] = 1
    else:
        pass

def browseFile24(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName24, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName24 != '':
        buttons.save_image(TABs.fileName24, TABs.in_, 24)
        pixmap = QPixmap(TABs.in_ + os.sep + '24_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[23].setPixmap(pixmap)
        globals.loaded[24] = 1
    else:
        pass

def browseFile25(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName25, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName25 != '':
        buttons.save_image(TABs.fileName25, TABs.in_, 25)
        pixmap = QPixmap(TABs.in_ + os.sep + '25_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[24].setPixmap(pixmap)
        globals.loaded[25] = 1
    else:
        pass

def browseFile26(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName26, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName26 != '':
        buttons.save_image(TABs.fileName26, TABs.in_, 26)
        pixmap = QPixmap(TABs.in_ + os.sep + '26_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[25].setPixmap(pixmap)
        globals.loaded[26] = 1
    else:
        pass

def browseFile27(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName27, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName27 != '':
        buttons.save_image(TABs.fileName27, TABs.in_, 27)
        pixmap = QPixmap(TABs.in_ + os.sep + '27_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[26].setPixmap(pixmap)
        globals.loaded[27] = 1
    else:
        pass

def browseFile28(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName28, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName28 != '':
        buttons.save_image(TABs.fileName28, TABs.in_, 28)
        pixmap = QPixmap(TABs.in_ + os.sep + '28_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[27].setPixmap(pixmap)
        globals.loaded[28] = 1
    else:
        pass

def browseFile29(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName29, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName29 != '':
        buttons.save_image(TABs.fileName29, TABs.in_, 29)
        pixmap = QPixmap(TABs.in_ + os.sep + '29_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[28].setPixmap(pixmap)
        globals.loaded[29] = 1
    else:
        pass

def browseFile30(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName30, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName30 != '':
        buttons.save_image(TABs.fileName30, TABs.in_, 30)
        pixmap = QPixmap(TABs.in_ + os.sep + '30_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[29].setPixmap(pixmap)
        globals.loaded[30] = 1
    else:
        pass

def browseFile31(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName31, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName31 != '':
        buttons.save_image(TABs.fileName31, TABs.in_, 31)
        pixmap = QPixmap(TABs.in_ + os.sep + '31_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[30].setPixmap(pixmap)
        globals.loaded[31] = 1
    else:
        pass

def browseFile32(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName32, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName32 != '':
        buttons.save_image(TABs.fileName32, TABs.in_, 32)
        pixmap = QPixmap(TABs.in_ + os.sep + '32_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[31].setPixmap(pixmap)
        globals.loaded[32] = 1
    else:
        pass

def browseFile33(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName33, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName33 != '':
        buttons.save_image(TABs.fileName33, TABs.in_, 33)
        pixmap = QPixmap(TABs.in_ + os.sep + '33_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[32].setPixmap(pixmap)
        globals.loaded[33] = 1
    else:
        pass

def browseFile34(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName34, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName34 != '':
        buttons.save_image(TABs.fileName34, TABs.in_, 34)
        pixmap = QPixmap(TABs.in_ + os.sep + '34_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[33].setPixmap(pixmap)
        globals.loaded[34] = 1
    else:
        pass

def browseFile35(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName35, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName35 != '':
        buttons.save_image(TABs.fileName35, TABs.in_, 35)
        pixmap = QPixmap(TABs.in_ + os.sep + '35_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[34].setPixmap(pixmap)
        globals.loaded[35] = 1
    else:
        pass

def browseFile36(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName36, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName36 != '':
        buttons.save_image(TABs.fileName36, TABs.in_, 36)
        pixmap = QPixmap(TABs.in_ + os.sep + '36_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[35].setPixmap(pixmap)
        globals.loaded[36] = 1
    else:
        pass

def browseFile37(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName37, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName37 != '':
        buttons.save_image(TABs.fileName37, TABs.in_, 37)
        pixmap = QPixmap(TABs.in_ + os.sep + '37_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[36].setPixmap(pixmap)
        globals.loaded[37] = 1
    else:
        pass

def browseFile38(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName38, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName38 != '':
        buttons.save_image(TABs.fileName38, TABs.in_, 38)
        pixmap = QPixmap(TABs.in_ + os.sep + '38_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[37].setPixmap(pixmap)
        globals.loaded[38] = 1
    else:
        pass

def browseFile39(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName39, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName39 != '':
        buttons.save_image(TABs.fileName39, TABs.in_, 39)
        pixmap = QPixmap(TABs.in_ + os.sep + '39_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[38].setPixmap(pixmap)
        globals.loaded[39] = 1
    else:
        pass

def browseFile40(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName40, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName40 != '':
        buttons.save_image(TABs.fileName40, TABs.in_, 40)
        pixmap = QPixmap(TABs.in_ + os.sep + '40_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[39].setPixmap(pixmap)
        globals.loaded[40] = 1
    else:
        pass

def browseFile41(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName41, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName41 != '':
        buttons.save_image(TABs.fileName41, TABs.in_, 41)
        pixmap = QPixmap(TABs.in_ + os.sep + '41_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[40].setPixmap(pixmap)
        globals.loaded[41] = 1
    else:
        pass

def browseFile42(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName42, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName42 != '':
        buttons.save_image(TABs.fileName42, TABs.in_, 42)
        pixmap = QPixmap(TABs.in_ + os.sep + '42_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[41].setPixmap(pixmap)
        globals.loaded[42] = 1
    else:
        pass

def browseFile43(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName43, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName43 != '':
        buttons.save_image(TABs.fileName43, TABs.in_, 43)
        pixmap = QPixmap(TABs.in_ + os.sep + '43_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[42].setPixmap(pixmap)
        globals.loaded[43] = 1
    else:
        pass

def browseFile44(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName44, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName44 != '':
        buttons.save_image(TABs.fileName44, TABs.in_, 44)
        pixmap = QPixmap(TABs.in_ + os.sep + '44_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[43].setPixmap(pixmap)
        globals.loaded[44] = 1
    else:
        pass

def browseFile45(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName45, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName45 != '':
        buttons.save_image(TABs.fileName45, TABs.in_, 45)
        pixmap = QPixmap(TABs.in_ + os.sep + '45_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[44].setPixmap(pixmap)
        globals.loaded[45] = 1
    else:
        pass

def browseFile46(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName46, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName46 != '':
        buttons.save_image(TABs.fileName46, TABs.in_, 46)
        pixmap = QPixmap(TABs.in_ + os.sep + '46_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[45].setPixmap(pixmap)
        globals.loaded[46] = 1
    else:
        pass

def browseFile47(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName47, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName47 != '':
        buttons.save_image(TABs.fileName47, TABs.in_, 47)
        pixmap = QPixmap(TABs.in_ + os.sep + '47_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[46].setPixmap(pixmap)
        globals.loaded[47] = 1
    else:
        pass

def browseFile48(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName48, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName48 != '':
        buttons.save_image(TABs.fileName48, TABs.in_, 48)
        pixmap = QPixmap(TABs.in_ + os.sep + '48_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[47].setPixmap(pixmap)
        globals.loaded[48] = 1
    else:
        pass

def browseFile49(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName49, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName49 != '':
        buttons.save_image(TABs.fileName49, TABs.in_, 49)
        pixmap = QPixmap(TABs.in_ + os.sep + '49_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[48].setPixmap(pixmap)
        globals.loaded[49] = 1
    else:
        pass

def browseFile50(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName50, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName50 != '':
        buttons.save_image(TABs.fileName50, TABs.in_, 50)
        pixmap = QPixmap(TABs.in_ + os.sep + '50_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[49].setPixmap(pixmap)
        globals.loaded[50] = 1
    else:
        pass

def browseFile51(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName51, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName51 != '':
        buttons.save_image(TABs.fileName51, TABs.in_, 51)
        pixmap = QPixmap(TABs.in_ + os.sep + '51_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[50].setPixmap(pixmap)
        globals.loaded[51] = 1
    else:
        pass

def browseFile52(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName52, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName52 != '':
        buttons.save_image(TABs.fileName52, TABs.in_, 52)
        pixmap = QPixmap(TABs.in_ + os.sep + '52_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[51].setPixmap(pixmap)
        globals.loaded[52] = 1
    else:
        pass

def browseFile53(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName53, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName53 != '':
        buttons.save_image(TABs.fileName53, TABs.in_, 53)
        pixmap = QPixmap(TABs.in_ + os.sep + '53_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[52].setPixmap(pixmap)
        globals.loaded[53] = 1
    else:
        pass

def browseFile54(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName54, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName54 != '':
        buttons.save_image(TABs.fileName54, TABs.in_, 54)
        pixmap = QPixmap(TABs.in_ + os.sep + '54_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[53].setPixmap(pixmap)
        globals.loaded[54] = 1
    else:
        pass

def browseFile55(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName55, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName55 != '':
        buttons.save_image(TABs.fileName55, TABs.in_, 55)
        pixmap = QPixmap(TABs.in_ + os.sep + '55_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[54].setPixmap(pixmap)
        globals.loaded[55] = 1
    else:
        pass

def browseFile56(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName56, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName56 != '':
        buttons.save_image(TABs.fileName56, TABs.in_, 56)
        pixmap = QPixmap(TABs.in_ + os.sep + '56_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[55].setPixmap(pixmap)
        globals.loaded[56] = 1
    else:
        pass

def browseFile57(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName57, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName57 != '':
        buttons.save_image(TABs.fileName57, TABs.in_, 57)
        pixmap = QPixmap(TABs.in_ + os.sep + '57_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[56].setPixmap(pixmap)
        globals.loaded[57] = 1
    else:
        pass

def browseFile58(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName58, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName58 != '':
        buttons.save_image(TABs.fileName58, TABs.in_, 58)
        pixmap = QPixmap(TABs.in_ + os.sep + '58_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[57].setPixmap(pixmap)
        globals.loaded[58] = 1
    else:
        pass

def browseFile59(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName59, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName59 != '':
        buttons.save_image(TABs.fileName59, TABs.in_, 59)
        pixmap = QPixmap(TABs.in_ + os.sep + '59_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[58].setPixmap(pixmap)
        globals.loaded[59] = 1
    else:
        pass

def browseFile60(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName60, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName60 != '':
        buttons.save_image(TABs.fileName60, TABs.in_, 60)
        pixmap = QPixmap(TABs.in_ + os.sep + '60_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[59].setPixmap(pixmap)
        globals.loaded[60] = 1
    else:
        pass

def browseFile61(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName61, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName61 != '':
        buttons.save_image(TABs.fileName61, TABs.in_, 61)
        pixmap = QPixmap(TABs.in_ + os.sep + '61_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[60].setPixmap(pixmap)
        globals.loaded[61] = 1
    else:
        pass

def browseFile62(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName62, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName62 != '':
        buttons.save_image(TABs.fileName62, TABs.in_, 62)
        pixmap = QPixmap(TABs.in_ + os.sep + '62_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[61].setPixmap(pixmap)
        globals.loaded[62] = 1
    else:
        pass

def browseFile63(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName63, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName63 != '':
        buttons.save_image(TABs.fileName63, TABs.in_, 63)
        pixmap = QPixmap(TABs.in_ + os.sep + '63_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[62].setPixmap(pixmap)
        globals.loaded[63] = 1
    else:
        pass

def browseFile64(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName64, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName64 != '':
        buttons.save_image(TABs.fileName64, TABs.in_, 64)
        pixmap = QPixmap(TABs.in_ + os.sep + '64_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[63].setPixmap(pixmap)
        globals.loaded[64] = 1
    else:
        pass

def browseFile65(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName65, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName65 != '':
        buttons.save_image(TABs.fileName65, TABs.in_, 65)
        pixmap = QPixmap(TABs.in_ + os.sep + '65_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[64].setPixmap(pixmap)
        globals.loaded[65] = 1
    else:
        pass

def browseFile66(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName66, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName66 != '':
        buttons.save_image(TABs.fileName66, TABs.in_, 66)
        pixmap = QPixmap(TABs.in_ + os.sep + '66_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[65].setPixmap(pixmap)
        globals.loaded[66] = 1
    else:
        pass

def browseFile67(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName67, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName67 != '':
        buttons.save_image(TABs.fileName67, TABs.in_, 67)
        pixmap = QPixmap(TABs.in_ + os.sep + '67_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[66].setPixmap(pixmap)
        globals.loaded[67] = 1
    else:
        pass

def browseFile68(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName68, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName68 != '':
        buttons.save_image(TABs.fileName68, TABs.in_, 68)
        pixmap = QPixmap(TABs.in_ + os.sep + '68_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[67].setPixmap(pixmap)
        globals.loaded[68] = 1
    else:
        pass

def browseFile69(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName69, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName69 != '':
        buttons.save_image(TABs.fileName69, TABs.in_, 69)
        pixmap = QPixmap(TABs.in_ + os.sep + '69_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[68].setPixmap(pixmap)
        globals.loaded[69] = 1
    else:
        pass

def browseFile70(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName70, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName70 != '':
        buttons.save_image(TABs.fileName70, TABs.in_, 70)
        pixmap = QPixmap(TABs.in_ + os.sep + '70_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[69].setPixmap(pixmap)
        globals.loaded[70] = 1
    else:
        pass

def browseFile71(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName71, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName71 != '':
        buttons.save_image(TABs.fileName71, TABs.in_, 71)
        pixmap = QPixmap(TABs.in_ + os.sep + '71_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[70].setPixmap(pixmap)
        globals.loaded[71] = 1
    else:
        pass

def browseFile72(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName72, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName72 != '':
        buttons.save_image(TABs.fileName72, TABs.in_, 72)
        pixmap = QPixmap(TABs.in_ + os.sep + '72_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[71].setPixmap(pixmap)
        globals.loaded[72] = 1
    else:
        pass

def browseFile73(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName73, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName73 != '':
        buttons.save_image(TABs.fileName73, TABs.in_, 73)
        pixmap = QPixmap(TABs.in_ + os.sep + '73_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[72].setPixmap(pixmap)
        globals.loaded[73] = 1
    else:
        pass

def browseFile74(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName74, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName74 != '':
        buttons.save_image(TABs.fileName74, TABs.in_, 74)
        pixmap = QPixmap(TABs.in_ + os.sep + '74_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[73].setPixmap(pixmap)
        globals.loaded[74] = 1
    else:
        pass

def browseFile75(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName75, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName75 != '':
        buttons.save_image(TABs.fileName75, TABs.in_, 75)
        pixmap = QPixmap(TABs.in_ + os.sep + '75_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[74].setPixmap(pixmap)
        globals.loaded[75] = 1
    else:
        pass

def browseFile76(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName76, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName76 != '':
        buttons.save_image(TABs.fileName76, TABs.in_, 76)
        pixmap = QPixmap(TABs.in_ + os.sep + '76_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[75].setPixmap(pixmap)
        globals.loaded[76] = 1
    else:
        pass

def browseFile77(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName77, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName77 != '':
        buttons.save_image(TABs.fileName77, TABs.in_, 77)
        pixmap = QPixmap(TABs.in_ + os.sep + '77_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[76].setPixmap(pixmap)
        globals.loaded[77] = 1
    else:
        pass

def browseFile78(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName78, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName78 != '':
        buttons.save_image(TABs.fileName78, TABs.in_, 78)
        pixmap = QPixmap(TABs.in_ + os.sep + '78_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[77].setPixmap(pixmap)
        globals.loaded[78] = 1
    else:
        pass

def browseFile79(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName79, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName79 != '':
        buttons.save_image(TABs.fileName79, TABs.in_, 79)
        pixmap = QPixmap(TABs.in_ + os.sep + '79_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[78].setPixmap(pixmap)
        globals.loaded[79] = 1
    else:
        pass

def browseFile80(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName80, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName80 != '':
        buttons.save_image(TABs.fileName80, TABs.in_, 80)
        pixmap = QPixmap(TABs.in_ + os.sep + '80_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[79].setPixmap(pixmap)
        globals.loaded[80] = 1
    else:
        pass

def browseFile81(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName81, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName81 != '':
        buttons.save_image(TABs.fileName81, TABs.in_, 81)
        pixmap = QPixmap(TABs.in_ + os.sep + '81_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[80].setPixmap(pixmap)
        globals.loaded[81] = 1
    else:
        pass

def browseFile82(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName82, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName82 != '':
        buttons.save_image(TABs.fileName82, TABs.in_, 82)
        pixmap = QPixmap(TABs.in_ + os.sep + '82_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[81].setPixmap(pixmap)
        globals.loaded[82] = 1
    else:
        pass

def browseFile83(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName83, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName83 != '':
        buttons.save_image(TABs.fileName83, TABs.in_, 83)
        pixmap = QPixmap(TABs.in_ + os.sep + '83_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[82].setPixmap(pixmap)
        globals.loaded[83] = 1
    else:
        pass

def browseFile84(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName84, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName84 != '':
        buttons.save_image(TABs.fileName84, TABs.in_, 84)
        pixmap = QPixmap(TABs.in_ + os.sep + '84_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[83].setPixmap(pixmap)
        globals.loaded[84] = 1
    else:
        pass

def browseFile85(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName85, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName85 != '':
        buttons.save_image(TABs.fileName85, TABs.in_, 85)
        pixmap = QPixmap(TABs.in_ + os.sep + '85_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[84].setPixmap(pixmap)
        globals.loaded[85] = 1
    else:
        pass

def browseFile86(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName86, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName86 != '':
        buttons.save_image(TABs.fileName86, TABs.in_, 86)
        pixmap = QPixmap(TABs.in_ + os.sep + '86_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[85].setPixmap(pixmap)
        globals.loaded[86] = 1
    else:
        pass

def browseFile87(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName87, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName87 != '':
        buttons.save_image(TABs.fileName87, TABs.in_, 87)
        pixmap = QPixmap(TABs.in_ + os.sep + '87_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[86].setPixmap(pixmap)
        globals.loaded[87] = 1
    else:
        pass

def browseFile88(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName88, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName88 != '':
        buttons.save_image(TABs.fileName88, TABs.in_, 88)
        pixmap = QPixmap(TABs.in_ + os.sep + '88_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[87].setPixmap(pixmap)
        globals.loaded[88] = 1
    else:
        pass

def browseFile89(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName89, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName89 != '':
        buttons.save_image(TABs.fileName89, TABs.in_, 89)
        pixmap = QPixmap(TABs.in_ + os.sep + '89_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[88].setPixmap(pixmap)
        globals.loaded[89] = 1
    else:
        pass

def browseFile90(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName90, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName90 != '':
        buttons.save_image(TABs.fileName90, TABs.in_, 90)
        pixmap = QPixmap(TABs.in_ + os.sep + '90_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[89].setPixmap(pixmap)
        globals.loaded[90] = 1
    else:
        pass

def browseFile91(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName91, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName91 != '':
        buttons.save_image(TABs.fileName91, TABs.in_, 91)
        pixmap = QPixmap(TABs.in_ + os.sep + '91_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[90].setPixmap(pixmap)
        globals.loaded[91] = 1
    else:
        pass

def browseFile92(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName92, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName92 != '':
        buttons.save_image(TABs.fileName92, TABs.in_, 92)
        pixmap = QPixmap(TABs.in_ + os.sep + '92_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[91].setPixmap(pixmap)
        globals.loaded[92] = 1
    else:
        pass

def browseFile93(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName93, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName93 != '':
        buttons.save_image(TABs.fileName93, TABs.in_, 93)
        pixmap = QPixmap(TABs.in_ + os.sep + '93_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[92].setPixmap(pixmap)
        globals.loaded[93] = 1
    else:
        pass

def browseFile94(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName94, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName94 != '':
        buttons.save_image(TABs.fileName94, TABs.in_, 94)
        pixmap = QPixmap(TABs.in_ + os.sep + '94_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[93].setPixmap(pixmap)
        globals.loaded[94] = 1
    else:
        pass

def browseFile95(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName95, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName95 != '':
        buttons.save_image(TABs.fileName95, TABs.in_, 95)
        pixmap = QPixmap(TABs.in_ + os.sep + '95_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[94].setPixmap(pixmap)
        globals.loaded[95] = 1
    else:
        pass

def browseFile96(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName96, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName96 != '':
        buttons.save_image(TABs.fileName96, TABs.in_, 96)
        pixmap = QPixmap(TABs.in_ + os.sep + '96_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[95].setPixmap(pixmap)
        globals.loaded[96] = 1
    else:
        pass

def browseFile97(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName97, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName97 != '':
        buttons.save_image(TABs.fileName97, TABs.in_, 97)
        pixmap = QPixmap(TABs.in_ + os.sep + '97_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[96].setPixmap(pixmap)
        globals.loaded[97] = 1
    else:
        pass

def browseFile98(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName98, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName98 != '':
        buttons.save_image(TABs.fileName98, TABs.in_, 98)
        pixmap = QPixmap(TABs.in_ + os.sep + '98_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[97].setPixmap(pixmap)
        globals.loaded[98] = 1
    else:
        pass

def browseFile99(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName99, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName99 != '':
        buttons.save_image(TABs.fileName99, TABs.in_, 99)
        pixmap = QPixmap(TABs.in_ + os.sep + '99_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[98].setPixmap(pixmap)
        globals.loaded[99] = 1
    else:
        pass

def browseFile100(TABs):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    TABs.fileName100, _ = QFileDialog.getOpenFileName(TABs, 'Select File', '', 'All Files (*)', options=options)
    if TABs.fileName100 != '':
        buttons.save_image(TABs.fileName100, TABs.in_, 100)
        pixmap = QPixmap(TABs.in_ + os.sep + '100_in.jpg')
        pixmap = pixmap.scaled(TABs.width, TABs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        TABs.label_left[99].setPixmap(pixmap)
        globals.loaded[100] = 1
    else:
        pass

