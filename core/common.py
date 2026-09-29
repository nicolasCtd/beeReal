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
from PyQt5.QtGui import QPixmap, QCursor, QFont, QImage

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
import copy

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
    - de l'indice de Hantel (4 points : 2 points CI, 1 points DS, +1 point)
    """
    def __init__(self, tabs, num, parent=None):
        super().__init__(parent)

        self.zoom = False
        self.x_min = 0
        self.y_min = 0

        self.switch_button_zoom_in = True
        self.switch_button_zoom_out = True

        self.setWindowTitle('')
        self.move(50, 100)

        self.window = QWidget()
        self.layout = QVBoxLayout(self.window)

        self.color_ci = [0, 255, 255]
        self.color_ds = [255, 255, 51]
        self.color_hi = [255, 0, 0]

        self.colors = {"ci":self.color_ci, "ds":self.color_ds, "hi":self.color_hi}

        # Label pour afficher les résultats après édition de l'image (valeur du CI, classe etc)
        self.LAB_RIGHT = tabs.label_right

        self.GRIDS = tabs.grids
        self.WIDTH = tabs.width
        self.HEIGHT = tabs.height
        self.NUM = num
        self.LAB_RES = tabs.label_results
        self.RES = tabs.RES

        # self.pts = tabs.PTS[num]

        self.path = tabs.path + os.sep
        self.TMP = tabs.tmp + os.sep
        self.IN_ = tabs.in_ + os.sep
        self.OUT = tabs.out + os.sep

        self.name = f"{num}_in"
        self.extension = ".jpg"

        self.original_image = IMAGE()
        self.original_image.load(self.IN_ + self.name + self.extension)

        self.count_zoom = 0

        if len(tabs.list_of_images[num]) > 0: 
            self.list_of_images = tabs.list_of_images[num]
            self.list_of_points = tabs.list_of_points[num]
        else:
            self.list_of_images =  [self.original_image]
            self.list_of_points =  []

        # if len(tabs.list_of_images_zoom[num]) > 0: 
        #     self.list_of_images_zoom = tabs.list_of_images_zoom[num]
        # else:
        #     self.list_of_images_zoom =  []
        self.list_of_images_zoom =  []

    def ci_button_turned_on(self):
        return self.count_ci_points() < 3

    def ds_button_turned_on(self):
        if globals.analysis_level[globals.analysis] > 1:
            return self.count_ds_points() < 4
        return False

    def hi_button_turned_on(self):
        if globals.analysis_level[globals.analysis] > 2:
            return self.count_hi_points() < 1
        return False
    
    @property
    def done_button_turned_on(self):
        if globals.analysis_level[globals.analysis] == 1:
            return self.count_ci_points() == 3
        elif globals.analysis_level[globals.analysis] == 2:
            return self.count_ci_points() == 3 and self.count_ds_points() == 4()
        elif globals.analysis_level[globals.analysis] == 3:
            return self.count_ci_points() == 3 and self.count_ds_points() == 4 and self.count_hi_points() == 1
        return False

    def display(self, filename, all_tabs):
        """ Cette fonction permet d'aficher la fenêtre d'édition."""
        num = int(filename.split("_")[0])
        self.all_tabs = all_tabs

        image = self.list_of_images[-1]

        logging.info(f"Edition de l'image : {self.name}")

        self.label = QLabel(self)

        h, w, channels = image.data.shape

        qimage = QImage(
            image.data.data,
            w,
            h,
            3 * w,
            QImage.Format_RGB888,
        )
         
        pixmap = QPixmap.fromImage(qimage.copy())
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

        self.btn_ci_points = QPushButton("3 CI points")
        self.btn_ci_points.setFont(QFont('Times', 13))
        self.btn_ci_points.clicked.connect(partial(self.set_ci_points, switch=self.ci_button_turned_on))

        self.btn_ds_points = QPushButton("4 DS points")
        self.btn_ds_points.setFont(QFont('Times', 13))
        self.btn_ds_points.clicked.connect(partial(self.set_ds_points, switch=self.ds_button_turned_on))

        self.btn_hi_points = QPushButton("1 HI point")
        self.btn_hi_points.setFont(QFont('Times', 13))
        self.btn_hi_points.clicked.connect(partial(self.set_hi_point, switch=self.hi_button_turned_on))
    
        done = globals.media + "done.jpg"
        self.btn_done = QPushButton("  Done")
        self.btn_done.setIcon(QtGui.QIcon(done))
        self.btn_done.setFont(QFont('Times', 14))
        self.btn_done.setEnabled(self.done_button_turned_on)
        self.btn_done.clicked.connect(partial(self.validate_editing, all_tabs))

        self.btn_ci_points.setEnabled(self.ci_button_turned_on())
        self.btn_ds_points.setEnabled(self.ds_button_turned_on())
        self.btn_hi_points.setEnabled(self.hi_button_turned_on())

        self.layout.addWidget(self.btn_zoom_in)
        self.layout.addWidget(self.btn_zoom_out)
        self.layout.addWidget(self.btn_cancel)
        self.layout.addWidget(self.btn_ci_points)
        self.layout.addWidget(self.btn_ds_points)
        self.layout.addWidget(self.btn_hi_points)
        self.layout.addWidget(self.btn_done)
        self.dock = QDockWidget(f"{self.name}.jpg", self)
        self.dock.setFeatures(QDockWidget.DockWidgetMovable)
        self.dock.setWidget(self.window)

        # self.addDockWidget(Qt.LeftDockWidgetArea, self.dock)

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
        image = copy.deepcopy(self.list_of_images[-1])

        ci_points = list()
        ds_points = list()
        hi_points = list()
        for point in self.list_of_points:
            if point.label == "ci":
                ci_points.append(point)
            if point.label == "ds":
                ds_points.append(point)
            if point.label == "hi":
                hi_points.append(point)

        image.ci_points = sort_ci_points(ci_points)
        image.ds_points = sort_ds_points(ds_points)
        image.hi_points = hi_points

        logging.info(f"Point Ci n°1 : (i,j)=({image.ci_points[0].i}, {image.ci_points[0].j})")
        logging.info(f"Point Ci n°2 : (i,j)=({image.ci_points[1].i}, {image.ci_points[1].j})")
        logging.info(f"Point Ci n°3 : (i,j)=({image.ci_points[2].i}, {image.ci_points[2].j})")
        logging.info("----------------------")

        if globals.analysis_level[globals.analysis] > 1:
            logging.info(f"Point Ds n°1 : (i,j)=({image.ds_points[0].i}, {image.ds_points[0].j})")
            logging.info(f"Point Ds n°2 : (i,j)=({image.ds_points[1].i}, {image.ds_points[1].j})")
            logging.info(f"Point Ds n°3 : (i,j)=({image.ds_points[2].i}, {image.ds_points[2].j})")
            logging.info(f"Point Ds n°4 : (i,j)=({image.ds_points[3].i}, {image.ds_points[3].j})")

        image.draw_ci_lines(self.color_ci)
        self.ci_value = compute_cubital_index(image.ci_points)
        logging.info(f"Indice cubital Abeille #{self.NUM}) : {self.ci_value}")

        if globals.analysis_level[globals.analysis] > 1:
            image.draw_ds_line_02(self.color_ds)
            image.draw_ds_line_02_perpendicular(self.color_ds)    
            self.ds_value = compute_discoidal_shift(image.point1, image.point2, image.ds_points)
            logging.info(f"Shift discoidal Abeille #{self.NUM}) : {clean(self.ds_value)}°")

        if globals.analysis_level[globals.analysis] > 2:
            image.draw_hi_lines(self.color_hi)
            self.hi_value = compute_hantel_index(image.hi_points[0], image.ds_points[1], image.ci_points[0], image.ci_points[2])


        plt.imsave(fname=f"{self.OUT}{self.NUM}_out.jpg", arr=image.data)
        logging.info(f"Image sauvegardée : {self.OUT}{self.NUM}_out.jpg")

        self.add_infos()
        # self.write_results()
        logging.info(f"Les infos ont été ajoutées sur l'image.")
        
        img = os.sep.join([self.OUT, f"{self.NUM}_out.jpg"])
        pixmap = QPixmap(img)
        pixmap = pixmap.scaled(self.WIDTH, self.HEIGHT, Qt.KeepAspectRatio, Qt.FastTransformation)
        
        self.LAB_RIGHT[self.NUM-1].setPixmap(pixmap)

        # tabs.showMinimized()
        self.close()

        ci= format_ci(self.ci_value)
        H = HISTOGRAM(indices=[], path="", id_bees=[], save_abacus=0) # seulement utilisé pour utiliser la fonction get_classes()
        ci_class = H.get_classes([self.ci_value])[0]

        self.RES[int(self.NUM)] = (clean(self.ci_value), ci_class, None, None)

        ds = None
        if globals.analysis_level[globals.analysis] > 1:
            ds = format_ds(self.ds_value)
            self.RES[int(self.NUM)] = (clean(self.ci_value), ci_class, clean(self.ds_value), None)

        hi = None
        if globals.analysis_level[globals.analysis] > 2:
            hi = format_hi(self.hi_value)
            self.RES[int(self.NUM)] = (clean(self.ci_value), ci_class, clean(self.ds_value), clean(self.hi_value))
        
        self.LAB_RES[self.NUM-1].setContentsMargins(30, 0, 0, 0)

        text_ihm = text_result_IHM(num_abeille=self.NUM, ci=ci, ci_class=ci_class, ds=ds, hi=hi)

        self.LAB_RES[self.NUM-1].setText(text_ihm)

        globals.edited[self.NUM] = 1

        tabs.list_of_images[self.NUM] = self.list_of_images
        tabs.list_of_images_zoom[self.NUM] = self.list_of_images_zoom
        tabs.list_of_points[self.NUM] = self.list_of_points

    def add_infos(self):
        img_path = globals.out + f"{self.NUM}_out.jpg"
        img = Image.open(img_path)
        # Create a drawing object
        draw = ImageDraw.Draw(img)
        # Define text attributes
        num = self.NUM
        # ci = int(self.ci_value*100)/100
        # ds = int(self.ds_value*100)/100

        ci = format_ci(self.ci_value)

        text = f"Abeille #{num}             Cubital Index: {ci}"
        if globals.analysis_level[globals.analysis] > 1:
            ds = format_ds(self.ds_value)
            text += f"    Discoïdal shift: {ds}°"
        if globals.analysis_level[globals.analysis] > 2:
            hi = format_hi(self.hi_value)
            text += f"    Hantel Index: {hi}"

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

    def set_hi_point(self, switch):
        """Appel de la fonction getPos_hi()"""
        self.switch_hi = switch
        # Set the cursor to a cross cursor
        # self.setCursor(Qt.CrossCursor)
        self.label.mousePressEvent = self.getPos_hi

    # def set_points(self):
    #     """"""

    #     self.list_of_images = [self.original_image]
    #     self.list_of_images_zoom = []

    #     data_source = self.original_image.data.copy()
       
    #     if self.count_zoom > 0:
    #         new_image_zoom = IMAGE()
    #         new_image_zoom.load2(data_source[self.y_min:self.y_max, self.x_min:self.x_max, :])
    #         self.list_of_images_zoom.append(copy.deepcopy(new_image_zoom))
    #         for point in self.list_of_points:
    #             point_zoom = point.shifted(di=-self.y_min, dj=-self.x_min)
    #             new_image_zoom.highlight(point_zoom, self.colors[point.label])
    #             self.list_of_images_zoom.append(copy.deepcopy(new_image_zoom))

    #     new_image = IMAGE()
    #     new_image.load2(data_source)
    #     for point in self.list_of_points:
    #         new_image.highlight(point, self.colors[point.label])
    #         self.list_of_images.append(copy.deepcopy(new_image))

    #     if self.count_zoom > 0:
    #         data = np.ascontiguousarray(self.list_of_images_zoom[-1].data, dtype=np.uint8)
    #     else:
    #         data = np.ascontiguousarray(self.list_of_images[-1].data, dtype=np.uint8)

    #     h, w, channels = data.shape

    #     qimage = QImage(
    #         data.tobytes(),
    #         w,
    #         h,
    #         3 * w,
    #         QImage.Format_RGB888,
    #     )

    #     self.refresh_buttons()

    #     return QPixmap.fromImage(qimage.copy())

    # def set_points(self):
    #     """"""

    #     data_source = self.original_image.data.copy()


    #     if self.count_zoom > 0:
    #         data_source = data_source[
    #             self.y_min:self.y_max,
    #             self.x_min:self.x_max,
    #             :
    #         ]

    #     # if self.count_zoom > 0:
    #     #     new_image_zoom = IMAGE()
    #     #     new_image_zoom.load2(data_source[self.y_min:self.y_max, self.x_min:self.x_max, :])
    #     #     self.list_of_images_zoom.append(copy.deepcopy(new_image_zoom))
    #     #     for point in self.list_of_points:
    #     #         point_zoom = point.shifted(di=-self.y_min, dj=-self.x_min)
    #     #         new_image_zoom.highlight(point_zoom, self.colors[point.label])
    #     #         self.list_of_images_zoom.append(copy.deepcopy(new_image_zoom))

    #     # new_image = IMAGE()
    #     # new_image.load2(data_source)

    #     image = IMAGE()
    #     image.load2(data_source)

    #     for point in self.list_of_points:
    #         if self.count_zoom > 0:
    #             point_display = point.shifted(
    #                 di=-self.y_min,
    #                 dj=-self.x_min,
    #             )
    #         else:
    #             point_display = point

    #     image.highlight(
    #         point_display,
    #         self.colors[point.label],
    #     )

    #     # for point in self.list_of_points:
    #     #     new_image.highlight(point, self.colors[point.label])
    #     #     self.list_of_images.append(copy.deepcopy(new_image))

    #     # if self.count_zoom > 0:
    #     #     data = np.ascontiguousarray(self.list_of_images_zoom[-1].data, dtype=np.uint8)
    #     # else:
    #     #     data = np.ascontiguousarray(self.list_of_images[-1].data, dtype=np.uint8)

    #     data = np.ascontiguousarray(image.data, dtype=np.uint8)

    #     h, w, _ = data.shape

    #     qimage = QImage(
    #         data.tobytes(),
    #         w,
    #         h,
    #         3 * w,
    #         QImage.Format_RGB888,
    #     )

    #     self.refresh_buttons()

    #     return QPixmap.fromImage(qimage.copy())


    #     # h, w, channels = data.shape

    #     # qimage = QImage(
    #     #     data.tobytes(),
    #     #     w,
    #     #     h,
    #     #     3 * w,
    #     #     QImage.Format_RGB888,
    #     # )

    #     # self.refresh_buttons()

    #     # return QPixmap.fromImage(qimage.copy())


    def set_points(self):
        self.list_of_images = [self.original_image]
        self.list_of_images_zoom = []

        # Image complète
        new_image = IMAGE()
        new_image.load2(self.original_image.data.copy())

        for point in self.list_of_points:
            new_image.highlight(point, self.colors[point.label])

        self.list_of_images.append(copy.deepcopy(new_image))

        # Image affichée
        if self.count_zoom > 0:
            new_image_zoom = IMAGE()
            new_image_zoom.load2(
                self.original_image.data[
                    self.y_min:self.y_max,
                    self.x_min:self.x_max,
                    :
                ].copy()
            )

            for point in self.list_of_points:
                point_zoom = point.shifted(
                    di=-self.y_min,
                    dj=-self.x_min,
                )
                new_image_zoom.highlight(
                    point_zoom,
                    self.colors[point.label],
                )

            self.list_of_images_zoom.append(new_image_zoom)
            data = new_image_zoom.data

        else:
            data = new_image.data

        data = np.ascontiguousarray(data, dtype=np.uint8)

        h, w, _ = data.shape

        qimage = QImage(
            data.data,
            w,
            h,
            3 * w,
            QImage.Format_RGB888,
        )

        self.refresh_buttons()

        return QPixmap.fromImage(qimage.copy())


    def getPos_ci(self, event):
        """
        Positionnement des points CI.

        1) Récupère les coordonnées (x,y) du clic de l'utilisateur.

        2) Dessine un point bleu où l'utilisateur a cliqué.

        NB : L'utilisateur place un maximum de 3 points.

        Args:
            event (QMouseEvent): Clic de l'utilisateur dans la fenêtre.
        """
        if self.count_ci_points() < 3:
            x, y = self.get_pos_in_widget(event)

            node = POINT(i=y, j=x, label="ci", color=self.color_ci)
            if self.count_zoom > 0:
                node = node.shifted(di=self.y_min, dj=self.x_min)

            self.list_of_points.append(node)

            pixmap = self.set_points()

            self.label.setPixmap(pixmap)
            self.setCentralWidget(self.label)
            self.setCursor(Qt.ArrowCursor)

    @property
    def condition_btn_ci(self):
        return self.count_ci_points() == 3
    
    @property
    def condition_btn_ds(self):
        return self.count_ds_points() == 4

    @property
    def condition_btn_hi(self):
        return self.count_hi_points() == 1

    
    def count_ci_points(self):
        count = 0
        for point in self.list_of_points: 
            if point.label == "ci":
                count+= 1
        return count

    def count_ds_points(self):
        count = 0
        for point in self.list_of_points: 
            if point.label == "ds":
                count+= 1
        return count

    def count_hi_points(self):
        count = 0
        for point in self.list_of_points: 
            if point.label == "hi":
                count+= 1
        return count
    
    def refresh_buttons(self):
        if globals.analysis_level[globals.analysis] == 1:
            self.btn_ci_points.setEnabled(not self.condition_btn_ci)
            self.btn_ds_points.setEnabled(False)
            self.btn_hi_points.setEnabled(False)
            self.btn_done.setEnabled(self.condition_btn_ci)

        if globals.analysis_level[globals.analysis] == 2:
            self.btn_ci_points.setEnabled(not self.condition_btn_ci)
            self.btn_ds_points.setEnabled(not self.condition_btn_ds)
            self.btn_hi_points.setEnabled(False)
            self.btn_done.setEnabled(self.condition_btn_ci and self.condition_btn_ds)

        if globals.analysis_level[globals.analysis] == 3:
            self.btn_ci_points.setEnabled(not self.condition_btn_ci)
            self.btn_ds_points.setEnabled(not self.condition_btn_ds)
            self.btn_hi_points.setEnabled(not self.condition_btn_hi)
            self.btn_done.setEnabled(self.condition_btn_ci and self.condition_btn_ds and self.condition_btn_hi)


    def refresh_image(self):

        source = self.list_of_images_zoom[-1] if self.count_zoom > 0 else self.list_of_images[-1]

        h, w, channels = source.data.shape

        qimage = QImage(
            source.data.tobytes(),
            w,
            h,
            3 * w,
            QImage.Format_RGB888,
        )

        pixmap = QPixmap.fromImage(qimage.copy())
        self.label.setPixmap(pixmap)

    def getPos_ds(self, event):
        """
        Positionnement des points DS.

        1)	Récupère les coordonnées (x,y) du clic de l'utilisateur.

        2)	Dessine un point jaune où l'utilisateur a cliqué.

        NB : L'utilisateur place un maximum de 4 points.
        
        Args:
            event (QMouseEvent): Clic de l'utilisateur dans la fenêtre.
        """
        if self.count_ds_points() < 4:
            x, y = self.get_pos_in_widget(event)

            node = POINT(i=y, j=x, label="ds", color=self.color_ds)
            if self.count_zoom > 0:
                node = node.shifted(di=self.y_min, dj=self.x_min)

            self.list_of_points.append(node)

            pixmap = self.set_points()

            self.label.setPixmap(pixmap)
            self.setCentralWidget(self.label)
            self.setCursor(Qt.ArrowCursor)


    def getPos_hi(self, event):
        """
        Positionnement du point HI.

        1)	Récupère les coordonnées (x,y) du clic de l'utilisateur.

        2)	Dessine un point orange où l'utilisateur a cliqué.
        
        Args:
            event (QMouseEvent): Clic de l'utilisateur dans la fenêtre.
        """
        print("hola, ",  self.count_hi_points())
        if self.count_hi_points() < 1:
            x, y = self.get_pos_in_widget(event)

            node = POINT(i=y, j=x, label="hi", color=self.color_hi)
            if self.count_zoom > 0:
                node = node.shifted(di=self.y_min, dj=self.x_min)

            self.list_of_points.append(node)

            pixmap = self.set_points()

            self.label.setPixmap(pixmap)
            self.setCentralWidget(self.label)
            self.setCursor(Qt.ArrowCursor)


    def cancel(self):
        if self.list_of_points:
            self.list_of_points.pop()

            pixmap = self.set_points()
            self.label.setPixmap(pixmap)

            self.refresh_buttons()


    # def cancel(self):
    #     if self.list_of_points:
    #         self.list_of_points.pop()

    #         pixmap = self.set_points()
    #         self.label.setPixmap(pixmap)

    #         self.refresh_buttons()

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
        self.count_zoom += 1

    def zoom_out(self):
        """
        - Affiche l'image initiale (affichage sans zoom)
        - désactive le bouton 'ZOOM OUT'
        """
        image = IMAGE()
        image.load2(self.list_of_images[-1].data)

        data = np.ascontiguousarray(image.data, dtype=np.uint8)

        hz, wz, channels = image.data.shape

        qimage = QImage(
            data.tobytes(),
            wz,
            hz,
            3 * wz,
            QImage.Format_RGB888,
        )

        pixmap = QPixmap.fromImage(qimage.copy())

        self.label.setPixmap(pixmap)

        self.setCentralWidget(self.label)
    
        cursor = QCursor(Qt.ArrowCursor)
        self.setCursor(cursor)

        self.count_zoom = max(0, self.count_zoom - 1)


    def get_pos_in_widget(self, event):
        """
        Retourne la position du x, y du clic gauhe de la souris.

        Args:
            event (QMouseEvent): Clic de l'utilisateur dans la fenêtre.
        
        Returns:
            tuple[int, int]: Coordonnées x, y de l'endroit du clic.
        """
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

        j_min = max(x-zoom_x//2, 0)
        j_max = min(x+zoom_x//2, self.original_image.data.shape[1])

        i_min = max(y-zoom_y//2, 0)
        i_max = min(y+zoom_y//2, self.original_image.data.shape[0])

        self.x_min = j_min 
        self.y_min = i_min

        self.x_max = j_max
        self.y_max = i_max

        # image_zoom = IMAGE()
        # image_zoom.load2(self.list_of_images[-1].data[i_min:i_max, j_min:j_max, :])
        # data_zoom = np.ascontiguousarray(image_zoom.data, dtype=np.uint8)
        # hz, wz, channels = image_zoom.data.shape
        # qimage_zoom = QImage(
        #     data_zoom.tobytes(),
        #     wz,
        #     hz,
        #     3 * wz,
        #     QImage.Format_RGB888,
        # )
        # self.list_of_images_zoom.append(copy.deepcopy(image_zoom))

        # for point in self.list_of_points:
        #     if point.label == "ci":
        #         color = self.color_ci
        #     elif point.label == "ds":
        #         color = self.color_ds
        #     image_zoom = IMAGE()
        #     image_zoom.load2(self.list_of_images[-1].data[i_min:i_max, j_min:j_max, :])
        #     image_zoom.highlight(point, color=color)
        #     data_zoom = np.ascontiguousarray(image_zoom.data, dtype=np.uint8)
        #     hz, wz, channels = image_zoom.data.shape
        #     qimage_zoom = QImage(
        #         data_zoom.tobytes(),
        #         wz,
        #         hz,
        #         3 * wz,
        #         QImage.Format_RGB888,
        #     )
        #     self.list_of_images_zoom.append(copy.deepcopy(image_zoom))

        # image = IMAGE()
        # image.load2(self.list_of_images[-1].data)

        # data = np.ascontiguousarray(image.data, dtype=np.uint8)


        # h, w, channels = image.data.shape

        # qimage = QImage(
        #     data.tobytes(),
        #     w,
        #     h,
        #     3 * w,
        #     QImage.Format_RGB888,
        # )

        # pixmap_zoom = QPixmap.fromImage(qimage_zoom.copy())

        pixmap_zoom = self.set_points()

        self.label.setPixmap(pixmap_zoom)

        self.setCentralWidget(self.label)
    
        cursor = QCursor(Qt.ArrowCursor)
        self.setCursor(cursor)

        # self.list_of_images.append(image)
        self.refresh_buttons()


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


def text_result_IHM(num_abeille, ci=None, ci_class=None, ds=None, hi=None):
    print("ici", hi)
    unit_ds = "°"
    if ci == None:
        ci = ""
    if ds == None or globals.analysis_level[globals.analysis] < 2:
        ds = ""
        unit_ds = ""
    if hi == None or globals.analysis_level[globals.analysis] < 3:
        hi = ""
    if ci_class == None:
        ci_class = ""

    txt_ci = f"Ci : {ci}"

    txt_class = f"Classe : {ci_class}"

    txt_ds =  f"<span style='color: gray'>DS : {ds}{unit_ds}</span>"
    if globals.analysis_level[globals.analysis] > 1:
        txt_ds = f" Ds : {ds} {unit_ds}"
        
    txt_hi = f"<span style='color: gray'>HI : {hi}</span>"
    if globals.analysis_level[globals.analysis] > 2:
        txt_hi = f" Hi : {hi}"

    return f"<u>Abeille #{num_abeille}</u> <br /> {txt_ci}  <br /> {txt_class} <br /> {txt_ds} <br /> {txt_hi}"