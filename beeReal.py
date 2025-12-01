import sys
import os
import shutil
import zipfile
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QSizePolicy,
    QTabWidget,
    QLineEdit,
    QFileDialog,
    QInputDialog,
    QMessageBox,
    QComboBox
)
from PyQt5.QtGui import QPixmap, QFont
from functools import partial
from modules.buttons_edit import *
from modules.buttons_visu import *
from modules.buttons_browse import *
from modules.buttons_onoff import *
from modules.ci_and_ds_tools import *
from modules.utile import *
from modules.analyses import *
import sys
import logging
from datetime import date
from modules import globals
from modules import buttons

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QAudioOutput
import csv

# Définir une fonction pour attraper toutes les exceptions non gérées
def log_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        # Laisse le Ctrl+C s'afficher normalement
        sys._excepthook_(exc_type, exc_value, exc_traceback)
        return
    # Log complet de l'erreur avec stack trace
    logging.error("Exception non gérée :", exc_info=(exc_type, exc_value, exc_traceback))

# Remplacer le hook d'exception
#¶sys.excepthook = log_exception

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

connections_edit = {1:editFile1, 2:editFile2, 3:editFile3, 4:editFile4, 5:editFile5,
                    6:editFile6, 7:editFile7, 8:editFile8, 9:editFile9, 10:editFile10,
                    11:editFile11, 12:editFile12, 13:editFile13, 14:editFile14, 15:editFile15,
                    16:editFile16, 17:editFile17, 18:editFile18, 19:editFile19, 20:editFile20,
                    21:editFile21, 22:editFile22, 23:editFile23, 24:editFile24, 25:editFile25,
                    26:editFile26, 27:editFile27, 28:editFile28, 29:editFile29, 30:editFile30,
                    31:editFile31, 32:editFile32, 33:editFile33, 34:editFile34, 35:editFile35,
                    36:editFile36, 37:editFile37, 38:editFile38, 39:editFile39, 40:editFile40,
                    41:editFile41, 42:editFile42, 43:editFile43, 44:editFile44, 45:editFile45,
                    46:editFile46, 47:editFile47, 48:editFile48, 49:editFile49, 50:editFile50,
                    51:editFile51, 52:editFile52, 53:editFile53, 54:editFile54, 55:editFile55,
                    56:editFile56, 57:editFile57, 58:editFile58, 59:editFile59, 60:editFile60,
                    61:editFile61, 62:editFile62, 63:editFile63, 64:editFile64, 65:editFile65,
                    66:editFile66, 67:editFile67, 68:editFile68, 69:editFile69, 70:editFile70,
                    71:editFile71, 72:editFile72, 73:editFile73, 74:editFile74, 75:editFile75,
                    76:editFile76, 77:editFile77, 78:editFile78, 79:editFile79, 80:editFile80,
                    81:editFile81, 82:editFile82, 83:editFile83, 84:editFile84, 85:editFile85,
                    86:editFile86, 87:editFile87, 88:editFile88, 89:editFile89, 90:editFile90,
                    91:editFile91, 92:editFile92, 93:editFile93, 94:editFile94, 95:editFile95,
                    96:editFile96, 97:editFile97, 98:editFile98, 99:editFile99, 100:editFile100}

connections_visu = {1:visu1, 2:visu2, 3:visu3, 4:visu4, 5:visu5,
                       6:visu6, 7:visu7, 8:visu8, 9:visu9, 10:visu10,
                       11:visu11, 12:visu12, 13:visu13, 14:visu14, 15:visu15,
                       16:visu16, 17:visu17, 18:visu18, 19:visu19, 20:visu20,
                       21:visu21, 22:visu22, 23:visu23, 24:visu24, 25:visu25,
                       26:visu26, 27:visu27, 28:visu28, 29:visu29, 30:visu30,
                       31:visu31, 32:visu32, 33:visu33, 34:visu34, 35:visu35,
                       36:visu36, 37:visu37, 38:visu38, 39:visu39, 40:visu40,
                       41:visu41, 42:visu42, 43:visu43, 44:visu44, 45:visu45,
                       46:visu46, 47:visu47, 48:visu48, 49:visu49, 50:visu50,
                       51:visu51, 52:visu52, 53:visu53, 54:visu54, 55:visu55,
                       56:visu56, 57:visu57, 58:visu58, 59:visu59, 60:visu60,
                       61:visu61, 62:visu62, 63:visu63, 64:visu64, 65:visu65,
                       66:visu66, 67:visu67, 68:visu68, 69:visu69, 70:visu70,
                       71:visu71, 72:visu72, 73:visu73, 74:visu74, 75:visu75,
                       76:visu76, 77:visu77, 78:visu78, 79:visu79, 80:visu80,
                       81:visu81, 82:visu82, 83:visu83, 84:visu84, 85:visu85,
                       86:visu86, 87:visu87, 88:visu88, 89:visu89, 90:visu90,
                       91:visu91, 92:visu92, 93:visu93, 94:visu94, 95:visu95,
                       96:visu96, 97:visu97, 98:visu98, 99:visu99, 100:visu100}

