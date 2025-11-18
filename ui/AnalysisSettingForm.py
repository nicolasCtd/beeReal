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
        #self.model = QStandardItemModel()
        #self.model.setHorizontalHeaderLabels(["name", "Status"])
        self.model = BeeItemModel()
        self.ui.beeTableView.setModel(self.model)

    def initialize(self):
        self.ui.discoidalCheckBox.setText("Use discoidal points")
        self.ui.startAnalysisPushButton.setText("Start analysis")
        self.ui.analysisNameLabel.setText("Analysis name")
        self.ui.authorNameLabel.setText("Author")
        self.ui.commentLabel.setText("Comments")
        self.setupConnection()

    def setupConnection(self):
        self.ui.nameLineEdit.editingFinished.connect(self.slotNameLineEditEditingFinished)

    @pyqtSlot()
    def slotNameLineEditEditingFinished(self):
        if self.analysis is not None:
            self.analysis.name = self.ui.nameLineEdit.text

    @pyqtSlot(QListWidgetItem)
    def slotImageItemDoubleClicked(self, item : QListWidgetItem):
        if item is not None:
            print(item.text())        
        return

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