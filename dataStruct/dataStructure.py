from datetime import date

invalidValue = -100

class Measure:
    ''' A measure '''     
    def __init__(self, imageFile):
        self.image = imageFile
        self.treated = False
        self.imageSizePixels = [invalidValue, invalidValue]
        self.cubitalPointsPixels = {"P1": [invalidValue, invalidValue], 
                                    "P2": [invalidValue, invalidValue], 
                                    "P3": [invalidValue, invalidValue]
                                    }
    
        self.discoidalPointsPixels = {"P1": [invalidValue, invalidValue], 
                                      "P2": [invalidValue, invalidValue], 
                                      "P3": [invalidValue, invalidValue], 
                                      "P4": [invalidValue, invalidValue]}
        self.cubitalIndex= -100.
        self.discoidalShift= -100.
        self.comment=""


class Analysis:
    '''This class may at least contains a list of measures'''
    measures = []

    def __init__(self,name):
        self.name = name
        self.date = date.today()
        self.comment = ""
        self.author = ""

    def appendMeasure(self, measure):
        self.measures.append(measure)
        