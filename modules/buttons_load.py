from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
import logging
from PIL import Image
from modules import globals
from modules import buttons

def load1(all_tabs):
    """Charge l'image numero 1 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName1, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName1 != '':
        buttons.save_image(all_tabs.fileName1, all_tabs.in_, 1)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '1_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[0].setPixmap(pixmap)
        globals.loaded[1] = 1
    else:
        pass

def load2(all_tabs):
    """Charge l'image numero 2 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName2, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName2 != '':
        buttons.save_image(all_tabs.fileName2, all_tabs.in_, 2)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '2_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[1].setPixmap(pixmap)
        globals.loaded[2] = 1
    else:
        pass

def load3(all_tabs):
    """Charge l'image numero 3 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName3, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName3 != '':
        buttons.save_image(all_tabs.fileName3, all_tabs.in_, 3)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '3_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[2].setPixmap(pixmap)
        globals.loaded[3] = 1
    else:
        pass

def load4(all_tabs):
    """Charge l'image numero 4 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName4, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName4 != '':
        buttons.save_image(all_tabs.fileName4, all_tabs.in_, 4)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '4_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[3].setPixmap(pixmap)
        globals.loaded[4] = 1
    else:
        pass

def load5(all_tabs):
    """Charge l'image numero 5 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName5, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName5 != '':
        buttons.save_image(all_tabs.fileName5, all_tabs.in_, 5)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '5_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[4].setPixmap(pixmap)
        globals.loaded[5] = 1
    else:
        pass

def load6(all_tabs):
    """Charge l'image numero 6 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName6, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName6 != '':
        buttons.save_image(all_tabs.fileName6, all_tabs.in_, 6)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '6_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[5].setPixmap(pixmap)
        globals.loaded[6] = 1
    else:
        pass

def load7(all_tabs):
    """Charge l'image numero 7 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName7, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName7 != '':
        buttons.save_image(all_tabs.fileName7, all_tabs.in_, 7)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '7_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[6].setPixmap(pixmap)
        globals.loaded[7] = 1
    else:
        pass

def load8(all_tabs):
    """Charge l'image numero 8 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName8, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName8 != '':
        buttons.save_image(all_tabs.fileName8, all_tabs.in_, 8)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '8_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[7].setPixmap(pixmap)
        globals.loaded[8] = 1
    else:
        pass

def load9(all_tabs):
    """Charge l'image numero 9 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName9, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName9 != '':
        buttons.save_image(all_tabs.fileName9, all_tabs.in_, 9)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '9_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[8].setPixmap(pixmap)
        globals.loaded[9] = 1
    else:
        pass

def load10(all_tabs):
    """Charge l'image numero 10 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName10, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName10 != '':
        buttons.save_image(all_tabs.fileName10, all_tabs.in_, 10)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '10_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[9].setPixmap(pixmap)
        globals.loaded[10] = 1
    else:
        pass

def load11(all_tabs):
    """Charge l'image numero 11 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName11, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName11 != '':
        buttons.save_image(all_tabs.fileName11, all_tabs.in_, 11)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '11_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[10].setPixmap(pixmap)
        globals.loaded[11] = 1
    else:
        pass

def load12(all_tabs):
    """Charge l'image numero 12 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName12, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName12 != '':
        buttons.save_image(all_tabs.fileName12, all_tabs.in_, 12)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '12_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[11].setPixmap(pixmap)
        globals.loaded[12] = 1
    else:
        pass

def load13(all_tabs):
    """Charge l'image numero 13 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName13, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName13 != '':
        buttons.save_image(all_tabs.fileName13, all_tabs.in_, 13)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '13_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[12].setPixmap(pixmap)
        globals.loaded[13] = 1
    else:
        pass

def load14(all_tabs):
    """Charge l'image numero 14 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName14, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName14 != '':
        buttons.save_image(all_tabs.fileName14, all_tabs.in_, 14)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '14_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[13].setPixmap(pixmap)
        globals.loaded[14] = 1
    else:
        pass

