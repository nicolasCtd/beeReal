import numpy as np
import matplotlib.pyplot as plt
import logging

def get_zoom_center(file):
    """
    Extrait les bornes spatiales xmin, xmax, ymin, ymax à partir du nom du fichier.
    
    Le nom du fichier doit contenir 
    """
    xmin, xmax, ymin, ymax = 0, 0, 0, 0
    if "zoom" not in file:
        print("Erreur : cette image n'est pas un zoom")
    else:
        a = file.find("xmin")
        b = file.find("xmax")
        c = file.find("ymin")
        d = file.find("ymax")
        e = file.find("end")

        xmin=int(file[a+4:b])
        xmax=int(file[b+4:c])
        ymin=int(file[c+4:d])
        ymax=int(file[d+4:e])
    return xmin, xmax, ymin, ymax

def sort_ci_points(nodes):
    nodes_ordered = list()
    if len(nodes) != 3:
        print("Erreur : le nombre de points CI devrait être égal à 3")
    else:
        # sort the 3 points from left to right 
        order = np.array(np.argsort(np.array([nodes[0].j, nodes[1].j, nodes[2].j])), dtype=int)
        for i in range(3):
            nodes_ordered.append(nodes[order[i]])
    return nodes_ordered

def sort_ds_points(nodes):
    nodes_ordered = list()
    if len(nodes) != 4:
        print("Erreur : le nombre de points DS devrait être égal à 4")
    else:
        idx = np.argmax([nodes[0].i, nodes[1].i, nodes[2].i, nodes[3].i])
        DS = nodes[idx]
        nodes.remove(nodes[idx])
        # sort the 3 points from left to right 
        order = np.array(np.argsort(np.array([nodes[0].j, nodes[1].j, nodes[2].j])), dtype=int)
        for i in range(3):
            nodes_ordered.append(nodes[order[i]])
        nodes_ordered.append(DS)
    return nodes_ordered

def compute_cubital_index(ci_points):
    """
    Calcul de l'indice cubital.

    Args:
        ci_points (list[POINT, POINT, POINT]): Liste des 3 points CI.
    """
    n0 = ci_points[0]
    n1 = ci_points[1]
    n2 = ci_points[2]
    a = DROITE(n0, n1).distance
    b = DROITE(n1, n2).distance
    return a/b

def compute_discoidal_shift(point1, point2, ds_points):
    """
    Calcul du décalage discoidal.
    
    Args:
        ds_points (list[POINT, POINT, POINT, POINT]): Liste des 4 points DS.
        point1 (POINT): Point appartenant à la droite perpendiculaire à la cellule radiale.
        point2 (POINT): Deuxième point appartenant à la droite perpendiculaire à la cellule radiale.
    
    Returns:
        float: Décalage discoidal.
    """
    U = DROITE(point1, point2)
    V = DROITE(ds_points[1], ds_points[3])
    dot = U.nX * V.nX + U.nY * V.nY
    delta = ds_points[3].j - U.get_x(ds_points[3].i)
    return np.sign(delta) *  np.arccos(dot/(U.distance * V.distance)) * 180/np.pi

