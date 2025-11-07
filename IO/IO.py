# Add parent folder in sys path for import to work for testing this module as main
if __name__ == '__main__': 
    import sys
    import os
    # Get the parent directory
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    # Add parent directory to sys.path
    sys.path.append(parent_dir)

import xml.etree.ElementTree as ET
from dataStruct import dataStructure as DS
from pathlib import Path
        
AnalysisXmlTag = "Analysis"
MeasureXmlTag = "measure"
MeasuresDictXmlTag = "measures"
ImageXmlTag = "image"
ImageTreatedXmlTag = "treated"

class AnalysisFile:
    def __init__(self, fileName):
        self.filePath = Path(fileName)
        return
    
    def checkImagesExistence(self, analysis):
        for measure in analysis.measures:
            #print(type(measure.image))
            #measure.image.exists()
            print(measure.image, measure.image.exists(), measure.treated)

        return


    def saveAnalysis(self, analysis):
        # creating root element
        root = ET.Element(AnalysisXmlTag)
        # Add attributes
        for attr, value in analysis.__dict__.items():
            if (attr!=MeasuresDictXmlTag):
                child = ET.SubElement(root, attr)
                child.text = str(value)

        for measure in analysis.measures:
            measureElement = ET.SubElement(root, MeasureXmlTag)
            for attr, value in measure.__dict__.items():
                child = ET.SubElement(measureElement, attr)
                toto = str(value)
                child.text = str(value)

        # Construct tree
        tree = ET.ElementTree(root)
        ET.indent(tree, space="\t", level=0)

        # Write to the file
        tree.write(self.filePath, encoding="utf-8", xml_declaration=True)
        return

    def loadAnalysis(self):
        # TODO: check existence of the file
        # TODO: Check if the parsing turns well
        # TODO: Check if image are on disk. Reject if not ?

        if (not self.filePath.exists()):
            print("Analysis file does no exists")
            return
            

        tree = ET.parse(self.filePath)
        root = tree.getroot()
        analysis = DS.Analysis("")

        for child in root:
            if child.tag == MeasureXmlTag:                
                # This is a measure
                measure = DS.Measure("")
                for measureNode in child:
                    if measureNode.tag==ImageXmlTag:                        
                        setattr(measure, measureNode.tag, Path(measureNode.text) )
                    elif measureNode.tag==ImageTreatedXmlTag:
                        imageTreated = True
                        if (measureNode.text == "False"):
                            imageTreated = False
                                                        
                        setattr(measure, measureNode.tag, imageTreated )
                    else:
                        setattr(measure, measureNode.tag, measureNode.text )

                analysis.measures.append(measure)
            else:
                setattr(analysis, child.tag, child.text )

        # Check image existence
        self.checkImagesExistence(analysis)

        return analysis
    
if __name__ == '__main__':  

    '''Define main test function: Doing so also avoid declaring module global variables'''
    def mainTest():
        analysis = DS.Analysis("testAnalysis")
        analysis.appendMeasure(DS.Measure("bee1.png"))
        analysis.appendMeasure(DS.Measure("bee2.png"))
        analysis.appendMeasure(DS.Measure("bee3.png"))
        analysis.appendMeasure(DS.Measure("bee4.png"))
        analysis.measures[2].treated= True
        analysis.measures[3].treated= True
        analysis.author = "Jerem"
        analysis.comment="Bzzzzzz! A very nice analysis"
        analysisFile = AnalysisFile("analysisTestFile.xml")

        # Saving
        analysisFile.saveAnalysis(analysis)

        #return

        # Loading 
        loadedAnalysis = analysisFile.loadAnalysis()

        print(loadedAnalysis.name, loadedAnalysis.date, loadedAnalysis.measures[3].image)
        print("finished")

    # launch the tests
    mainTest()



    