def load15(all_tabs):
    """Charge l'image numero 15 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName15, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName15 != '':
        buttons.save_image(all_tabs.fileName15, all_tabs.in_, 15)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '15_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[14].setPixmap(pixmap)
        globals.loaded[15] = 1
    else:
        pass

def load16(all_tabs):
    """Charge l'image numero 16 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName16, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName16 != '':
        buttons.save_image(all_tabs.fileName16, all_tabs.in_, 16)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '16_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[15].setPixmap(pixmap)
        globals.loaded[16] = 1
    else:
        pass

def load17(all_tabs):
    """Charge l'image numero 17 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName17, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName17 != '':
        buttons.save_image(all_tabs.fileName17, all_tabs.in_, 17)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '17_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[16].setPixmap(pixmap)
        globals.loaded[17] = 1
    else:
        pass

def load18(all_tabs):
    """Charge l'image numero 18 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName18, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName18 != '':
        buttons.save_image(all_tabs.fileName18, all_tabs.in_, 18)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '18_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[17].setPixmap(pixmap)
        globals.loaded[18] = 1
    else:
        pass

def load19(all_tabs):
    """Charge l'image numero 19 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName19, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName19 != '':
        buttons.save_image(all_tabs.fileName19, all_tabs.in_, 19)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '19_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[18].setPixmap(pixmap)
        globals.loaded[19] = 1
    else:
        pass

def load20(all_tabs):
    """Charge l'image numero 20 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName20, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName20 != '':
        buttons.save_image(all_tabs.fileName20, all_tabs.in_, 20)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '20_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[19].setPixmap(pixmap)
        globals.loaded[20] = 1
    else:
        pass

def load21(all_tabs):
    """Charge l'image numero 21 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName21, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName21 != '':
        buttons.save_image(all_tabs.fileName21, all_tabs.in_, 21)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '21_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[20].setPixmap(pixmap)
        globals.loaded[21] = 1
    else:
        pass

def load22(all_tabs):
    """Charge l'image numero 22 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName22, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName22 != '':
        buttons.save_image(all_tabs.fileName22, all_tabs.in_, 22)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '22_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[21].setPixmap(pixmap)
        globals.loaded[22] = 1
    else:
        pass

def load23(all_tabs):
    """Charge l'image numero 23 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName23, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName23 != '':
        buttons.save_image(all_tabs.fileName23, all_tabs.in_, 23)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '23_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[22].setPixmap(pixmap)
        globals.loaded[23] = 1
    else:
        pass

def load24(all_tabs):
    """Charge l'image numero 24 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName24, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName24 != '':
        buttons.save_image(all_tabs.fileName24, all_tabs.in_, 24)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '24_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[23].setPixmap(pixmap)
        globals.loaded[24] = 1
    else:
        pass

def load25(all_tabs):
    """Charge l'image numero 25 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName25, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName25 != '':
        buttons.save_image(all_tabs.fileName25, all_tabs.in_, 25)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '25_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[24].setPixmap(pixmap)
        globals.loaded[25] = 1
    else:
        pass

def load26(all_tabs):
    """Charge l'image numero 26 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName26, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName26 != '':
        buttons.save_image(all_tabs.fileName26, all_tabs.in_, 26)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '26_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[25].setPixmap(pixmap)
        globals.loaded[26] = 1
    else:
        pass

def load27(all_tabs):
    """Charge l'image numero 27 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName27, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName27 != '':
        buttons.save_image(all_tabs.fileName27, all_tabs.in_, 27)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '27_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[26].setPixmap(pixmap)
        globals.loaded[27] = 1
    else:
        pass

def load28(all_tabs):
    """Charge l'image numero 28 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName28, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName28 != '':
        buttons.save_image(all_tabs.fileName28, all_tabs.in_, 28)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '28_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[27].setPixmap(pixmap)
        globals.loaded[28] = 1
    else:
        pass