class IMAGE():
    """Classe permettant de charger et editer une image."""
    def __init__(self):
        """
        Attributes:
            name (str): Nom de l'image.
            data (np.array[nb_lignes, nb_colonnes, 3]): Valeurs des pixels de l'image RGB.
            nb_lignes (int): Nombre de lignes de l'image.
            nb_col (int): Nombre de colonnes de l'image.
        """
        self.name = ''
        self.data = np.array([])
        self.nb_lignes = 0
        self.nb_col = 0
        self.ci_points = list()
        self.ds_points = list()
    
    def load(self, path):
        """
        Charge une image depuis un fichier.

        Args:
            path (str): Chemin absolu de l'image.
        
        Attributes:
            nb_lignes (int): Nombre de lignes dans l'image.
            nb_lignes (int): Nombre de colonnes dans l'image.
            data (np.array[nb_lignes, nb_col, 3]): Valeurs des pixels de l'image RGB.
        """
        self.name = path
        self.data = np.copy(plt.imread(path))
        if self.data.ndim == 2:    #image grayscale
            self.data = np.stack((self.data,)*3, axis=-1)   # convert to RGB
        self.nb_lignes = self.data.shape[0]
        self.nb_col = self.data.shape[1]
        
    def highlight(self, node, color, rayon=5):
        """
        Place un point de couleur sur l'image.

        Args:
            node (POINT): Point dans l'image.
            color (tuple[int, int, int]): Couleur RGB du point.
            rayon (int): Taille en pixels du rayon du point.
        """
        y, x = np.meshgrid(np.arange(self.nb_col), np.arange(self.nb_lignes))
        dot_ci = (np.sqrt(np.abs(node.i - x)**2 + np.abs(node.j-y)**2) <= rayon) * 1
        idx_ci_i, idx_ci_j = np.where(dot_ci == 1)
        # Color the point that has been identified
        for i, j in zip(idx_ci_i, idx_ci_j):
            self.data[i, j][0] = color[0]
            self.data[i, j][1] = color[1]
            self.data[i, j][2] = color[2]
    
    def draw_ci_lines(self, clr):
        """
        Trace deux segments (par défaut en bleu) qui relient les 3 points CI.
        
        Args:
            clr (tuple[int, int, int]): Couleur des segments.
        """
        DROITE(self.ci_points[0], self.ci_points[1]).draw(self, 2, 2, color=clr)
        DROITE(self.ci_points[1], self.ci_points[2]).draw(self, 2, 2, color=clr)
    
    def draw_ds_line_02(self, clr):
        """
        Trace le segment qui relie les deux extrémités de la cellule radiale (par défaut en jaune).
        
        Args:
            clr (tuple[int, int, int]): Couleur du segment.
        """
        DROITE(self.ds_points[0], self.ds_points[2]).draw(self, 2, 2, color=clr)
    
    def draw_ds_line_02_perpendicular(self, clr):
        """
        Trace la ligne perpendiculaire aux extrémités de la cellule radiale et passant
        par le point DS situé au centre/bas de la cellule radiale.
        
        Args:
            clr (tuple[int, int, int]): Couleur de la ligne.
        
        Attributes:
            point1 (POINT): Point n°1 appartenant à la droite perpendiculaire à la cellule radiale
            point2 (POINT): Point n°2 appartenant à la droite perpendiculaire à la cellule radiale
        """
        point_ds_line_02_perp_1 = POINT()
        point_ds_line_02_perp_2 = POINT()
        x, y = DROITE(self.ds_points[0], self.ds_points[2]).xy
        dot_product = np.ones(x.size)
        for pixel in range(x.size):
            u = (self.ds_points[2].j - self.ds_points[0].j, self.ds_points[2].i - self.ds_points[0].i)
            v = (x[pixel] - self.ds_points[1].j, y[pixel] - self.ds_points[1].i)
            dot_product[pixel] = u[0] * v[0] + u[1] * v[1]
        idx = int(np.argmin(np.abs(dot_product)))
        Pyy, Pxx = y[idx], x[idx]

        # look for another pixel (point1) in this area that minimizes the dot product
        square = 20
        dot_product = np.ones((self.nb_lignes, self.nb_col)) * 1000
        for dY in np.arange(0, int(1.5*square)):
            for dX in np.arange(-square, +square+1):
                Py_test, Px_test = Pyy - dY, Pxx - dX
                u = (self.ds_points[2].j - self.ds_points[0].j, self.ds_points[2].i - self.ds_points[0].i)
                v = (Px_test - self.ds_points[1].j, Py_test - self.ds_points[1].i)
                dot_product[Py_test, Px_test] = u[0] * v[0] + u[1] * v[1]
        Py, Px = np.where(np.abs(dot_product) == np.min(np.abs(dot_product)))

        if len(Py)>1:
            txt = "draw_ds_line_02_perpendicular(): la recherche + précise d'un autre pixel "
            txt += "appartenant à la droite perpendiculaire à la première n'a pas marché"
            logging.info(txt)
            Py, Px = Pyy, Pxx

        point_ds_line_02_perp_1.i = Py
        point_ds_line_02_perp_1.j = Px
        point_ds_line_02_perp_1.color = self.ds_points[0].color
        # Now find another point far from the second DS point but in the same alignment
        distance_ref = 0.8 * DROITE(self.ds_points[0], self.ds_points[2]).distance
        small_line = DROITE(point_ds_line_02_perp_1, self.ds_points[1])
        x = np.arange(self.nb_col)
        y = small_line.get_y(x)
        x = x[y>0]
        y = y[y>0]
        distance = np.sqrt((x - point_ds_line_02_perp_1.j) **2 + (y - point_ds_line_02_perp_1.i) ** 2)
        delta = np.abs(distance - distance_ref)
        idx = int(np.where(delta == np.min(delta))[0][0])
        point_ds_line_02_perp_2.i = int(y[idx])
        point_ds_line_02_perp_2.j = int(x[idx])
        DROITE(point_ds_line_02_perp_1, point_ds_line_02_perp_2).draw(self, 2, 5, color=clr)
        self.point1 = point_ds_line_02_perp_1
        self.point2 = point_ds_line_02_perp_2
        
    
class POINT():
    """Représente un point avec des coordonnées et une couleur"""
    def __init__(self):
        """
        Attributes:
            i (int): Numéro de ligne du pixel au centre du point (coordonnée y).
            j (int): Numéro de colonne du pixel au centre du point (coordonnée x).
            color (tuple[int, int, int]): Couleur du point.
        """
        self.i = 0
        self.j = 0
        self.color = (0, 0, 255)
    
    def __str__(self) -> str:
        print(f"i : {self.i}")
        print(f"j : {self.j}")


