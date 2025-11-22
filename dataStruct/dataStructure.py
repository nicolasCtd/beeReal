from datetime import date
from pathlib import Path


invalidValuePixel = -100
invalidValueReal = -100.

class Measure:
    ''' A measure '''     
    def __init__(self, imageFile):
        self.image = Path(imageFile)
        self.treated = False
        self.imageSizePixels = [invalidValuePixel, invalidValuePixel]
        self.cubitalPointsPixels = {"P1": [invalidValuePixel, invalidValuePixel], 
                                    "P2": [invalidValuePixel, invalidValuePixel], 
                                    "P3": [invalidValuePixel, invalidValuePixel]
                                    }
    
        self.discoidalPointsPixels = {"P1": [invalidValuePixel, invalidValuePixel], 
                                      "P2": [invalidValuePixel, invalidValuePixel], 
                                      "P3": [invalidValuePixel, invalidValuePixel], 
                                      "P4": [invalidValuePixel, invalidValuePixel]}
        self.cubitalIndex= invalidValueReal
        self.discoidalShift= invalidValueReal
        self.comment=""


class Analysis:
    '''This class may at least contains a list of measures'''
    def __init__(self,name):
        self.name = name
        self.date = date.today()
        self.comment = ""
        self.author = ""
        self.useDiscoidalPoints = False
        self.measures = []

    def updateDate(self):
        self.date = date.today()

    def appendMeasure(self, measure):
        self.measures.append(measure)
        