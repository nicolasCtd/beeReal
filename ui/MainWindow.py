from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from ui import MainWindow_ui as ui
from ui import AnalysisSettingForm as ASF

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
        self.setCentralWidget(self.analysisForm)