class DROITE():
    """
    Représente une droite définie par 2 points.

    La droite est construite à partir de deux instances de POINT, P1 et P2. Elle calcule le coefficient
    directeur et l'ordonnée à l'origine, génère les coordonnées discrètes (x, y) de la droite, et peut 
    être tracée sur une image via draw().
    """
    
    def __init__(self, P1, P2):
        """
        Args:
            P1 (POINT): Point n°1
            P2 (POINT): Point n°2
        
        Attributes:
            color ([int, int, int]): Couleur
            P1 (POINT): Point n°1
            P2 (POINT): Point n°2
        
        Calls:
            coefficients()
            coords_xy()
            distance_P1_P2()
            vecteur_P1_P2()
        """
        self.color = P1.color
        self.P1 = P1
        self.P2 = P2
        self.coefficients()
        self.coords_xy()
        self.distance_P1_P2()
        self.vecteur_P1_P2()

    def coefficients(self):
        """
        Calcul des coefficients de la droite (pente, offset).

        Attributes:
            slope (float): Pente.
            offset (float): Offset.
            coeffs (tuple[float, float]): Pente, Offset.
        """
        if np.abs(self.P2.j - self.P1.j) > 0:
            slope = (self.P2.i - self.P1.i) / (self.P2.j - self.P1.j)
        else:
            slope = (self.P2.i - self.P1.i) / (self.P2.j+1 - self.P1.j)
        offset = self.P1.i - slope * self.P1.j
        self.slope = slope 
        self.offset = offset
        self.coeffs = (slope, offset)
        return slope, offset

    def coords_xy(self):
        """
        Calcul des coordonnées discrètes (x, y) de la droite dans l'image.

        Attributes:
            x (list): Liste des coordonnées x (indices colonne dans l'image).
            y (list): Liste des coordonnées y (indices ligne dans l'image).
        """
        if np.abs(self.P1.j - self.P2.j) > np.abs(self.P1.i - self.P2.i):
            x = np.arange(self.P1.j, self.P2.j+1, step=np.sign(self.P2.j - self.P1.j))
            y = self.get_y(x)
        else:
            y = np.arange(self.P1.i, self.P2.i+1)
            x = self.get_x(y)
        self.x = x 
        self.y = y
        self.xy = x, y
        return x, y

    def draw(self, image, dx, dy, color):
        """
        Dessine une droite sur l'image.

        Args:
            image (IMAGE): Image d'aile
            dx (int): Largeur du trait.
            dy (int): Hauteur du trait.
            color (tuple[int, int, int]): Couleur RGB.
        
        Uses:
            self.x (np.ndarray): Abscisses des points de la droite.
            self.y (np.ndarray): Ordonnées des points de la droite.
        """
        for i in range(self.x.size):
            for g in range(-dy//2, +dy//2+1):
                for h in range(-dx//2, +dx//2+1):
                    image.data[self.y[i]+g, self.x[i]+h][0] = color[0]
                    image.data[self.y[i]+g, self.x[i]+h][1] = color[1]
                    image.data[self.y[i]+g, self.x[i]+h][2] = color[2]

    def distance_P1_P2(self):
        """
        Calcul de la distance entre les points P1 et P2.

        Attributes:
            distance (float): Distance entre les P1 et P2 en pixels.
        
        Uses:
            P1 : point 1
            P2 : point 2
        """
        distance = np.sqrt(np.abs(self.P2.i - self.P1.i) ** 2 + np.abs(self.P2.j - self.P1.j) ** 2)
        self.distance = distance
        return distance

    def get_y(self, x):
        """
        Calcul des coordonnées y connaissant x, la pente 'slope' et l'offset  : y = slope * x + offset.

        Uses:
            slope : pente
            offset : ordonnée à l'origine

        Returns:
            Coordonnées y.
        """
        return np.int32(self.slope * x + self.offset)
    
    def get_x(self, y):
        """
        Calcul des coordonnées x connaissant y, la pente 'slope' et l'offset  : y = slope * x + offset.

        Uses:
            slope : pente
            offset : ordonnée à l'origine

        Returns:
            Coordonnées x.
        """
        return np.int32((y - self.offset) / self.slope)
    
    def vecteur_P1_P2(self):
        """
        Calcul du vecteur P1P2 (delta x, delta y)

        Attributes:
            nX (int): Différence des coordonnées x (P2.j - P1.j).
            nY (int): Différence des coordonnées y (P2.i - P1.i).
        """
        self.nX = self.P2.j - self.P1.j
        self.nY = self.P2.i - self.P1.i