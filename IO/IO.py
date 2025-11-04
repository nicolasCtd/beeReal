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
        
AnalysisXmlTag = "Analysis"
MeasureXmlTag = "measure"

class AnalysisFile:
    def __init__(self, fileName):
        self.fileName = fileName
        return
    
    def saveAnalysis(self, analysis):
        # creating root element
        root = ET.Element(AnalysisXmlTag)
        # Add attributes
        for attr, value in analysis.__dict__.items():
            child = ET.SubElement(root, attr)
            child.text = str(value)

        for measure in analysis.measures:
            measureElement = ET.SubElement(root, MeasureXmlTag)
            for attr, value in measure.__dict__.items():
                child = ET.SubElement(measureElement, attr)
                child.text = str(value)

        # Construct tree
        tree = ET.ElementTree(root)
        ET.indent(tree, space="\t", level=0)

        # Write to the file
        tree.write(self.fileName, encoding="utf-8", xml_declaration=True)
        return

    def loadAnalysis(self):
        # TODO: check existence of the file
        # TODO: Check if the parsing turns well
        # TODO: Check if image are on disk. Reject if not ?

        tree = ET.parse(self.fileName)
        root = tree.getroot()
        analysis = DS.Analysis("")

        for child in root:
            if child.tag != MeasureXmlTag:
                setattr(analysis, child.tag, child.text )
            else:
                # This is a measure
                measure = DS.Measure("")
                for measureNode in child:
                    setattr(measure, measureNode.tag, measureNode.text )
                analysis.measures.append(measure)

        return analysis
    
if __name__ == '__main__':  

    analysis = DS.Analysis("testAnalysis")

    analysis.appendMeasure(DS.Measure("bee1.png"))
    analysis.appendMeasure(DS.Measure("bee2.png"))
    analysis.appendMeasure(DS.Measure("bee3.png"))
    analysis.appendMeasure(DS.Measure("bee4.png"))
    analysisFile = AnalysisFile("analysis1.xml")

    # Saving
    analysisFile.saveAnalysis(analysis)

    # Loading 
    loadedAnalysis = analysisFile.loadAnalysis()

    print(loadedAnalysis.name, loadedAnalysis.date, analysis.measures[3].image)
    

    print("finished")



    