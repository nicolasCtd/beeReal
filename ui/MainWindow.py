from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon
from ui import MainWindow_ui as ui
from ui import AnalysisSettingForm as ASF
from PyQt5.QtCore import pyqtSlot


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui.Ui_mainWindow()
        self.ui.setupUi(self)
        self.initialize()
        
    def initialize(self):        
        #self.setWindowIcon(QIcon(":/images/deco1.jpg"))        
        self.analysisForm = ASF.AnalysisSettingForm()
        #self.analysisForm .setEnabled(False)
        #self.setCentralWidget(self.analysisForm)
        self.ui.analysisVerticalLayout.addWidget(self.analysisForm)

        # Some shortcuts
        self.ui.actionLoad_analysis.setShortcut("Ctrl+O")

        # Connection
        self.ui.actionLoad_analysis.triggered.connect(self.loadAnalysis)

    @pyqtSlot()
    def loadAnalysis(self):
        print("Loading analysis")
        # QFileDialog renvoie un tuple (chemin, filtre)
        chemin, _ = QFileDialog.getOpenFileName(
            self,
            "Open analysis file",
            "",
            "xml file (*.xml);; bee file (*.bee)"
        )

        return