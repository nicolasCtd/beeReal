from PyQt5.QtWidgets import QWidget, QListWidgetItem
from ui import AnalysisSettingForm_ui as ui
from dataStruct import dataStructure as DS
from PyQt5.QtCore import pyqtSlot
from models.beeItemModel import BeeItemModel 

class AnalysisSettingForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui.Ui_AnalysisSettingForm()
        self.ui.setupUi(self)
        self.initialize()
        self.analysis = DS.Analysis("")
        self.model = BeeItemModel()
        self.ui.beeTableView.setModel(self.model)
        self.ui.beeTableView.measureAdded.connect(self.slotMeasureAdded)

    def initialize(self):
        self.ui.discoidalCheckBox.setText("Use discoidal points")
        self.ui.startAnalysisPushButton.setText("Start analysis")
        self.ui.stopAnalysisPushButton.setText("Stop")
        #self.ui.stopAnalysisPushButton.setEnabled(False)
        self.ui.analysisNameLabel.setText("Analysis name")
        self.ui.authorNameLabel.setText("Author")
        self.ui.commentLabel.setText("Comments")
        
        self.setupConnection()

    def getAnalysis(self):
        return self.analysis

    def setAnalysis(self, analysis : DS):
        self.analysis = analysis
        self.updateUI()
        return 
        
    def updateUI(self):        
        self.ui.nameLineEdit.setText(self.analysis.name)
        self.ui.authorLineEdit.setText(self.analysis.author)
        self.ui.commentsTextEdit.setText(self.analysis.comment)
        self.ui.discoidalCheckBox.setChecked(self.analysis.useDiscoidalPoints)

        for measure in self.analysis.measures:
            self.model.appendMeasure(measure)

        # and so on ...
        
        return
    
    def setupConnection(self):
        self.ui.nameLineEdit.editingFinished.connect(self.slotNameLineEditEditingFinished)
        self.ui.authorLineEdit.editingFinished.connect(self.slotAuthorLineEditEditingFinished)
        self.ui.discoidalCheckBox.toggled.connect(self.slotDiscoidalCheckBoxToggled)
        self.ui.commentsTextEdit.textChanged.connect(self.slotCommentsTextEditTextChanged)
        self.ui.stopAnalysisPushButton.released.connect(self.slotStopAnalysisReleased)

    #### SLOTS GOES HERE
    @pyqtSlot()
    def slotNameLineEditEditingFinished(self):
        if self.analysis is not None:
            self.analysis.name = self.ui.nameLineEdit.text()   

    @pyqtSlot()
    def slotAuthorLineEditEditingFinished(self):
        if self.analysis is not None:
            self.analysis.author = self.ui.authorLineEdit.text()         

    @pyqtSlot()
    def slotCommentsTextEditTextChanged(self):
        if self.analysis is not None:
            self.analysis.comment = self.ui.commentsTextEdit.toPlainText()

    @pyqtSlot(bool)
    def slotDiscoidalCheckBoxToggled(self, checked):
        if self.analysis is not None:
            self.analysis.useDiscoidalPoints = checked   

    @pyqtSlot(QListWidgetItem)
    def slotImageItemDoubleClicked(self, item : QListWidgetItem):
        if item is not None:
            print(item.text())        
        return
    
    @pyqtSlot(DS.Measure)
    def slotMeasureAdded(self, measure : DS.Measure):
        # Append a measure to the analyse
        self.analysis.appendMeasure(measure)
        return
    
    @pyqtSlot()
    def slotStopAnalysisReleased(self):
        return