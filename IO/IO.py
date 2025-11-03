import xml.etree.ElementTree as ET
from datetime import date

invalidValue = -100

class Measure:
    ''' A measure '''
     
    def __init__(self):
        self.image = "image"
        self.image = ""
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
        return


class Analysis:
    '''This class may at least contains a list of measures'''
    name=""
    date = None
    measures = []
    
    def __init__(self,name):
        self.name = name
        self.date=date.today()

    def appendMeasure(self, measure):
        self.measures.append(measure)
        

class AnalysisFile:
    def __init__(self, fileName):
        self.fileName = fileName
        return
    
    def saveAnalysis(self, analysis):
        # creating root element
        root = ET.Element("Analysis")
        # Ajout des attributs (ou sous-éléments)
        for attr, value in analysis.__dict__.items():
            child = ET.SubElement(root, attr)
            child.text = str(value)

        for measure in analysis.measures:
            measureElement = ET.SubElement(root, "measure")
            for attr, value in measure.__dict__.items():
                child = ET.SubElement(measureElement, attr)
                child.text = str(value)

        # Construction tree
        tree = ET.ElementTree(root)

        # write to the file
        tree.write(self.fileName, encoding="utf-8", xml_declaration=True)
        return

    def loadAnalysis(self):
        return
    
if __name__ == '__main__':
    analysis = Analysis("testAnalysis")
    print(analysis.date)
    measure = Measure()

    for attr, value in measure.__dict__.items():
        print(value)

    analysis.appendMeasure(measure)
    analysis.appendMeasure(measure)
    analysis.appendMeasure(measure)
    analysis.appendMeasure(measure)
    analysisFile = AnalysisFile("toto.xml")

    # Saving
    analysisFile.saveAnalysis(analysis)

    # Loading 




    