from PyQt5.QtWidgets import QWidget
from ui import AnalysisSettingForm_ui as ui
from dataStruct import dataStructure as DS

class AnalysisSettingForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui.Ui_AnalysisSettingForm()
        self.ui.setupUi(self)
        self.initialize()

    def initialize(self):
        self.ui.cubitalCheckBox.setText("Use cubital points")
        self.ui.discoidalCheckBox.setText("Use discoidal points")
        self.ui.startAnalysisPushButton.setText("Start analysis")
        self.ui.analysisNameLabel.setText("Analysis name")
        self.ui.authorNameLabel.setText("Author")
        self.ui.commentLabel.setText("Comments")
        self.ui.inputImagelabel.setText("Input images")
        self.ui.treatedImageLael.setText("Treated images")

    def populateFromAnalysis(self, analysis : DS):        

        self.ui.nameLineEdit.setText(analysis.name)
        self.ui.authorLineEdit.setText(analysis.author)
        self.ui.commentsTextEdit.setText(analysis.comment)

        for measure in analysis.measures:
            imagePath = str(measure.image)
            print(measure.image, measure.treated)
            if measure.treated:
                self.ui.treatedWingListWidget.addItem(imagePath)
            else:
                self.ui.nonTreatedWingListWidget.addItem(imagePath)


        # and so on ...
        
        return