def load29(all_tabs):
    """Charge l'image numero 29 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName29, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName29 != '':
        buttons.save_image(all_tabs.fileName29, all_tabs.in_, 29)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '29_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[28].setPixmap(pixmap)
        globals.loaded[29] = 1
    else:
        pass

def load30(all_tabs):
    """Charge l'image numero 30 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName30, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName30 != '':
        buttons.save_image(all_tabs.fileName30, all_tabs.in_, 30)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '30_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[29].setPixmap(pixmap)
        globals.loaded[30] = 1
    else:
        pass

def load31(all_tabs):
    """Charge l'image numero 31 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName31, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName31 != '':
        buttons.save_image(all_tabs.fileName31, all_tabs.in_, 31)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '31_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[30].setPixmap(pixmap)
        globals.loaded[31] = 1
    else:
        pass

def load32(all_tabs):
    """Charge l'image numero 32 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName32, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName32 != '':
        buttons.save_image(all_tabs.fileName32, all_tabs.in_, 32)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '32_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[31].setPixmap(pixmap)
        globals.loaded[32] = 1
    else:
        pass

def load33(all_tabs):
    """Charge l'image numero 33 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName33, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName33 != '':
        buttons.save_image(all_tabs.fileName33, all_tabs.in_, 33)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '33_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[32].setPixmap(pixmap)
        globals.loaded[33] = 1
    else:
        pass

def load34(all_tabs):
    """Charge l'image numero 34 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName34, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName34 != '':
        buttons.save_image(all_tabs.fileName34, all_tabs.in_, 34)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '34_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[33].setPixmap(pixmap)
        globals.loaded[34] = 1
    else:
        pass

def load35(all_tabs):
    """Charge l'image numero 35 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName35, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName35 != '':
        buttons.save_image(all_tabs.fileName35, all_tabs.in_, 35)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '35_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[34].setPixmap(pixmap)
        globals.loaded[35] = 1
    else:
        pass

def load36(all_tabs):
    """Charge l'image numero 36 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName36, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName36 != '':
        buttons.save_image(all_tabs.fileName36, all_tabs.in_, 36)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '36_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[35].setPixmap(pixmap)
        globals.loaded[36] = 1
    else:
        pass

def load37(all_tabs):
    """Charge l'image numero 37 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName37, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName37 != '':
        buttons.save_image(all_tabs.fileName37, all_tabs.in_, 37)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '37_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[36].setPixmap(pixmap)
        globals.loaded[37] = 1
    else:
        pass

def load38(all_tabs):
    """Charge l'image numero 38 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName38, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName38 != '':
        buttons.save_image(all_tabs.fileName38, all_tabs.in_, 38)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '38_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[37].setPixmap(pixmap)
        globals.loaded[38] = 1
    else:
        pass

def load39(all_tabs):
    """Charge l'image numero 39 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName39, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName39 != '':
        buttons.save_image(all_tabs.fileName39, all_tabs.in_, 39)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '39_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[38].setPixmap(pixmap)
        globals.loaded[39] = 1
    else:
        pass

def load40(all_tabs):
    """Charge l'image numero 40 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName40, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName40 != '':
        buttons.save_image(all_tabs.fileName40, all_tabs.in_, 40)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '40_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[39].setPixmap(pixmap)
        globals.loaded[40] = 1
    else:
        pass

def load41(all_tabs):
    """Charge l'image numero 41 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName41, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName41 != '':
        buttons.save_image(all_tabs.fileName41, all_tabs.in_, 41)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '41_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[40].setPixmap(pixmap)
        globals.loaded[41] = 1
    else:
        pass

def load42(all_tabs):
    """Charge l'image numero 42 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName42, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName42 != '':
        buttons.save_image(all_tabs.fileName42, all_tabs.in_, 42)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '42_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[41].setPixmap(pixmap)
        globals.loaded[42] = 1
    else:
        pass

def load43(all_tabs):
    """Charge l'image numero 43 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName43, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName43 != '':
        buttons.save_image(all_tabs.fileName43, all_tabs.in_, 43)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '43_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[42].setPixmap(pixmap)
        globals.loaded[43] = 1
    else:
        pass

def load44(all_tabs):
    """Charge l'image numero 44 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName44, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName44 != '':
        buttons.save_image(all_tabs.fileName44, all_tabs.in_, 44)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '44_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[43].setPixmap(pixmap)
        globals.loaded[44] = 1
    else:
        pass

