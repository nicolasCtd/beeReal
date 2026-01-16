import sys
import os
import shutil
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import (
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QDockWidget,
)
from PyQt5.QtGui import QPixmap, QCursor, QFont

from PyQt5 import QtCore, QtGui

from functools import partial

from PIL import Image, ImageDraw, ImageFont
from modules.ci_and_ds_tools import *
from modules.analyses import *
from modules.utile import *
from modules import globals
import logging
from datetime import datetime
from PyQt5.QtWidgets import (
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class MESSAGE(QMainWindow):
    """Cette classe permet de gérer les messages de l'IHM"""
    def __init__(self):
        super().__init__()
        self.error1 = "Please first load \nan image..."
        self.error2 = "Please first edit \nan image..."

    def message_erreur1(self):
        """Affiche le message d'erreur 1"""
        self.setWindowTitle(' ')
        layout = QVBoxLayout()
        coconfort = globals.media + "coconfort.png"
        pixmap = QPixmap(coconfort)
        label = QLabel()
        label.setPixmap(pixmap)
        layout.addWidget(label)
        txt = QLabel(self.error1)
        txt.setFont(QFont('Times', 12))
        layout.addWidget(txt)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()

    def message_erreur2(self):
        """Affiche le message d'erreur 2"""
        self.setWindowTitle(' ')
        layout = QVBoxLayout()
        coconfort = globals.media + "coconfort.png"
        pixmap = QPixmap(coconfort)
        label = QLabel()
        label.setPixmap(pixmap)
        layout.addWidget(label)
        txt = QLabel(self.error2)
        txt.setFont(QFont('Times', 12))
        layout.addWidget(txt)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()

    def message(self, msg):
        """Fonction permettant d'afficher un message en entrée."""
        self.move(100, 200)
        self.setWindowTitle(' ')
        layout = QHBoxLayout()
        aspicot = globals.media + "aspicot.png"
        pixmap = QPixmap(aspicot)
        label = QLabel()
        label.setPixmap(pixmap)
        layout.addWidget(label)
        txt = QLabel(msg)
        txt.setFont(QFont('Times', 12))
        layout.addWidget(txt)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()

class EDIT(QMainWindow):
    """
    Fenêtre d'édition de l'image.
    
    Gère le placement des points nécessaires au calcul :
    - de l'indice cubital (3 points)
    - de l'angle discoidal (4 points)
    """
    def __init__(self, tabs, num, parent=None):
        super().__init__(parent)
        
        # - count_ci_points : compteur pour le nombre de nombre de points 
        # placés sur l’image permettant de calculer l’indice cubital (3 points)

        # - count_ds_points : compteur pour le nombre de nombre de points
        # placés sur l’image permettant de calculer l’angle discoidal (4 points)

        self.count_ci_points = 0
        self.count_ds_points = 0

        # switchs pour activer / désactiver les boutons
        self.switch_ci = False
        self.switch_ds = False
        self.switch_back = False
        self.switch_done = False
        self.switch_button_zoom_in = True
        self.switch_button_zoom_out = False

        self.setWindowTitle('')
        self.move(50, 100)

        self.window = QWidget()
        self.layout = QVBoxLayout(self.window)

        self.ZOOM = 0
        self.last_name =  ["", ""]

        self.color_ci = [0, 255, 255]
        self.color_ds = [255, 255, 51]

        # Label pour afficher les résultats après édition de l'image (valeur du CI, classe etc)
        self.LAB_RIGHT = tabs.label_right

        self.GRIDS = tabs.grids
        self.WIDTH = tabs.width
        self.HEIGHT = tabs.height
        self.NUM = num
        self.LAB_RES = tabs.label_results
        self.RES = tabs.RES

        self.ci_points = [POINT(), POINT(), POINT()]
        self.ds_points = [POINT(), POINT(), POINT(), POINT()]

        self.path = tabs.path + os.sep
        self.TMP = tabs.tmp + os.sep
        self.IN_ = tabs.in_ + os.sep
        self.OUT = tabs.out + os.sep

    def display(self, fileName, all_tabs):
        """ Cette fonction permet d'aficher la fenêtre d'édition."""
        logging.info(f"Edition de l'image : {fileName}")
        self.name = get_file_name(fileName).replace(".jpg", "").replace("png", "")
        self.extension = "." + fileName.split(".")[-1]

        self.last_name[self.ZOOM] = insertnow(self.name + self.extension)

        try:
            print(f"Copie du fichier : {self.IN_}{fileName} >> {self.TMP}{self.last_name[self.ZOOM]}")
            shutil.copyfile(self.IN_ + fileName, self.TMP + self.last_name[self.ZOOM])
            logging.info(f"Copie du fichier : {self.IN_}{fileName} >> {self.TMP}{self.last_name[self.ZOOM]}")
            
        except:
            print("la copie du fichier a échoué")
            pass

        self.label = QLabel(self)
        pixmap = QPixmap(self.TMP + self.last_name[self.ZOOM])

        self.label.setPixmap(pixmap)
        self.setCentralWidget(self.label)

        self.pixmapWidth = pixmap.width()
        self.pixmapHeight = pixmap.height()

        width = min(1800, self.pixmapWidth)
        ratio = width / self.pixmapWidth 
        height = int(ratio * self.pixmapHeight)
        self.label.setFixedSize(width, height)

        self.label.setScaledContents(True)

        self.set_dock(all_tabs)
        self.show()
    
    def set_dock(self, all_tabs):
        """Ajoute les boutons à la fenêtre d'édition (ZOOM IN, ZOOM OUT, annuler, 3 CI points, 4 DS points, Done)."""
        search = globals.media + "search.png"
        self.btn_zoom_in = QPushButton("  ZOOM IN ")
        self.btn_zoom_in.setIcon(QtGui.QIcon(search))
        self.btn_zoom_in.setFont(QFont('Times', 14))
        self.btn_zoom_in.clicked.connect(self.zoom_in)

        fusee = globals.media + "fusee.webp"
        self.btn_zoom_out = QPushButton("  ZOOM OUT")
        self.btn_zoom_out.setIcon(QtGui.QIcon(fusee))
        self.btn_zoom_out.setFont(QFont('Times', 14))
        self.btn_zoom_out.clicked.connect(self.zoom_out)

        self.btn_zoom_in.setEnabled(self.switch_button_zoom_in)
        self.btn_zoom_out.setEnabled(self.switch_button_zoom_out)

        back = globals.media + "back.png"
        self.btn_cancel = QPushButton("")
        self.btn_cancel.setIcon(QtGui.QIcon(back))
        self.btn_cancel.clicked.connect(self.cancel)

        self.btn_cancel.setEnabled(self.switch_back)

        self.btn_ci_points = QPushButton("3 CI points")
        self.btn_ci_points.setFont(QFont('Times', 13))
        self.btn_ci_points.clicked.connect(partial(self.set_ci_points, switch=self.switch_ci))

        self.btn_ds_points = QPushButton("4 DS points")
        self.btn_ds_points.setFont(QFont('Times', 13))
        self.btn_ds_points.clicked.connect(partial(self.set_ds_points, switch=self.switch_ds))

        done = globals.media + "done.jpg"
        self.btn_done = QPushButton("  Done")
        self.btn_done.setIcon(QtGui.QIcon(done))
        self.btn_done.setFont(QFont('Times', 14))
        self.btn_done.setEnabled(self.switch_done)
        self.btn_done.clicked.connect(partial(self.validate_editing, all_tabs))

        self.layout.addWidget(self.btn_zoom_in)
        self.layout.addWidget(self.btn_zoom_out)
        self.layout.addWidget(self.btn_cancel)
        self.layout.addWidget(self.btn_ci_points)
        self.layout.addWidget(self.btn_ds_points)
        self.layout.addWidget(self.btn_done)
        self.dock = QDockWidget(f"{self.name}.jpg", self)
        self.dock.setFeatures(QDockWidget.DockWidgetMovable)
        self.dock.setWidget(self.window)

    def validate_editing(self, tabs):
        """
        Valide l'édition d'une image :
        - trace les 2 segments dont les longueurs permettent de calculer l'indice cubital (en bleu)
        - trace les 2 droites qui permettent de visualiser l'angle discoidal (en jaune)
        - ajoute les informations sur l'image (numéro de l'abeille, indice cubital, angle discoidal)
        - met à jour la fenêtre principale del'IHM : 
                * ajout de l'image éditée
                * ajout des informations de l'aile : indice cubital, angle discoidal, classe
        """
        file_wo_zoom, file_w_zoom = get_last_file(self.TMP, self.extension)
        im = IMAGE()

        img = self.TMP + file_wo_zoom
        im.load(img)
        im.ci_points = sort_ci_points(self.ci_points)
        logging.info(f"Point Ci n°1 : (i,j)=({im.ci_points[0].i}, {im.ci_points[0].j})")
        logging.info(f"Point Ci n°2 : (i,j)=({im.ci_points[1].i}, {im.ci_points[1].j})")
        logging.info(f"Point Ci n°3 : (i,j)=({im.ci_points[2].i}, {im.ci_points[2].j})")
        logging.info("----------------------")

        im.ds_points = sort_ds_points(self.ds_points)
        logging.info(f"Point Ds n°1 : (i,j)=({im.ds_points[0].i}, {im.ds_points[0].j})")
        logging.info(f"Point Ds n°2 : (i,j)=({im.ds_points[1].i}, {im.ds_points[1].j})")
        logging.info(f"Point Ds n°3 : (i,j)=({im.ds_points[2].i}, {im.ds_points[2].j})")
        logging.info(f"Point Ds n°4 : (i,j)=({im.ds_points[3].i}, {im.ds_points[3].j})")

        im.draw_ci_lines(self.color_ci)
        im.draw_ds_line_02(self.color_ds)
        im.draw_ds_line_02_perpendicular(self.color_ds)
        self.ci_value = compute_cubital_index(self.ci_points)
        self.ds_value = compute_discoidal_shift(im.point1, im.point2, im.ds_points)

        logging.info(f"Indice cubital Abeille #{self.NUM}) : {self.ci_value}")
        logging.info(f"Shift discoidal Abeille #{self.NUM}) : {clean(self.ds_value)}°")
        
        plt.imsave(fname=f"{self.OUT}{self.NUM}_out.jpg", arr=im.data)
        logging.info(f"Image sauvegardée : {self.OUT}{self.NUM}_out.jpg")

        self.add_infos()
        # self.write_results()
        logging.info(f"Les infos ont été ajoutées sur l'image.")
        
        img = os.sep.join([self.OUT, f"{self.NUM}_out.jpg"])
        pixmap = QPixmap(img)
        pixmap = pixmap.scaled(self.WIDTH, self.HEIGHT, Qt.KeepAspectRatio, Qt.FastTransformation)
        
        self.LAB_RIGHT[self.NUM-1].setPixmap(pixmap)

        tabs.showMinimized()
        self.close()

        ci, ds = get_ci_ds(self.ci_value, self.ds_value)

        H = HISTOGRAM(indices=[], path="", id_bees=[], save_abacus=0) # seulement utilisé pour utiliser la fonction get_classes()
        self.LAB_RES[self.NUM-1].setContentsMargins(30, 0, 0, 0)

        self.LAB_RES[self.NUM-1].setText(f"<u>Abeille #{self.NUM}</u> <br /> Ci : {ci} <br /> Ds : {ds}° <br /> Classe : {H.get_classes([self.ci_value])}")

        globals.edited[self.NUM] = 1

        self.RES[int(self.NUM)] = (clean(self.ci_value), clean(self.ds_value))


    def add_infos(self):
        img_path = globals.out + f"{self.NUM}_out.jpg"
        img = Image.open(img_path)
        # Create a drawing object
        draw = ImageDraw.Draw(img)
        # Define text attributes
        num = self.NUM
        ci = int(self.ci_value*100)/100
        ds = int(self.ds_value*100)/100
        tt = ""
        if np.sign(ds) == 1:
            tt = "+"
        text = f"Abeille #{num}             Indice cubital : {ci}             Angle discoïdal : {tt}{ds}°"
        font_path = globals.media + "Paul.ttf"
        font = ImageFont.truetype(font_path, size=40)
        text_color = (255, 0, 0)  # Red color

        # Position of the text
        position = (50, 25)

        # Add text to the image
        draw.text(position, text, fill=text_color, font=font)

        # Save or display the image
        img.save(f"{self.OUT}{self.NUM}_out.jpg")

    def set_ci_points(self, switch):
        """Appel de la fonction getPos_ci()"""
        self.switch_ci = switch
        # Set the cursor to a cross cursor
        # self.setCursor(Qt.CrossCursor)
        self.label.mousePressEvent = self.getPos_ci
    
    def set_ds_points(self, switch):
        """Appel de la fonction getPos_ds()"""
        self.switch_ds = switch
        # Set the cursor to a cross cursor
        # self.setCursor(Qt.CrossCursor)
        self.label.mousePressEvent = self.getPos_ds

    def getPos_ci(self, event):
        """
        - Récupère les coordonnées (x,y) du clic de l'utilisateur pour placer un point CI.
        - Dessine un point bleu où l'utilisateur a cliqué.
        - L'utilisateur place un maximum de 3 points pour le calcul de l'indice cubital.
        """
        self.count_ci_points += 1
        if  self.count_ci_points <= 3:
            x, y = self.get_pos_in_widget(event)
            file = self.last_name[self.ZOOM]
            if self.ZOOM:
                xmin, xmax, ymin, ymax = get_zoom_center(file)
                new_name = insertnow(self.name + "_zoom_" + f"xmin{xmin}xmax{xmax}ymin{ymin}ymax{ymax}end" + f"_CI_{self.count_ci_points}" + f"_DS_{self.count_ds_points}" + '.jpg')
            else:
                new_name = insertnow(self.name + f"_CI_{self.count_ci_points}" + f"_DS_{self.count_ds_points}" + '.jpg')
                xmin, xmax, ymin, ymax = 0, 0, 0, 0
            self.last_name[self.ZOOM] = new_name
            A = IMAGE()
            A.load(self.TMP + file)
            node, node_zoom = POINT(), POINT()
            node_zoom.j, node_zoom.i = x, y
            node.j, node.i = x+xmin, y+ymin
            # Sauvegarde de la position du point 
            # ///////////////////////////////////
            self.ci_points[self.count_ci_points-1] = node
            # ///////////////////////////////////
            # logging.info(f"coordonnées (ligne, col) du point Ci : ({node.i}, {node.j})")
            if self.ZOOM:
                A.highlight(node_zoom, self.color_ci)
            else:
                A.highlight(node, self.color_ci)

            plt.imsave(fname=f"{self.TMP}{self.last_name[self.ZOOM]}", arr=A.data)
            pixmap = QPixmap(f"{self.TMP}{os.sep}{self.last_name[self.ZOOM]}")
            self.label.setPixmap(pixmap)
            self.setCentralWidget(self.label)
            self.setCursor(Qt.ArrowCursor)
            if self.ZOOM:
                file_wo_zoom, file_w_zoom = get_last_file(self.TMP, self.extension)
                B = IMAGE()
                B.load(self.TMP + file_wo_zoom)
                B.highlight(node, self.color_ci)
                new_name = insertnow(self.name + f"_CI_{self.count_ci_points}" + f"_DS_{self.count_ds_points}" + '.jpg')
                plt.imsave(fname=f"{self.TMP}{new_name}", arr=B.data)
        if self.count_ci_points in [1, 2, 3]:
            self.switch_back = True
        else:
            self.switch_back = False
        if self.count_ci_points >= 3:
            self.switch_ci = False
        else:
            self.switch_ci = True
        
        if self.count_ci_points == 3 and self.count_ds_points == 4:
            self.switch_done = True
        
        self.btn_cancel.setEnabled(self.switch_back)
        self.btn_ci_points.setEnabled(self.switch_ci)
        self.btn_done.setEnabled(self.switch_done)
        self.setCursor(Qt.ArrowCursor)

    def getPos_ds(self, event):
        """
        - Récupère les coordonnées (x,y) du clic de l'utilisateur pour placer un point DS.
        - Dessine un point jaune où l'utilisateur a cliqué.
        - L'utilisateur place un maximum de 4 points pour le calcul de l'angle discoidal.
        """
        self.count_ds_points += 1
        if  self.count_ds_points <= 4:
            x, y = self.get_pos_in_widget(event)
            file = self.last_name[self.ZOOM]
            if self.ZOOM:
                xmin, xmax, ymin, ymax = get_zoom_center(file)
                new_name = insertnow(self.name + "_zoom_" + f"xmin{xmin}xmax{xmax}ymin{ymin}ymax{ymax}end" + f"_CI_{self.count_ci_points}" + f"_DS_{self.count_ds_points}" + '.jpg')
            else:
                new_name = insertnow(self.name + f"_CI_{self.count_ci_points}" + f"_DS_{self.count_ds_points}" + '.jpg')
                xmin, xmax, ymin, ymax = 0, 0, 0, 0
            self.last_name[self.ZOOM] = new_name
            A = IMAGE()
            A.load(self.TMP + file)
            node, node_zoom = POINT(), POINT()
            node_zoom.j, node_zoom.i = x, y
            node.j, node.i = x+xmin, y+ymin
            # logging.info(f"coordonnées (ligne, col) du point Ds : ({node.i}, {node.j})")
            # Sauvegarde de la position du point 
            # ///////////////////////////////////
            self.ds_points[self.count_ds_points-1] = node
            # ///////////////////////////////////
            if self.ZOOM:
                A.highlight(node_zoom, self.color_ds)
            else:
                A.highlight(node, self.color_ds)

            A.highlight(node, self.color_ds)
            plt.imsave(fname=f"{self.TMP}{self.last_name[self.ZOOM]}", arr=A.data)
            pixmap = QPixmap(f"{self.TMP}{os.sep}{self.last_name[self.ZOOM]}")
            self.label.setPixmap(pixmap)
            self.setCentralWidget(self.label)
            self.setCursor(Qt.ArrowCursor)
            if self.ZOOM:
                file_wo_zoom, file_w_zoom = get_last_file(self.TMP, self.extension)
                B = IMAGE()
                B.load(self.TMP + file_wo_zoom)
                B.highlight(node, self.color_ds)
                new_name = insertnow(self.name + f"_CI_{self.count_ci_points}" + f"_DS_{self.count_ds_points}" + '.jpg')
                plt.imsave(fname=f"{self.TMP}{new_name}", arr=B.data)
            
        if self.count_ds_points in [1, 2, 3, 4]:
            self.switch_back = True
        else:
            self.switch_back = False
        
        if self.count_ds_points >= 4:
            self.switch_ds = False
        else:
            self.switch_ds = True
        
        if self.count_ci_points == 3 and self.count_ds_points == 4:
            self.switch_done = True
            
        self.btn_cancel.setEnabled(self.switch_back)
        self.btn_ds_points.setEnabled(self.switch_ds)
        self.btn_done.setEnabled(self.switch_done)

        self.setCursor(Qt.ArrowCursor)

    def cancel(self):
        """Enlève le dernier point placé par l'utilisateur."""
        last_file_wo_zoom, last_file_w_zoom = get_last_file(self.TMP, self.extension)
        os.remove(self.TMP + last_file_wo_zoom)
        try:
            os.remove(self.TMP + last_file_w_zoom)
        except:
            pass
        last_file_wo_zoom, last_file_w_zoom = get_last_file(self.TMP, self.extension)
        self.last_name[0] = last_file_wo_zoom
        self.last_name[1] = last_file_w_zoom

        pixmap = QPixmap(f"{self.TMP}{os.sep}{self.last_name[self.ZOOM]}")
        self.label.setPixmap(pixmap)
        self.setCentralWidget(self.label)

        if ("CI_0" in last_file_wo_zoom) or ("CI" not in last_file_wo_zoom):
            self.count_ci_points = 0
        elif "CI_1" in last_file_wo_zoom:
            self.count_ci_points = 1
            self.ci_points[1] = POINT()
            self.ci_points[2] = POINT()
        elif "CI_2" in last_file_wo_zoom:
            self.count_ci_points = 2
            self.ci_points[2] = POINT()
        elif "CI_3" in last_file_wo_zoom:
            self.count_ci_points = 3

        if ("DS_0" in last_file_wo_zoom) or ("DS" not in last_file_wo_zoom):
            self.count_ds_points = 0
        elif "DS_1" in last_file_wo_zoom:
            self.count_ds_points = 1
        elif "DS_2" in last_file_wo_zoom:
            self.count_ds_points = 2
        elif "DS_3" in last_file_wo_zoom:
            self.count_ds_points = 3
        elif "DS_4" in last_file_wo_zoom:
            self.count_ds_points = 4

        if (self.count_ci_points<1) and (self.count_ds_points<1):
            self.switch_back = False
        else:
            self.switch_back = True

        if self.count_ci_points >= 3:
            self.switch_ci = False 
        else:
            self.switch_ci = True

        if self.count_ds_points >= 4:
            self.switch_ds = False 
        else:
            self.switch_ds = True

        self.btn_cancel.setEnabled(self.switch_back)
        self.btn_ci_points.setEnabled(self.switch_ci)
        self.btn_ds_points.setEnabled(self.switch_ds)
        self.switch_done = False
        self.btn_done.setEnabled(self.switch_done)


    def zoom_in(self):
        """
        - Change le curseur de la souris (forme de loupe).
        - Détecte la zone où l'utilisateur a cliqué.
        - Zoom sur cette zone.
        """
        self.ZOOM = 1
        zm = globals.media + "search.png"
        pixmap = QPixmap(zm)
        pixmap = pixmap.scaled(32, 32)
        cursor = QCursor(pixmap, 32, 32)
        self.setCursor(cursor)
        self.label.mousePressEvent = self.getPos_and_zoom

    def zoom_out(self):
        """
        - Affiche l'image initiale (affichage sans zoom)
        - désactive le bouton 'ZOOM OUT'
        """
        last_file_wo_zoom, last_file_w_zoom = get_last_file(self.TMP, self.extension)
        pixmap = QPixmap(self.TMP + last_file_wo_zoom)
        self.label.setPixmap(pixmap)
        self.setCentralWidget(self.label)
        self.switch_button_zoom_in = True
        self.btn_zoom_in.setEnabled(self.switch_button_zoom_in)
        self.switch_button_zoom_out = False
        self.btn_zoom_out.setEnabled(self.switch_button_zoom_out)
        self.ZOOM = 0
        self.last_name[0] = last_file_wo_zoom
        self.last_name[1] = last_file_w_zoom

    def get_pos_in_widget(self, event):
        pos = event.pos()

        pixmapRect = self.label.pixmap().rect()
        contentsRect = QtCore.QRectF(self.label.contentsRect())

        fx = pixmapRect.width() / contentsRect.width()
        fy = pixmapRect.height() / contentsRect.height()

        x = int(pos.x() * fx)
        y = int(pos.y() * fy)

        return x, y

    def getPos_and_zoom(self, event):
        """
        - Détecte la position x, y de l'endroit où a cliqué l'utilisateur
        - zoom sur cette zone
        - désactive le bouton 'ZOOM IN'
        """

        x, y = self.get_pos_in_widget(event)

        zoom_x = int(self.pixmapWidth / 2.5)
        zoom_y = int(self.pixmapHeight / 2.5)

        self.btn_zoom_in.setEnabled(self.switch_button_zoom_in)

        if self.switch_button_zoom_in and self.ZOOM:

            file_wo_zoom, file_w_zoom = get_last_file(self.TMP, self.extension)

            A = IMAGE()
            A.load(self.TMP + file_wo_zoom)

            j_min = max(x-zoom_x//2, 0)
            j_max = min(x+zoom_x//2, A.data.shape[1])

            i_min = max(y-zoom_y//2, 0)
            i_max = min(y+zoom_y//2, A.data.shape[0])

            image_temp = A.data[i_min:i_max, j_min:j_max, :]

            new_name = insertnow(self.name + "_zoom_" + f"xmin{j_min}xmax{j_max}ymin{i_min}ymax{i_max}end" + '.jpg')
            self.last_name[self.ZOOM] = new_name

            plt.imsave(fname=f"{self.TMP}{new_name}", arr=image_temp)

            pixmap = QPixmap(f"{self.TMP}{os.sep}{new_name}")

            self.label.setPixmap(pixmap)

            self.setCentralWidget(self.label)
        
            cursor = QCursor(Qt.ArrowCursor)
            self.setCursor(cursor)

            self.switch_button_zoom_in = False
            self.switch_button_zoom_out = True
            self.btn_zoom_in.setEnabled(self.switch_button_zoom_in)
            self.btn_zoom_out.setEnabled(self.switch_button_zoom_out)
            self.ZOOM = 1

        else:
            pass


class VISU(QMainWindow):
    def __init__(self):
        super(VISU, self).__init__()

    def display(self, path_to_image):
        self.setWindowTitle(' ')
        self.label = QLabel(self)
        pixmap = QPixmap(path_to_image)

        self.label.setPixmap(pixmap)
        self.setCentralWidget(self.label)

        self.pixmapWidth = pixmap.width()
        self.pixmapHeight = pixmap.height()

        # coeff = 0.83
        width = min(1800, self.pixmapWidth)
        ratio = width / self.pixmapWidth 
        height = int(ratio * self.pixmapHeight)
        self.label.setFixedSize(width, height)

        self.label.setScaledContents(True)
        self.move(50, 50)
        self.show()