connections_load = {1:browseFile1, 2:browseFile2, 3:browseFile3, 4:browseFile4, 5:browseFile5,
                       6:browseFile6, 7:browseFile7, 8:browseFile8, 9:browseFile9, 10:browseFile10,
                       11:browseFile11, 12:browseFile12, 13:browseFile13, 14:browseFile14, 15:browseFile15,
                       16:browseFile16, 17:browseFile17, 18:browseFile18, 19:browseFile19, 20:browseFile20,
                       21:browseFile21, 22:browseFile22, 23:browseFile23, 24:browseFile24, 25:browseFile25,
                       26:browseFile26, 27:browseFile27, 28:browseFile28, 29:browseFile29, 30:browseFile30,
                       31:browseFile31, 32:browseFile32, 33:browseFile33, 34:browseFile34, 35:browseFile35,
                       36:browseFile36, 37:browseFile37, 38:browseFile38, 39:browseFile39, 40:browseFile40,
                       41:browseFile41, 42:browseFile42, 43:browseFile43, 44:browseFile44, 45:browseFile45,
                       46:browseFile46, 47:browseFile47, 48:browseFile48, 49:browseFile49, 50:browseFile50,
                       51:browseFile51, 52:browseFile52, 53:browseFile53, 54:browseFile54, 55:browseFile55,
                       56:browseFile56, 57:browseFile57, 58:browseFile58, 59:browseFile59, 60:browseFile60,
                       61:browseFile61, 62:browseFile62, 63:browseFile63, 64:browseFile64, 65:browseFile65,
                       66:browseFile66, 67:browseFile67, 68:browseFile68, 69:browseFile69, 70:browseFile70,
                       71:browseFile71, 72:browseFile72, 73:browseFile73, 74:browseFile74, 75:browseFile75,
                       76:browseFile76, 77:browseFile77, 78:browseFile78, 79:browseFile79, 80:browseFile80,
                       81:browseFile81, 82:browseFile82, 83:browseFile83, 84:browseFile84, 85:browseFile85,
                       86:browseFile86, 87:browseFile87, 88:browseFile88, 89:browseFile89, 90:browseFile90,
                       91:browseFile91, 92:browseFile92, 93:browseFile93, 94:browseFile94, 95:browseFile95,
                       96:browseFile96, 97:browseFile97, 98:browseFile98, 99:browseFile99, 100:browseFile100}
        
connections_ONOFF = {1:onoff1, 2:onoff2, 3:onoff3, 4:onoff4, 5:onoff5,
                     6:onoff6, 7:onoff7, 8:onoff8, 9:onoff9, 10:onoff10,
                     11:onoff11, 12:onoff12, 13:onoff13, 14:onoff14, 15:onoff15,
                     16:onoff16, 17:onoff17, 18:onoff18, 19:onoff19, 20:onoff20,
                     21:onoff21, 22:onoff22, 23:onoff23, 24:onoff24, 25:onoff25,
                     26:onoff26, 27:onoff27, 28:onoff28, 29:onoff29, 30:onoff30,
                     31:onoff31, 32:onoff32, 33:onoff33, 34:onoff34, 35:onoff35,
                     36:onoff36, 37:onoff37, 38:onoff38, 39:onoff39, 40:onoff40,
                     41:onoff41, 42:onoff42, 43:onoff43, 44:onoff44, 45:onoff45,
                     46:onoff46, 47:onoff47, 48:onoff48, 49:onoff49, 50:onoff50,
                     51:onoff51, 52:onoff52, 53:onoff53, 54:onoff54, 55:onoff55,
                     56:onoff56, 57:onoff57, 58:onoff58, 59:onoff59, 60:onoff60,
                     61:onoff61, 62:onoff62, 63:onoff63, 64:onoff64, 65:onoff65,
                     66:onoff66, 67:onoff67, 68:onoff68, 69:onoff69, 70:onoff70,
                     71:onoff71, 72:onoff72, 73:onoff73, 74:onoff74, 75:onoff75,
                     76:onoff76, 77:onoff77, 78:onoff78, 79:onoff79, 80:onoff80,
                     81:onoff82, 82:onoff82, 83:onoff83, 84:onoff84, 85:onoff85,
                     86:onoff86, 87:onoff87, 88:onoff88, 89:onoff89, 90:onoff90,
                     91:onoff91, 92:onoff92, 93:onoff93, 94:onoff94, 95:onoff95,
                     96:onoff96, 97:onoff97, 98:onoff98, 99:onoff99, 100:onoff100}

def set_paths():
    """Retourne le chemin absolu du dossier qui contient le script main.py """
    if getattr(sys, 'frozen', False):
        # PyInstaller utilise ce répertoire temporaire
        globals.out = os.sep.join([sys._MEIPASS, 'out']) + os.sep
        globals.in_ = os.sep.join([sys._MEIPASS, 'in']) + os.sep
        globals.tmp = os.sep.join([sys._MEIPASS, 'tmp']) + os.sep
        globals.logs = os.sep.join([sys._MEIPASS, 'logs']) + os.sep
        globals.media = os.sep.join([sys._MEIPASS, 'media']) + os.sep
        globals.path = sys._MEIPASS + os.sep
        globals.future = os.sep.join([sys._MEIPASS, 'media', 'future.mp3'])

    else:
        # Script normal
        globals.out = os.sep.join([os.path.dirname(__file__), 'out']) + os.sep
        globals.in_ = os.sep.join([os.path.dirname(__file__), 'in']) + os.sep
        globals.tmp = os.sep.join([os.path.dirname(__file__), 'tmp']) + os.sep
        globals.logs = os.sep.join([os.path.dirname(__file__), 'logs']) + os.sep
        globals.media = os.sep.join([os.path.dirname(__file__), 'media']) + os.sep
        globals.path = os.path.dirname(__file__) + os.sep
        globals.future = os.sep.join([os.path.dirname(__file__), 'media', 'future.mp3'])

    return 0