def load45(all_tabs):
    """Charge l'image numero 45 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName45, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName45 != '':
        buttons.save_image(all_tabs.fileName45, all_tabs.in_, 45)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '45_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[44].setPixmap(pixmap)
        globals.loaded[45] = 1
    else:
        pass

def load46(all_tabs):
    """Charge l'image numero 46 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName46, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName46 != '':
        buttons.save_image(all_tabs.fileName46, all_tabs.in_, 46)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '46_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[45].setPixmap(pixmap)
        globals.loaded[46] = 1
    else:
        pass

def load47(all_tabs):
    """Charge l'image numero 47 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName47, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName47 != '':
        buttons.save_image(all_tabs.fileName47, all_tabs.in_, 47)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '47_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[46].setPixmap(pixmap)
        globals.loaded[47] = 1
    else:
        pass

def load48(all_tabs):
    """Charge l'image numero 48 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName48, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName48 != '':
        buttons.save_image(all_tabs.fileName48, all_tabs.in_, 48)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '48_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[47].setPixmap(pixmap)
        globals.loaded[48] = 1
    else:
        pass

def load49(all_tabs):
    """Charge l'image numero 49 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName49, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName49 != '':
        buttons.save_image(all_tabs.fileName49, all_tabs.in_, 49)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '49_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[48].setPixmap(pixmap)
        globals.loaded[49] = 1
    else:
        pass

def load50(all_tabs):
    """Charge l'image numero 50 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName50, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName50 != '':
        buttons.save_image(all_tabs.fileName50, all_tabs.in_, 50)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '50_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[49].setPixmap(pixmap)
        globals.loaded[50] = 1
    else:
        pass

def load51(all_tabs):
    """Charge l'image numero 51 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName51, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName51 != '':
        buttons.save_image(all_tabs.fileName51, all_tabs.in_, 51)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '51_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[50].setPixmap(pixmap)
        globals.loaded[51] = 1
    else:
        pass

def load52(all_tabs):
    """Charge l'image numero 52 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName52, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName52 != '':
        buttons.save_image(all_tabs.fileName52, all_tabs.in_, 52)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '52_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[51].setPixmap(pixmap)
        globals.loaded[52] = 1
    else:
        pass

def load53(all_tabs):
    """Charge l'image numero 53 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName53, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName53 != '':
        buttons.save_image(all_tabs.fileName53, all_tabs.in_, 53)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '53_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[52].setPixmap(pixmap)
        globals.loaded[53] = 1
    else:
        pass

def load54(all_tabs):
    """Charge l'image numero 54 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName54, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName54 != '':
        buttons.save_image(all_tabs.fileName54, all_tabs.in_, 54)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '54_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[53].setPixmap(pixmap)
        globals.loaded[54] = 1
    else:
        pass

def load55(all_tabs):
    """Charge l'image numero 55 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName55, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName55 != '':
        buttons.save_image(all_tabs.fileName55, all_tabs.in_, 55)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '55_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[54].setPixmap(pixmap)
        globals.loaded[55] = 1
    else:
        pass

def load56(all_tabs):
    """Charge l'image numero 56 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName56, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName56 != '':
        buttons.save_image(all_tabs.fileName56, all_tabs.in_, 56)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '56_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[55].setPixmap(pixmap)
        globals.loaded[56] = 1
    else:
        pass

def load57(all_tabs):
    """Charge l'image numero 57 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName57, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName57 != '':
        buttons.save_image(all_tabs.fileName57, all_tabs.in_, 57)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '57_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[56].setPixmap(pixmap)
        globals.loaded[57] = 1
    else:
        pass

def load58(all_tabs):
    """Charge l'image numero 58 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName58, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName58 != '':
        buttons.save_image(all_tabs.fileName58, all_tabs.in_, 58)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '58_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[57].setPixmap(pixmap)
        globals.loaded[58] = 1
    else:
        pass

