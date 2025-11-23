# coding: utf-8

import numpy as np
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
from datetime import datetime
import yaml
# from .utile import gauss
from scipy.stats import pearsonr
from matplotlib.ticker import MultipleLocator
import logging
from scipy.spatial import procrustes



warnings.filterwarnings('ignore') 

mpl.use('TkAgg')

dpi = 160
HEIGHT = 870
WIDTH = 670

class HISTOGRAM():
    def __init__(self, indices, id_bees, path, visu="RUTTNER", save_abacus=1):
        self.path=path
        self.visu = visu
        self.id_bees=id_bees
        self.indices = indices
        self.classes = self.get_classes(indices)
        self.limits = {'carnica':[2.3, 3.2],
                       'ligustica':[2, 2.8],
                       'caucasica': [1.7, 2.3],
                       'mellifera':[1.4, 2.1]}
        self.mclc = {'carnica':0,
                       'ligustica':0,
                       'caucasica': 0,
                       'mellifera':0}
        if save_abacus:
            self.save_abacus()

    
    def save_abacus(self):
        classes, indices = self.compute_abacus()
        with open(os.sep.join([self.path, f"abacus_{self.visu}.txt"]), "w") as f:
            for classe, indice in zip(classes, indices):
                f.write(str(indice) + " " + str(classe) + "\n")
        return 0
        
    def histogram(self):
        y = list()
        x = list()
        for i in range(1, 25):
            y.append(self.classes.count(i))
            x.append(i)
        self.x = x
        self.y = y
        return x, y

    def compute_abacus(self):
        if self.visu == "DREHER":
            delta = 100 / 50
        elif self.visu == "RUTTNER":
            delta = 100 / 60

        CLASSES = list()
        INDICES = list()
        for i in range(-5, 20):
            a = 50 + i * delta 
            b = 50 - i * delta 
            CLASSES.append(6 + i)
            INDICES.append(int(a/b*1000)/1000)

        return CLASSES, INDICES

    def get_classes(self, indices):
        CLASSES, INDICES = self.compute_abacus()
        CL = CLASSES[:-1]
        CI_min = INDICES[:-1]
        CI_max = INDICES[1:]

        classes = list()
        for indice in indices:
            for i in range(len(CL)):
                if (indice >= CI_min[i]) and (indice < CI_max[i]):
                    classes.append(CL[i])
                    break
        return classes

    def MCLC(self):
        X = np.array(self.x)
        Y = np.array(self.y)
        
        E = Y.sum()

        coeffs = dict()
        somme = 0

        for espece in self.limits.keys():

            classes = self.get_classes(self.limits[espece])
            cmin, cmax = classes[0], classes[1]
            select = (X >= cmin) & (X <=cmax)

            Xnorm = X[select]
            Ynorm = Y[select] / Y[select].sum()
            Ynorm[0] = 0
            Ynorm[-1] = 0
            sigma = (cmax - cmin )/6
            mu = (cmax + cmin)/2

            normal = gauss(Xnorm, mu, sigma)
            coeff, _ = pearsonr(normal, Ynorm)
            coeff = coeff * Y[select].sum() / E

            if coeff < 0:
                coeff = 0
            coeffs[espece] = coeff
            somme += coeff

            try:
                COEF = int(coeff*100)/100
            except:
                COEF="NaN"

            f = plt.figure()
            plt.plot(Xnorm, Ynorm, "-*", label="mesures")
            plt.plot(Xnorm, normal, "-*", label="fit gauss")
            plt.title(f"{espece}. Coeff correlation: {COEF}")
            # plt.savefig(f"{self.path}debug_coeff_correlation_{espece}.png")
            plt.close()
        
        try:
            C1 = int(coeffs['mellifera'] / somme * 100)
            C2 = int(coeffs['caucasica'] / somme * 100)
            C3 = int(coeffs['ligustica'] / somme * 100)
            C4 = int(coeffs['carnica'] / somme * 100)
        except:
            C1 = 0
            C2 = 0
            C3 = 0
            C4 = 0

        MELLIFERA = C1
        CAUCASICA = C2
        LIGUSTICA = C3
        CARNICA = C4

        if MELLIFERA>0:
            MELLIFERA+=1
        else:
            if CAUCASICA>0:
                CAUCASICA += 1

        if LIGUSTICA>0:
            LIGUSTICA+=1
        else:
            if CARNICA>0:
                CARNICA += 1

        self.mclc = {'mellifera':min(100, MELLIFERA), 'caucasica':min(100, CAUCASICA), 'ligustica':min(100, LIGUSTICA), 'carnica':min(100, CARNICA)}
        print(self.mclc)

        return 0

    def reset_ticks(self, ax):
        tck_label = list()
        position = list()
        for tick in ax.get_yticklabels():
            
            if "−" in tick.get_text():
                tck_label.append("")
                position.append(tick.get_position()[1])
            else:
                if tick.get_position()[1] == int(tick.get_position()[1]):
                    tck_label.append(tick.get_text())
                    position.append(int(tick.get_position()[1]))

        ax.set_yticks(position, tck_label)
        cl, idx = self.compute_abacus()
        xticks = []
        for i in range(len(idx)):
            xticks.append(str(int(idx[i]*100)/100))
        
        ax.set_xticks(np.arange(1, 26), xticks, fontsize=6)

        ax.xaxis.set_major_locator(MultipleLocator(1))
        # ax.xaxis.set_minor_locator(MultipleLocator(0.5))

        return tck_label, position


    def plot_histogram(self, add_plot=False, id_bees_add=[], indices_add=[], legend="", show=True, save=True):

        x, y = self.histogram()
        # self.MCLC()
        mean_of_classes = np.sum((np.array(x)+0.5) * np.array(y)) / np.sum(np.array(y))

        print(f"indice cubital moyen : {int(np.mean(self.indices) * 100)/100}")
        print(f"moyenne des classes : {int(mean_of_classes * 100)/100}")
        print("\n")

        alpha = 0.5
        colors = ['aquamarine', 'khaki', 'silver', 'thistle']

        figures_out = list()

        for espece, m in zip(self.limits.keys(), range(4)):

            plt.figure(m, figsize=(HEIGHT/dpi, WIDTH/dpi), dpi=dpi)

            fig = plt.gcf()
            ax = plt.gca()
            # fig.set_size_inches((16*0.9, 9*0.9))

            plt.plot(np.array(x)+0.5, y, label=f"Bee Real ({len(self.indices)} bees)", linewidth=3.5, zorder=5)

            tck_label, positions = self.reset_ticks(ax)
            plt.ylim(0, max(positions))

            for i in range(0, 24):
                ax.axvline(i, color='black', linewidth=0.5, zorder=0)
            
            for classe in np.arange(6, 24):
                plt.text(classe+0.3, 0.15, str(classe), color='black', fontsize=7, fontweight='bold', zorder=30)

            plt.vlines(mean_of_classes+0.5, 0, max(positions), color='black', linewidth=1.5, linestyle="--", zorder=6)

            cmin = int(self.get_classes([self.limits[espece][0]])[0])
            cmax = int(self.get_classes([self.limits[espece][1]])[0])
            xx = range(cmin, cmax +1)
            yy1 = np.zeros(cmax - cmin + 1)
            yy2 = float(plt.gca().get_yticks()[-1])

            plt.fill_between(xx, yy1, yy2, color=colors[m], alpha=alpha, zorder=2)
            # plt.text(cmin + (cmax - cmin)/3, max(positions)-1.5, espece + f"\n     {self.mclc[espece]}%", fontsize=12, style='italic', zorder=10)
            plt.text(cmin + (cmax - cmin)/3, 3/4*max(positions), espece, fontsize=12, style='italic', zorder=10)
            plt.text(mean_of_classes+0., 2, f'Mean of indices : {int(np.mean(self.indices) * 100)/100}', 
                     fontstyle='italic', fontweight='light', fontsize=8, zorder=20)
        
            # plt.title(f"Histogramme de l'indice cubital (classification {self.visu})", fontweight='bold', fontsize='xx-large')
            plt.xticks(rotation=45)
            # plt.xlabel("Indice", fontsize='x-large', fontweight='light')
            plt.xlabel("Cubital index (-)", fontsize=10, fontweight='light')
            # plt.ylabel("Nombre d'abeilles", fontsize='x-large', fontweight='light')
            plt.ylabel("Number of bees", fontsize=10, fontweight='light')
            plt.legend(loc='upper left', fontsize=10)
            #plt.tight_layout()
            plt.grid()
            PATH = f"{self.path}{os.sep}{3-m}_histogramme_{self.visu}_{espece}.png"
            figures_out.append(PATH)
            ax.set_xlim(6, 26)
            ax.tick_params(axis='y', labelsize=8)

            if add_plot:
                H = HISTOGRAM(indices=indices_add, id_bees=id_bees_add, visu=self.visu, path="", save_abacus=False)
                x_add_histo, y_add_histo = H.histogram()

                PATH = f"{self.path}{os.sep}{3-m}_histogramme_{self.visu}_{espece}_DEEPWINGS.png"
                figures_out.append(PATH)
                plt.plot(np.array(x_add_histo)+0.5, y_add_histo, color='red', label=legend)
                plt.legend(loc='upper left')

                mean_of_classes_add = np.sum((np.array(x_add_histo)+0.5) * np.array(y_add_histo)) / np.sum(np.array(y_add_histo))
                plt.text(mean_of_classes_add+0., 2.5, f'Mean of indices : {int(np.mean(indices_add) * 100)/100}', 
                     fontstyle='italic', fontweight='light', color='red', fontsize=8, zorder=20)

                ax = plt.gca()
                tck_label, positions = self.reset_ticks(ax)

                plt.ylim(0, 1.2*max(positions))
                ax.set_xlim(6, 26)
                ax.tick_params(axis='y', labelsize=8)

            if show:
                plt.show()
    
            if save:
                plt.savefig(PATH, dpi=dpi)
            
            plt.close()

        return figures_out

    def scatter_plot(self, path, indices=list(), shifts=list(), id_bees=list(), id_bees_add=list(), add_plot=False, x_add=list(), y_add=list(), name_fig="", title=""):
        
        fig, ax = plt.subplots(figsize=(HEIGHT/dpi, WIDTH/dpi), dpi=dpi)
        #fig.set_size_inches((16*0.5, 9*0.7))
    #
        # colors = ["blue", "red", "black"]

        # for INDICES, SHIFTS, COL, LEG in zip(indices, shifts, colors, legends):
        #     plt.plot(INDICES, SHIFTS, "*", color=COL, label=LEG, markersize=10)

        indices = np.array(indices)
        shifts = np.array(shifts)

        xmax = 3
    
        abeilles_noires = (indices < 2.05) &  (indices > 1) & (shifts < 0.1)
        autres_abeilles = ~(abeilles_noires)

        ratio = int(len(indices[abeilles_noires])/indices.size*100)

        plt.plot(indices[abeilles_noires], shifts[abeilles_noires], "*", 
                color="black", markersize=8, 
                label=f"Black bees: {len(indices[abeilles_noires])}/{indices.size} ({ratio}%)")
        
        plt.plot(indices[autres_abeilles], shifts[autres_abeilles], "*", color="blue", markersize=8)

        if add_plot:
            plt.plot(x_add, y_add, "^", color="red", markersize=3)

            # # Transformer en matrices Nx2
            # A = np.column_stack((indices, x_add))
            # B = np.column_stack((shifts, y_add))

            # mtx1, mtx2, disparity = procrustes(A, B)
            # print("Disparité Procrustes (0 = identique) :", disparity)
            # print(id_bees)
            # print("--")
            # print(id_bees_add)
            # print("X")
            # print(indices)
            # print("x4")
            # print(x_add)
            # print("Y")
            # print(shifts)
            # print("Y'")
            # print(y_add)

        # add bee number on the graph
        for i in range(len(id_bees)):
            if autres_abeilles.squeeze()[i] or abeilles_noires.squeeze()[i]:
            # plt.text(indices[autres_abeilles][i], shifts[autres_abeilles][i], id_bees[autres_abeilles.squeeze()][i])
                plt.text(indices.squeeze()[i], shifts.squeeze()[i], id_bees[i], fontsize=8)

        for i in range(len(x_add)):
            plt.text(x_add[i], y_add[i], id_bees_add[i], fontsize=7, color='red')

        ax = plt.gca()
        ax.fill_between([1, 2], [-np.max(np.abs(shifts)), -np.max(np.abs(shifts))], color='grey', alpha=0.5)
        ax.tick_params(axis='x', labelsize=8)
        ax.tick_params(axis='y', labelsize=8)

        #plt.ylim([-np.max(np.abs(shifts)), +np.max(np.abs(shifts))])
        plt.ylim([-2*np.std(shifts), +2*np.std(shifts)])
        plt.xlim([1, xmax])

        # mean = np.mean(indices)
        # std = np.std(indices)
        plt.xlim([1, xmax])
        plt.axhline(0, color="darkgrey", linewidth=5, zorder=0)
        plt.axvline(2, color="darkgrey", linewidth=5, zorder=0)
        plt.grid()
        # plt.ylabel("Transgression discoïdale (°)", fontweight='bold', fontsize=14)
        plt.ylabel("Discoïdal shift (°)", fontsize=10, fontweight='light')
        # plt.xlabel("Indice cubital (-)", fontweight='bold', fontsize=14)
        plt.xlabel("Cubital index (-)", fontsize=10, fontweight='light')
        #plt.tight_layout()
        # plt.title(title)
        plt.legend()
        if name_fig != "":
            name_fig = "_" + name_fig
        ds_image = f"{path}{os.sep}scatter_plot{name_fig}.png"
        if add_plot:
            ds_image = f"{path}{os.sep}scatter_plot{name_fig}_deepwings.png"
        plt.savefig(ds_image, dpi=dpi)
        # plt.show()
        plt.close()
        return ds_image

def analyse(indices, shifts, id_bees, visu="RUTTNER", path_out=""):

    H = HISTOGRAM(indices=indices, id_bees=id_bees, visu=visu, path=path_out)

    list_of_ci_images = H.plot_histogram(show=False, save=True)

    ds_image = H.scatter_plot(path=path_out, id_bees=id_bees, indices=[indices], shifts=[shifts])

    return list_of_ci_images, ds_image, H

def analyse2(indices, shifts, id_bees, indices_add, shifts_add, id_bees_add, LEG="", visu="RUTTNER", path_out=""):
    
    H = HISTOGRAM(indices=indices, id_bees=id_bees, visu=visu, path=path_out)
    
    list_of_ci_images = H.plot_histogram(add_plot=True, id_bees_add=id_bees_add, indices_add=indices_add, 
                                         legend=LEG, show=False, save=True)

    ds_image = H.scatter_plot(indices=indices, shifts=shifts, add_plot=True, x_add=indices_add, y_add=shifts_add, 
                              id_bees=id_bees, id_bees_add=id_bees_add, path=path_out, name_fig="add_plot")

    return list_of_ci_images, ds_image, H


if __name__ == '__main__':
    with open('config.yml', 'r') as file:
        data = yaml.safe_load(file)
    