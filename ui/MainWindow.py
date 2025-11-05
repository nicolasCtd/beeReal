from PyQt5.QtWidgets import QMainWindow
from ui import MainWindow_ui as ui
from ui import AnalysisSettingForm as ASF

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui.Ui_mainWindow()
        self.ui.setupUi(self)
        self.initialize()
        
    def initialize(self):
        self.analysisForm = ASF.AnalysisSettingForm()
        self.setCentralWidget(self.analysisForm)