def load59(all_tabs):
    """Charge l'image numero 59 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName59, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName59 != '':
        buttons.save_image(all_tabs.fileName59, all_tabs.in_, 59)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '59_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[58].setPixmap(pixmap)
        globals.loaded[59] = 1
    else:
        pass

def load60(all_tabs):
    """Charge l'image numero 60 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName60, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName60 != '':
        buttons.save_image(all_tabs.fileName60, all_tabs.in_, 60)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '60_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[59].setPixmap(pixmap)
        globals.loaded[60] = 1
    else:
        pass

def load61(all_tabs):
    """Charge l'image numero 61 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName61, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName61 != '':
        buttons.save_image(all_tabs.fileName61, all_tabs.in_, 61)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '61_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[60].setPixmap(pixmap)
        globals.loaded[61] = 1
    else:
        pass

def load62(all_tabs):
    """Charge l'image numero 62 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName62, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName62 != '':
        buttons.save_image(all_tabs.fileName62, all_tabs.in_, 62)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '62_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[61].setPixmap(pixmap)
        globals.loaded[62] = 1
    else:
        pass

def load63(all_tabs):
    """Charge l'image numero 63 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName63, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName63 != '':
        buttons.save_image(all_tabs.fileName63, all_tabs.in_, 63)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '63_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[62].setPixmap(pixmap)
        globals.loaded[63] = 1
    else:
        pass

def load64(all_tabs):
    """Charge l'image numero 64 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName64, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName64 != '':
        buttons.save_image(all_tabs.fileName64, all_tabs.in_, 64)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '64_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[63].setPixmap(pixmap)
        globals.loaded[64] = 1
    else:
        pass

def load65(all_tabs):
    """Charge l'image numero 65 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName65, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName65 != '':
        buttons.save_image(all_tabs.fileName65, all_tabs.in_, 65)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '65_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[64].setPixmap(pixmap)
        globals.loaded[65] = 1
    else:
        pass

def load66(all_tabs):
    """Charge l'image numero 66 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName66, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName66 != '':
        buttons.save_image(all_tabs.fileName66, all_tabs.in_, 66)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '66_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[65].setPixmap(pixmap)
        globals.loaded[66] = 1
    else:
        pass

def load67(all_tabs):
    """Charge l'image numero 67 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName67, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName67 != '':
        buttons.save_image(all_tabs.fileName67, all_tabs.in_, 67)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '67_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[66].setPixmap(pixmap)
        globals.loaded[67] = 1
    else:
        pass

def load68(all_tabs):
    """Charge l'image numero 68 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName68, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName68 != '':
        buttons.save_image(all_tabs.fileName68, all_tabs.in_, 68)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '68_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[67].setPixmap(pixmap)
        globals.loaded[68] = 1
    else:
        pass

def load69(all_tabs):
    """Charge l'image numero 69 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName69, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName69 != '':
        buttons.save_image(all_tabs.fileName69, all_tabs.in_, 69)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '69_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[68].setPixmap(pixmap)
        globals.loaded[69] = 1
    else:
        pass

def load70(all_tabs):
    """Charge l'image numero 70 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName70, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName70 != '':
        buttons.save_image(all_tabs.fileName70, all_tabs.in_, 70)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '70_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[69].setPixmap(pixmap)
        globals.loaded[70] = 1
    else:
        pass

def load71(all_tabs):
    """Charge l'image numero 71 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName71, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName71 != '':
        buttons.save_image(all_tabs.fileName71, all_tabs.in_, 71)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '71_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[70].setPixmap(pixmap)
        globals.loaded[71] = 1
    else:
        pass

def load72(all_tabs):
    """Charge l'image numero 72 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName72, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName72 != '':
        buttons.save_image(all_tabs.fileName72, all_tabs.in_, 72)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '72_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[71].setPixmap(pixmap)
        globals.loaded[72] = 1
    else:
        pass