def launch_log(path, name):
    log_file =path + os.sep + name

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
                            
    logging.basicConfig(
        filename=log_file,
        filemode=globals.log_mode,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s')
    return 0


class FolderSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.button = QPushButton('Select Folder', self)
        self.button.clicked.connect(self.showFolderDialog)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def showFolderDialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        print('Selected Folder:', folder_path)

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bee real")

        self.out = globals.out
        self.in_ = globals.in_
        self.tmp = globals.tmp
        self.path = globals.path
        self.logs = globals.logs
        self.son = True

        logging.info("Démarrage du programme")

        if os.path.isdir(self.out):
            print(f"nettoyage du dossier 'out' : {self.out}")
            logging.info(f"nettoyage du dossier 'out' : {self.out}")
            for filename in os.listdir(self.out):
                file_path = self.out + os.sep + filename
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                        print(f"suppression du fichier {file_path}")
                        logging.info(f"suppression du fichier {file_path}")
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        print(f"suppression du dossier {file_path}")
                        logging.info(f"suppression du dossier {file_path}")
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
                    logging.info('Failed to delete %s. Reason: %s' % (file_path, e))
        else:
            logging.info(f"Création du répertoire de sortie : {self.out}")
            os.makedirs(self.out)

        if os.path.isdir(self.in_):
            print(f"nettoyage du dossier 'in' : {self.in_}")
            logging.info(f"nettoyage du dossier 'in' : {self.in_}")
            for filename in os.listdir(self.in_):
                file_path = self.in_ + os.sep + filename
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                        print(f"suppression du fichier {file_path}")
                        logging.info(f"suppression du fichier {file_path}")
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        print(f"suppression du dossier {file_path}")
                        logging.info(f"suppression du dossier {file_path}")
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
                    logging.info('Failed to delete %s. Reason: %s' % (file_path, e))
        else:
            logging.info(f"Création du répertoire d'entrée : {self.in_}")
            os.makedirs(self.in_)

        if os.path.isdir(self.tmp):
            print(f"nettoyage du dossier 'tmp' : {self.tmp}")
            logging.info(f"nettoyage du dossier 'tmp' : {self.tmp}")
            for filename in os.listdir(self.tmp):
                file_path = self.tmp + os.sep + filename
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                        print(f"suppression du fichier {file_path}")
                        logging.info(f"suppression du fichier {file_path}")
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        print(f"suppression du dossier {file_path}")
                        logging.info(f"suppression du fichier {file_path}")
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
                    logging.info('Failed to delete %s. Reason: %s' % (file_path, e))
        else:
            logging.info(f"Création du répertoire où sont stockés les fichiers temporaires : {self.tmp}")
            os.makedirs(self.tmp)


        if os.path.isdir(self.logs):
            print(f"nettoyage du dossier 'logs' : {self.logs}")
            logging.info(f"nettoyage du dossier 'logs' : {self.logs}")
            for filename in os.listdir(self.logs):
                file_path = self.logs + os.sep + filename
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                        print(f"suppression du fichier {file_path}")
                        logging.info(f"suppression du fichier {file_path}")
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        print(f"suppression du dossier {file_path}")
                        logging.info(f"suppression du fichier {file_path}")
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
                    logging.info('Failed to delete %s. Reason: %s' % (file_path, e))
        else:
            logging.info(f"Création du répertoire où sont stockés les fichiers temporaires : {self.logs}")
            os.makedirs(self.logs)

        launch_log(self.logs, f"logs_{date.today()}.log")

        self.tab_widget = Tabs(self, self.path)
        self.setCentralWidget(self.tab_widget)

        self.showMaximized()


    def close_all_windows(self):
        win_list = QApplication.allWindows()
        for w in win_list:
            w.close()

    def closeEvent(self, event: QCloseEvent) -> None:
        close = QMessageBox()
        close.setText("Exit?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close.setWindowTitle(" ")
        close = close.exec()

        if close == QMessageBox.Yes:
            event.accept()
            self.close_all_windows()
        else:
            event.ignore()


class Tabs(QWidget): 
    def __init__(self, parent, path): 
        super(QWidget, self).__init__(parent)

        self.out = globals.out
        self.in_ = globals.in_
        self.tmp = globals.tmp
        self.logs = globals.logs
        self.path = globals.path

        self.player = QMediaPlayer()
        self.play(globals.future)

        self.RES = {}
        self.analyse_name = str(date.today())

        self.switch_extra_plot = False

        self.layout = QVBoxLayout(self)
  
        # Initialize tab screen 
        self.tabs = QTabWidget()

        self.tab0 = QWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tab7 = QWidget()
        self.tab8 = QWidget()
        self.tab9 = QWidget()
        self.tab10 = QWidget()
        self.tab11 = QWidget()
        self.tab12 = QWidget()
        self.tab13 = QWidget()
        self.tab14 = QWidget()
        self.tab15 = QWidget()
        self.tab16 = QWidget()
        self.tab17 = QWidget()
        self.tab18 = QWidget()
        self.tab19 = QWidget()
        self.tab20 = QWidget()
        self.tab21 = QWidget()

        mf = QFont("Times New Roman", 14)

        self.tabs.addTab(self.tab0, "Main")
        self.tabs.addTab(self.tab1, "1-5")
        self.tabs.addTab(self.tab2, "6-10")
        self.tabs.addTab(self.tab3, "11-15")
        self.tabs.addTab(self.tab4, "16-20")
        self.tabs.addTab(self.tab5, "21-25")
        self.tabs.addTab(self.tab6, "26-30")
        self.tabs.addTab(self.tab7, "31-35")
        self.tabs.addTab(self.tab8, "36-40")
        self.tabs.addTab(self.tab9, "41-45")
        self.tabs.addTab(self.tab10, "46-50")
        self.tabs.addTab(self.tab11, "51-55")
        self.tabs.addTab(self.tab12, "56-60")
        self.tabs.addTab(self.tab13, "61-65")
        self.tabs.addTab(self.tab14, "66-70")
        self.tabs.addTab(self.tab15, "71-75")
        self.tabs.addTab(self.tab16, "76-80")
        self.tabs.addTab(self.tab17, "81-85")
        self.tabs.addTab(self.tab18, "86-90")
        self.tabs.addTab(self.tab19, "91-95")
        self.tabs.addTab(self.tab20, "96-100")
        self.tabs.addTab(self.tab21, "settings")

        self.tabs.setFont(QFont('Chalkduster', 13))
        self.tabs.setCurrentIndex(1)

        self.width = 413
        self.height = 307

        nb_tabs = 20

        self.label_left = list()
        self.label_right = list()
        self.label_results = list()

        for i in range(100):
            self.label_left.append(QLabel(self))
            self.label_right.append(QLabel(self))
            self.label_results.append(QLabel(self))

        self.label_analyses = [QLabel(self), QLabel(self)]
        self.label_analyses[0].setFixedWidth(900)
        self.label_analyses[0].setFixedHeight(850)

        self.label_analyses[1].setFixedWidth(900)
        self.label_analyses[1].setFixedHeight(850)

        layout_main_1 = QGridLayout()
        layout_main_2 = QGridLayout()
        vl = QVBoxLayout()
        vl.addLayout(layout_main_1)
        vl.addLayout(layout_main_2)

        SL = QGridLayout()

        my_font = QFont("Chalkduster", 16)

        text0 = QLabel("<u>Parameters for Histogram</u>")
        text1 = QLabel("<u>Parameters for Scatter plot</u>")

        text0.setFont(my_font)
        text1.setFont(my_font)

        SL.addWidget(text0, 0, 0, 1, 2, alignment=Qt.AlignTop)
        SL.addWidget(text1, 4, 0, 1, 2, alignment=Qt.AlignTop)

        sl = QVBoxLayout()

        self.BTN_params_apply = QPushButton()
        self.BTN_params_reset = QPushButton()

        self.BTN_params_apply.setFixedWidth(80)
        self.BTN_params_reset.setFixedWidth(80)

        SL.addWidget(self.BTN_params_apply, 6, 0, 1, 2)
        SL.addWidget(self.BTN_params_reset, 7, 0, 1, 2)

        self.BTN_params_apply.setText("Apply")
        self.BTN_params_reset.setText("Reset")

        self.visualisation = QComboBox()
        self.visualisation.addItems(['RUTTNER', 'DREHER'])
        self.visualisation.setCurrentText('RUTTNER')

        self.y_max = QComboBox()
        self.y_max.addItems(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
        self.y_max.setCurrentText('6')

        SL.addWidget(self.visualisation, 1, 2, 1, 2)

        SL.addWidget( QLabel("Visualisation"), 1, 1, 1, 2)

        self.BTN_params_apply.setEnabled(True)
        self.BTN_params_reset.setEnabled(False)

        self.BTN_params_apply.clicked.connect(self.params_apply_button)
        self.BTN_params_reset.clicked.connect(self.params_reset_button)

        self.classif = globals.classif
        self.y_max_scatter_plot = globals.y_max_scatter_plot

        label_max_y_scatter = QLabel("Max for Y-axis (°)")

        SL.addWidget(label_max_y_scatter, 5, 1, 1, 2)
        SL.addWidget(self.y_max, 5, 2, 1, 2)

        self.tab21.setLayout(SL)

        # layout_main_1.setVerticalSpacing(50)
        layout_main_1.setContentsMargins(0, 0, 15, 0)
        layout_main_2.setContentsMargins(0, 35, 0, 0)

        btn1 = QPushButton("Load\nanalysis")
        self.btn2 = QPushButton(f"Save\nanalysis\n{self.analyse_name}")
        self.btn3 = QPushButton(f"Launch\nanalysis\n{self.analyse_name}")
        label0 = QLabel("Name of the analysis: ")
        self.label00 = QLabel(self.analyse_name)
        label1 = QLabel("<u>Histogram of Cubital Index<u>")
        label2 = QLabel("<u>Cubital Index / Discoidal Shift<u>")
        # self.edit_analyse_name = QLineEdit()

        self.son = QPushButton("")
        self.son.setIcon(QtGui.QIcon(globals.media + "son_on.png"))
        self.son.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.son.resize(50, 50)
        self.son.clicked.connect(self.mute)

        self.btn_extra_plot = QPushButton(f"Add Deepwings data")
        self.btn_extra_plot.setEnabled(self.switch_extra_plot)

        label1.setStyleSheet("margin-bottom: 50px;")
        label2.setStyleSheet("margin-bottom: 50px;")
        self.btn_extra_plot.setStyleSheet("margin-bottom: 50px;")

        self.pb = QPushButton("Edit")
        self.pb.clicked.connect(self.edit_name)

        my_font = QFont("Chalkduster", 20)
        my_font2 = QFont("Chalkduster", 15)
        my_font3 = QFont("Chalkduster", 13)
        my_font4 = QFont("Chalkduster", 11)

        label1.setFont(my_font)
        label2.setFont(my_font)
        label0.setFont(my_font2)
        btn1.setFont(my_font3)
        self.btn2.setFont(my_font3)
        self.btn3.setFont(my_font3)
        self.btn_extra_plot.setFont(my_font4)

        self.btn2.setStyleSheet("QPushButton {background-color: plum}")
        self.btn3.setStyleSheet("QPushButton {background-color: lightblue}")

        btn1.resize(150, 150)
        btn1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.btn2.resize(150, 150)
        self.btn2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.btn3.resize(150, 150)
        self.btn3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.pb.resize(150, 150)
        self.pb.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        empty1 = globals.media + "empty1.png"
        pixmap = QPixmap(empty1)
        image_empty1 = self.label_analyses[0]
        image_empty1.setPixmap(pixmap)
        # image_empty1.setContentsMargins(0, -500, 0, 0)

        empty2 = globals.media + "empty2.png"
        pixmap = QPixmap(empty2)
        image_empty2 = self.label_analyses[1]
        image_empty2.setPixmap(pixmap)

        L1, H1 = 300, 200
        L2, H2 = 300, 200
        L3, H3 = 300, 200

        # cd1 = resource_path(f"images{os.sep}carte_dardagnan1.png")
        cd1 = globals.media + "deco1.jpg"
        pixmap = QPixmap(cd1)
        deco1 = QLabel(cd1)
        # deco1.setScaledContents(True)
        scaled_pixmap = pixmap.scaled(L1, H1)
        # scaled_pixmap = pixmap.scaled(L1, H1, Qt.IgnoreAspectRatio)
        deco1.setPixmap(scaled_pixmap)

        # cd1 = resource_path(f"images{os.sep}carte_dardagnan1.png")
        cd2 = globals.media + "deco4.jpg"
        pixmap = QPixmap(cd2)
        deco2 = QLabel(cd2)
        # deco1.setScaledContents(True)
        scaled_pixmap = pixmap.scaled(L2, H2, Qt.IgnoreAspectRatio)
        # scaled_pixmap = pixmap.scaled(L2, H2)
        deco2.setPixmap(scaled_pixmap)

        # cd3 = resource_path(f"images{os.sep}carte_dardagnan3.png")
        cd3 = globals.media + "deco5.png"
        pixmap = QPixmap(cd3)
        deco3 = QLabel()
        # deco2.setScaledContents(True)
        # scaled_pixmap = pixmap.scaled(L3, H3, Qt.IgnoreAspectRatio)
        scaled_pixmap = pixmap.scaled(L3, H3)
        deco3.setPixmap(scaled_pixmap)

        # deco.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout_main_1.addWidget(label0, 0+1, 0, 1, 3)
        layout_main_1.addWidget(self.label00, 0+1, 4, 1, 3)
        layout_main_1.addWidget(self.pb, 0+1, 8, 1, 3)
        layout_main_1.addWidget(self.son, 0, 0, 1, 3)
        layout_main_1.addWidget(btn1, 1, 0, 2, 2)
        layout_main_1.addWidget(self.btn2, 1, 4, 2, 2)
        layout_main_1.addWidget(self.btn3, 1, 8, 2, 2)
        
        layout_main_1.addWidget(deco1, 0, 10, 3, 3)
        layout_main_1.addWidget(deco2, 0, 13, 3, 3)
        layout_main_1.addWidget(deco3, 0, 16, 3, 3)
        
        layout_main_2.addWidget(image_empty1, 1, 0, 8, 8)
        layout_main_2.addWidget(image_empty2, 1, 10, 8, 8)

        layout_main_2.addWidget(label1, 1, 2, 1, 5)
        layout_main_2.addWidget(label2, 1, 12, 1, 5)

        layout_main_2.addWidget(self.btn_extra_plot, 1, 0, 1, 1)

        btn1.clicked.connect(self.load_project)
        self.btn2.clicked.connect(self.save_project)
        self.btn3.clicked.connect(self.lancer_analyse)
        self.btn_extra_plot.clicked.connect(self.add_histogram)

        self.grids = list()

        for num_tab in range(1, nb_tabs+1):
            
            self.grids.append(QGridLayout())

            for i in range(5):

                num_image = 5 * (num_tab - 1) + i + 1

                setBtn = QPushButton(f"{num_image}")
                setBtn.setFixedWidth(60)
                setBtn.setFixedHeight(60)
                setBtn.setStyleSheet("background-color: aquamarine")
                setBtn.clicked.connect(partial(connections_ONOFF[num_image], TABs=self))

                darda = globals.media + "dardagnan2.png"
                pixmap = QPixmap(darda)
                label = QLabel()
                label.setPixmap(pixmap)
                self.grids[-1].addWidget(setBtn, i, 0)
                self.grids[-1].addWidget(label, i, 1)

                im1 = globals.media + f"im{num_image}.png"
                pixmap = QPixmap(im1)
                label_left = self.label_left[num_image-1]
                label_left.setPixmap(pixmap)
                label_left.name = f"im{num_image}"
                self.grids[-1].addWidget(label_left, i, 2+1, 1, 1)

                pixmap = QPixmap(im1)
                label_right = self.label_right[num_image-1]
                label_right.setPixmap(pixmap)
                self.grids[-1].addWidget(label_right, i, 4+1, 1, 1)

                label_results = self.label_results[num_image-1]
                label_results.setText(f"<u>Abeille #{num_image}</u><br /> Ci :<br />Ds :<br />Classe :")
                label_results.setContentsMargins(30, 0, 0, 0)
                self.grids[-1].addWidget(label_results, i, 6+1, 1, 1)

                btn1 = QPushButton("Load")
                btn1.resize(50, 150)
                btn1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                
                btn2 = QPushButton("Edit")
                btn2.resize(50, 150)
                btn2.move(0,100)
                btn2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

                btn3 = QPushButton("Visu")
                # btn3.resize(80, 80)
                btn3.setFixedHeight(80)
                btn3.setFixedWidth(80)
                btn3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

                self.grids[-1].addWidget(btn1, i, 1+1)
                self.grids[-1].addWidget(btn2, i, 3+1)
                self.grids[-1].addWidget(btn3, i, 5+1)
                
                btn1.clicked.connect(partial(connections_load[num_image], TABs=self))
                btn2.clicked.connect(partial(connections_edit[num_image], TABs=self))
                btn3.clicked.connect(partial(connections_visu[num_image], TABs=self))

                darda = globals.media + "dardagnan2.png"

                pixmap = QPixmap(darda)
                darda = QLabel()
                darda.setPixmap(pixmap)
                self.grids[-1].addWidget(darda, i, 7+1)

        # Create main tab 
        self.tab0.layout = vl
        self.tab0.setFont(mf)
        self.tab0.setLayout(self.tab0.layout)

        # Create first tab 
        self.tab1.layout = self.grids[0]
        self.tab1.setFont(mf)
        self.tab1.setLayout(self.tab1.layout)

        # Create second tab 
        self.tab2.layout = self.grids[1]
        self.tab2.setFont(mf)
        self.tab2.setLayout(self.tab2.layout)

        # Create third tab 
        self.tab3.layout = self.grids[2]
        self.tab3.setLayout(self.tab3.layout)

        # Create fourth tab 
        self.tab4.layout = self.grids[3]
        self.tab4.setLayout(self.tab4.layout)

        # Create fifth tab 
        self.tab5.layout = self.grids[4]
        self.tab5.setLayout(self.tab5.layout)

        # Create sixth tab 
        self.tab6.layout = self.grids[5]
        self.tab6.setLayout(self.tab6.layout)

        # Create seventh tab 
        self.tab7.layout = self.grids[6]
        self.tab7.setLayout(self.tab7.layout)

        # Create eighth tab 
        self.tab8.layout = self.grids[7]
        self.tab8.setLayout(self.tab8.layout)

        # Create ninth tab 
        self.tab9.layout = self.grids[8]
        self.tab9.setLayout(self.tab9.layout)
        
        # # Create tenth tab 
        self.tab10.layout = self.grids[9]
        self.tab10.setLayout(self.tab10.layout)

        # # Create 11th tab 
        self.tab11.layout = self.grids[10]
        self.tab11.setLayout(self.tab11.layout)

        # # Create 12th tab 
        self.tab12.layout = self.grids[11]
        self.tab12.setLayout(self.tab12.layout)

        # # Create 13th tab 
        self.tab13.layout = self.grids[12]
        self.tab13.setLayout(self.tab13.layout)

        # # Create 14th tab 
        self.tab14.layout = self.grids[13]
        self.tab14.setLayout(self.tab14.layout)

        # # Create 15th tab 
        self.tab15.layout = self.grids[14]
        self.tab15.setLayout(self.tab15.layout)

        # # Create 16th tab 
        self.tab16.layout = self.grids[15]
        self.tab16.setLayout(self.tab16.layout)

        # # Create 17th tab 
        self.tab17.layout = self.grids[16]
        self.tab17.setLayout(self.tab17.layout)

        # # Create 18th tab 
        self.tab18.layout = self.grids[17]
        self.tab18.setLayout(self.tab18.layout)

        # # Create 19th tab 
        self.tab19.layout = self.grids[18]
        self.tab19.setLayout(self.tab19.layout)

        # # Create 20th tab 
        self.tab20.layout = self.grids[19]
        self.tab20.setLayout(self.tab20.layout)

        # # Create settings tab 
        self.tab21.layout =sl
        self.tab21.setLayout(self.tab21.layout)


        # Final step
        # #######
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.tabs.setCurrentIndex(0)


    def params_apply_button(self):
        print("apply button")
        self.BTN_params_apply.setEnabled(False)
        self.BTN_params_reset.setEnabled(True)
        globals.classif = self.visualisation.currentText()
        globals.y_max_scatter_plot = self.y_max.currentText()
        print(f"nouvelle valeur y_max : {globals.y_max_scatter_plot}")
        print(f"nouvelle valeur visualisation : {globals.classif}")
        return 0
    
    def params_reset_button(self):
        print("reset button")
        self.BTN_params_apply.setEnabled(True)
        self.BTN_params_reset.setEnabled(False)
        globals.classif = "RUTTNER"
        globals.y_max_scatter_plot = 6
        self.y_max.setCurrentText(str(globals.y_max_scatter_plot))
        self.visualisation.setCurrentText(str(globals.classif))
        print(f"valeurs remises aux valeurs par défaut")
        print(f"y_max : {globals.y_max_scatter_plot}°")
        print(f"classif : {globals.classif}")
        return 0

    def play(self, file):
        url = QUrl.fromLocalFile(file)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.setVolume(50)
        self.player.play()
        self.muted = False

    def mute(self):
        self.muted = not(self.muted)
        self.player.setMuted(self.muted)

        if not(self.muted):
            icon = "son_on.png"
        else:
            icon = "son_off.png"

        self.son.setIcon(QtGui.QIcon(globals.media + icon))
        self.son.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.son.resize(50, 50)

        return 0

    def edit_name(self):
        text, okPressed = QInputDialog.getText(self, " ", "Entrer le nom de l'analyse :", QLineEdit.Normal, "")
        if okPressed and text != '':
            self.label00.setText(text)
            self.btn2.setText(f"Save\nanalysis\n{text}")
            self.btn3.setText(f"Launch\nanalysis\n{text}")
            print(os.path.isfile(self.logs + f"logs_{self.analyse_name}.txt"))
            print('aa')
            logging.shutdown()
            shutil.move(self.logs + f"logs_{self.analyse_name}.log", self.logs + f"logs_{text}.log")
            self.analyse_name = text
            globals.log_mode = 'a'
            launch_log(self.logs, f"logs_{text}.log")
        return 0

    def save_project(self):
        DIR = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if DIR != "":
            save_results_txt(self.out, self.RES)
            with zipfile.ZipFile(DIR + os.sep + self.analyse_name + '.zip', "w") as zf:
                for file in os.listdir(self.out):
                    zf.write(f"{self.out}{os.sep}{file}", f"out{os.sep}{file}", zipfile.ZIP_DEFLATED )
                for file in os.listdir(self.tmp):
                    zf.write(f"{self.tmp}{os.sep}{file}", f"tmp{os.sep}{file}", zipfile.ZIP_DEFLATED )
                for file in os.listdir(self.in_):
                    zf.write(f"{self.in_}{os.sep}{file}", f"in{os.sep}{file}", zipfile.ZIP_DEFLATED )
                for file in os.listdir(self.logs):
                    zf.write(f"{self.logs}{os.sep}{file}", f"logs{os.sep}{file}", zipfile.ZIP_DEFLATED )
            self.dialog = MESSAGE()
            msg = f"L'analyse '{self.analyse_name}' a bien été enregistrée dans {DIR}"
            logging.info(msg)
            self.dialog.message(msg)
            self.dialog.show()
        else:
            pass
        return 0
    
    def load_project(self):
        DIR = QFileDialog.getOpenFileName(self, "Select a .zip project file")
        if DIR[0] != "":
            project_file = str(DIR[0])
            logging.info(f"Load project '{project_file}'")

            self.analyse_name = get_file_name(project_file)
            self.label00.setText(self.analyse_name)
            self.btn2.setText(f"Save\nanalysis\n{self.analyse_name}")
            self.btn3.setText(f"Launch\nanalysis\n{self.analyse_name}")
            
            shutil.unpack_archive(filename=project_file, extract_dir=self.tmp)
            copytree(src=self.tmp + os.sep + "in", dst=self.in_)
            copytree(src=self.tmp + os.sep + "out", dst=self.out)

            shutil.copyfile(src=f"{self.tmp}{os.sep}logs{os.sep}logs_{self.analyse_name}.log", dst=f"{self.path}{os.sep}logs{os.sep}logs_{self.analyse_name}.log")
            globals.log_mode = 'a'

            print(f"chargement des résultats {self.out}results.txt")
            self.RES = load_results(self.out + "results.txt")
            print("results already computed:")
            print(self.RES)

            logging.info("Affichage dans l'IHM des valeurs Ci et Ds")
            H = HISTOGRAM(indices=[], path="", id_bees=[], save_abacus=0)
            for num_abeille in self.RES.keys():
                print(num_abeille)
                logging.info(f"Abeille n°{num_abeille}")
                ci, ds = get_ci_ds(float(self.RES[num_abeille][0]), float(self.RES[num_abeille][1]))
                logging.info(f"Ci : {ci}, Ds : {ds}°")
                print(ci, ds)
                cla = H.get_classes([float(ci)])
                self.label_results[num_abeille-1].setText(
                    f"<u>Abeille #{num_abeille}</u> <br /> Ci : {ci} <br /> Ds : {ds}° <br /> Classe : {cla}")
                globals.edited[num_abeille] = 1
                globals.loaded[num_abeille] = 1
            for file in os.listdir(self.in_):
                num_abeille = int(file.split("_")[0])
                if num_abeille not in self.RES.keys():
                    print(f"Attention : l'abeille {num_abeille} n'a pas été trouvée dans le fichier de résultats")
                    logging.info(f"Attention : l'abeille {num_abeille} n'a pas été trouvée dans le fichier de résultats")
                else:
                    ff_in = self.in_ + os.sep + file
                    pixmap = QPixmap(ff_in)
                    pixmap = pixmap.scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.FastTransformation)
                    self.label_left[num_abeille-1].setPixmap(pixmap)
                    ff_out = self.out + os.sep + str(num_abeille) + "_out.jpg"
                    print(ff_out)
                    self.label_left[num_abeille-1].setPixmap(pixmap)
                    pixmap_out = QPixmap(ff_out)
                    pixmap_out = pixmap_out.scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.FastTransformation)
                    self.label_right[num_abeille-1].setPixmap(pixmap_out)
                    globals.enabled[num_abeille] = int(self.RES[num_abeille][2])
            for num_abeille in self.RES.keys():
                if not globals.enabled[num_abeille]:
                    buttons.turnToGrayImages(TABs=self, num=num_abeille)
        else:
            pass
        # self.tabs.setCurrentIndex(1)
        return 0
    
    def lancer_analyse(self):
        logging.info(f"Lancement de l'analyse : calcul de l'histogramme des indices + scatter plots DS vs CI")
        if len(self.RES) < 1:
            self.dialog = MESSAGE()
            msg = f"Error: at least 1 measure is expected (advised: >30)"
            self.dialog.message(msg)
            logging.info(msg)
        else:
            logging.info("calcul de l'histogramme de l'indice cubital")
            self.indices = []
            self.shifts = []
            self.id_bees = []
            for abeille in self.RES.keys():
                if globals.enabled[abeille]:
                    self.indices.append(float(self.RES[abeille][0]))
                    self.shifts.append(float(self.RES[abeille][1]))
                    self.id_bees.append(abeille)
            ci_images, ds_image, HISTO = analyse(self.indices, self.shifts, self.id_bees, path_out=self.out, visu=globals.classif)
            for image in ci_images:
                if "mellifera" in image:
                    ci_image = image 
            pixmap = QPixmap(ci_image)
            self.label_analyses[0].setPixmap(pixmap)
            pixmap = QPixmap(ds_image)
            self.label_analyses[1].setPixmap(pixmap)
            # self.setFixedSize(self.tab0.layout.sizeHint())()
            self.resize(self.tab0.sizeHint().width(), self.tab0.sizeHint().height())
            self.switch_extra_plot = True
            self.btn_extra_plot.setEnabled(self.switch_extra_plot)
        return
    
    def add_histogram(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        csv_file, _ = QFileDialog.getOpenFileName(self.tab0, "Select File", "", "All Files (*)", options=options)

        leg = csv_file.split("/")[-1].replace(" ", "_").replace(".csv", "")

        #res = dict()
        indices = list()
        angles = list()
        abeilles = list()

        if csv_file.split(os.sep)[-1] != '':
            with open(csv_file, newline='', encoding="utf-8") as f:
                lecteur = csv.reader(f, delimiter=";")
                for ligne in lecteur:
                    # each lign is a list of values (1 value per column)
                    try:
                        if ligne[5] != '0':
                            abeilles.append(int(ligne[0].replace('.jpg', '')))
                            indices.append(float(ligne[5].replace(',', '.')))
                            angles.append(float(ligne[7].replace(',', '.')))
                    except:
                        continue

        #new_histo = HISTOGRAM(indices=indices, path="", id_bees=abeilles, save_abacus=0)
        #x, y = new_histo.histogram()

        print(leg + f" ({len(indices)} abeilles)")

        ci_images, ds_image, HISTO = analyse2(self.indices, self.shifts, self.id_bees,
                                              indices, 
                                              angles,
                                              abeilles,
                                              LEG=leg + f" ({len(indices)} bees)", path_out=self.out, visu=classif)


        for image in ci_images:
            if "mellifera" in image:
                    ci_image = image
        pixmap = QPixmap(ci_image)
        self.label_analyses[0].setPixmap(pixmap)
        pixmap = QPixmap(ds_image)
        self.label_analyses[1].setPixmap(pixmap)
        self.resize(self.tab0.sizeHint().width(), self.tab0.sizeHint().height())

        return 0

if __name__ == '__main__':

    app = QApplication(sys.argv)
    
    screen = app.screens()[0]
    dpi = screen.physicalDotsPerInch()

    set_paths()

    window = MainWindow()

    window.show()

    app.exec()
