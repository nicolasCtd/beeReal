import xml.etree.ElementTree as ET
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
        return

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
        ET.indent(tree, space="\t", level=0)

        # write to the file
        tree.write(self.fileName, encoding="utf-8", xml_declaration=True)
        return

    def loadAnalysis(self):
        return
    
if __name__ == '__main__':
    analysis = Analysis("testAnalysis")

    analysis.appendMeasure(Measure("bee1.png"))
    analysis.appendMeasure(Measure("bee2.png"))
    analysis.appendMeasure(Measure("bee3.png"))
    analysis.appendMeasure(Measure("bee4.png"))
    analysisFile = AnalysisFile("analysis1.xml")

    # Saving
    analysisFile.saveAnalysis(analysis)

    # Loading 




    