def load73(all_tabs):
    """Charge l'image numero 73 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName73, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName73 != '':
        buttons.save_image(all_tabs.fileName73, all_tabs.in_, 73)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '73_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[72].setPixmap(pixmap)
        globals.loaded[73] = 1
    else:
        pass

def load74(all_tabs):
    """Charge l'image numero 74 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName74, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName74 != '':
        buttons.save_image(all_tabs.fileName74, all_tabs.in_, 74)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '74_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[73].setPixmap(pixmap)
        globals.loaded[74] = 1
    else:
        pass

def load75(all_tabs):
    """Charge l'image numero 75 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName75, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName75 != '':
        buttons.save_image(all_tabs.fileName75, all_tabs.in_, 75)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '75_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[74].setPixmap(pixmap)
        globals.loaded[75] = 1
    else:
        pass

def load76(all_tabs):
    """Charge l'image numero 76 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName76, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName76 != '':
        buttons.save_image(all_tabs.fileName76, all_tabs.in_, 76)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '76_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[75].setPixmap(pixmap)
        globals.loaded[76] = 1
    else:
        pass

def load77(all_tabs):
    """Charge l'image numero 77 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName77, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName77 != '':
        buttons.save_image(all_tabs.fileName77, all_tabs.in_, 77)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '77_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[76].setPixmap(pixmap)
        globals.loaded[77] = 1
    else:
        pass

def load78(all_tabs):
    """Charge l'image numero 78 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName78, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName78 != '':
        buttons.save_image(all_tabs.fileName78, all_tabs.in_, 78)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '78_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[77].setPixmap(pixmap)
        globals.loaded[78] = 1
    else:
        pass

def load79(all_tabs):
    """Charge l'image numero 79 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName79, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName79 != '':
        buttons.save_image(all_tabs.fileName79, all_tabs.in_, 79)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '79_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[78].setPixmap(pixmap)
        globals.loaded[79] = 1
    else:
        pass

def load80(all_tabs):
    """Charge l'image numero 80 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName80, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName80 != '':
        buttons.save_image(all_tabs.fileName80, all_tabs.in_, 80)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '80_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[79].setPixmap(pixmap)
        globals.loaded[80] = 1
    else:
        pass

def load81(all_tabs):
    """Charge l'image numero 81 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName81, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName81 != '':
        buttons.save_image(all_tabs.fileName81, all_tabs.in_, 81)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '81_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[80].setPixmap(pixmap)
        globals.loaded[81] = 1
    else:
        pass

def load82(all_tabs):
    """Charge l'image numero 82 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName82, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName82 != '':
        buttons.save_image(all_tabs.fileName82, all_tabs.in_, 82)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '82_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[81].setPixmap(pixmap)
        globals.loaded[82] = 1
    else:
        pass

def load83(all_tabs):
    """Charge l'image numero 83 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName83, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName83 != '':
        buttons.save_image(all_tabs.fileName83, all_tabs.in_, 83)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '83_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[82].setPixmap(pixmap)
        globals.loaded[83] = 1
    else:
        pass

def load84(all_tabs):
    """Charge l'image numero 84 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName84, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName84 != '':
        buttons.save_image(all_tabs.fileName84, all_tabs.in_, 84)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '84_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[83].setPixmap(pixmap)
        globals.loaded[84] = 1
    else:
        pass

def load85(all_tabs):
    """Charge l'image numero 85 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName85, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName85 != '':
        buttons.save_image(all_tabs.fileName85, all_tabs.in_, 85)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '85_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[84].setPixmap(pixmap)
        globals.loaded[85] = 1
    else:
        pass

def load86(all_tabs):
    """Charge l'image numero 86 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName86, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName86 != '':
        buttons.save_image(all_tabs.fileName86, all_tabs.in_, 86)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '86_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[85].setPixmap(pixmap)
        globals.loaded[86] = 1
    else:
        pass

