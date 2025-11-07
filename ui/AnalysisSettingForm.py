from PyQt5.QtWidgets import QWidget
from ui import AnalysisSettingForm_ui as ui
from dataStruct import dataStructure as DS
from PyQt5.QtCore import pyqtSlot

class AnalysisSettingForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui.Ui_AnalysisSettingForm()
        self.ui.setupUi(self)
        self.initialize()
        self.analysis = DS.Analysis("")

    def initialize(self):
        self.ui.cubitalCheckBox.setText("Use cubital points")
        self.ui.discoidalCheckBox.setText("Use discoidal points")
        self.ui.startAnalysisPushButton.setText("Start analysis")
        self.ui.analysisNameLabel.setText("Analysis name")
        self.ui.authorNameLabel.setText("Author")
        self.ui.commentLabel.setText("Comments")
        self.ui.inputImagelabel.setText("Input images")
        self.ui.treatedImageLael.setText("Treated images")
        self.setupConnection()

    def setupConnection(self):
        self.ui.nameLineEdit.editingFinished.connect(self.slotNameLineEditEditingFinished)

    @pyqtSlot()
    def slotNameLineEditEditingFinished(self, text):
        if self.analysis is not None:
            self.analysis.name = self.ui.nameLineEdit.text

    def setAnalysis(self, analysis : DS):
        self.analysis = analysis
        self.updateUI()
        return 
        
    def updateUI(self):        
        self.ui.nameLineEdit.setText(self.analysis.name)
        self.ui.authorLineEdit.setText(self.analysis.author)
        self.ui.commentsTextEdit.setText(self.analysis.comment)

        for measure in self.analysis.measures:
            imagePath = str(measure.image)
            print(measure.image, measure.treated)
            if measure.treated:
                self.ui.treatedWingListWidget.addItem(imagePath)
            else:
                self.ui.nonTreatedWingListWidget.addItem(imagePath)


        # and so on ...
        
        return