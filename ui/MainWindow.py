from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon
from ui import MainWindow_ui as ui
from ui import AnalysisSettingForm as ASF
from PyQt5.QtCore import pyqtSlot
from IO import IO
from dataStruct import dataStructure as DS


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui.Ui_mainWindow()
        self.ui.setupUi(self)
        self.initialize()
        self.analysisPath = None
        
    def initialize(self):        
        #self.setWindowIcon(QIcon(":/images/deco1.jpg"))        
        self.analysisForm = ASF.AnalysisSettingForm()
        self.analysisForm .setEnabled(False)        
        self.ui.analysisVerticalLayout.addWidget(self.analysisForm)

        # Some shortcuts
        self.ui.actionLoad.setShortcut("Ctrl+O")
        self.ui.actionNew.setShortcut("Ctrl+N")
        self.ui.actionSave.setShortcut("Ctrl+S")        
        self.ui.actionSave.setEnabled(False)
        self.ui.actionSaveAs.setEnabled(False)
        # Connection
        self.ui.actionLoad.triggered.connect(self.loadAnalysis)
        self.ui.actionSave.triggered.connect(self.saveAnalysis)
        self.ui.actionSaveAs.triggered.connect(self.saveAnalysisAs)


    @pyqtSlot()
    def loadAnalysis(self):
        #print("Loading analysis")
        # QFileDialog renvoie un tuple (chemin, filtre)
        chemin, _ = QFileDialog.getOpenFileName(
            self,
            "Open analysis file",
            "",
            "xml file (*.xml);; bee file (*.bee)"
        )

        if chemin:
            self.analysisPath = chemin
            analysisFile = IO.AnalysisFile(chemin)
            analysis = analysisFile.loadAnalysis()
            self.analysisForm.setAnalysis(analysis)
            self.analysisForm .setEnabled(True)
            self.ui.actionSave.setEnabled(True)
            self.ui.actionSaveAs.setEnabled(True)



        return
    
########## SLOTS GOES HERE

    @pyqtSlot()   
    def saveAnalysisAs(self):

        chemin, ext = QFileDialog.getSaveFileName(
            self,
            "Save analysis to ...",
            "",
            "xml file (*.xml);; bee file (*.bee)"
        )

        # TODO: find a way to automatically add default extension if missing

        if chemin:
            self.analysisPath = chemin
            self.saveAnalysis()

        return

    @pyqtSlot()
    def saveAnalysis(self):

        if self.analysisPath is not None:
            analysis =self.analysisForm.getAnalysis()        
            analysis.updateDate()    
            analysisFile = IO.AnalysisFile(self.analysisPath)
            analysisFile.saveAnalysis(analysis)

        return