def load87(all_tabs):
    """Charge l'image numero 87 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName87, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName87 != '':
        buttons.save_image(all_tabs.fileName87, all_tabs.in_, 87)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '87_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[86].setPixmap(pixmap)
        globals.loaded[87] = 1
    else:
        pass

def load88(all_tabs):
    """Charge l'image numero 88 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName88, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName88 != '':
        buttons.save_image(all_tabs.fileName88, all_tabs.in_, 88)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '88_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[87].setPixmap(pixmap)
        globals.loaded[88] = 1
    else:
        pass

def load89(all_tabs):
    """Charge l'image numero 89 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName89, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName89 != '':
        buttons.save_image(all_tabs.fileName89, all_tabs.in_, 89)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '89_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[88].setPixmap(pixmap)
        globals.loaded[89] = 1
    else:
        pass

def load90(all_tabs):
    """Charge l'image numero 90 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName90, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName90 != '':
        buttons.save_image(all_tabs.fileName90, all_tabs.in_, 90)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '90_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[89].setPixmap(pixmap)
        globals.loaded[90] = 1
    else:
        pass

def load91(all_tabs):
    """Charge l'image numero 91 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName91, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName91 != '':
        buttons.save_image(all_tabs.fileName91, all_tabs.in_, 91)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '91_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[90].setPixmap(pixmap)
        globals.loaded[91] = 1
    else:
        pass

def load92(all_tabs):
    """Charge l'image numero 92 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName92, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName92 != '':
        buttons.save_image(all_tabs.fileName92, all_tabs.in_, 92)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '92_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[91].setPixmap(pixmap)
        globals.loaded[92] = 1
    else:
        pass

def load93(all_tabs):
    """Charge l'image numero 93 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName93, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName93 != '':
        buttons.save_image(all_tabs.fileName93, all_tabs.in_, 93)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '93_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[92].setPixmap(pixmap)
        globals.loaded[93] = 1
    else:
        pass

def load94(all_tabs):
    """Charge l'image numero 94 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName94, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName94 != '':
        buttons.save_image(all_tabs.fileName94, all_tabs.in_, 94)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '94_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[93].setPixmap(pixmap)
        globals.loaded[94] = 1
    else:
        pass

def load95(all_tabs):
    """Charge l'image numero 95 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName95, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName95 != '':
        buttons.save_image(all_tabs.fileName95, all_tabs.in_, 95)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '95_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[94].setPixmap(pixmap)
        globals.loaded[95] = 1
    else:
        pass

def load96(all_tabs):
    """Charge l'image numero 96 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName96, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName96 != '':
        buttons.save_image(all_tabs.fileName96, all_tabs.in_, 96)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '96_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[95].setPixmap(pixmap)
        globals.loaded[96] = 1
    else:
        pass

def load97(all_tabs):
    """Charge l'image numero 97 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName97, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName97 != '':
        buttons.save_image(all_tabs.fileName97, all_tabs.in_, 97)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '97_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[96].setPixmap(pixmap)
        globals.loaded[97] = 1
    else:
        pass

def load98(all_tabs):
    """Charge l'image numero 98 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName98, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName98 != '':
        buttons.save_image(all_tabs.fileName98, all_tabs.in_, 98)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '98_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[97].setPixmap(pixmap)
        globals.loaded[98] = 1
    else:
        pass

def load99(all_tabs):
    """Charge l'image numero 99 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName99, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName99 != '':
        buttons.save_image(all_tabs.fileName99, all_tabs.in_, 99)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '99_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[98].setPixmap(pixmap)
        globals.loaded[99] = 1
    else:
        pass

def load100(all_tabs):
    """Charge l'image numero 100 dans l'interface."""
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    all_tabs.fileName100, _ = QFileDialog.getOpenFileName(all_tabs, 'Select File', '', 'All Files (*)', options=options)
    if all_tabs.fileName100 != '':
        buttons.save_image(all_tabs.fileName100, all_tabs.in_, 100)
        pixmap = QPixmap(all_tabs.in_ + os.sep + '100_in.jpg')
        pixmap = pixmap.scaled(all_tabs.width, all_tabs.height, Qt.KeepAspectRatio, Qt.FastTransformation)
        all_tabs.label_left[99].setPixmap(pixmap)
        globals.loaded[100] = 1
    else:
        pass

