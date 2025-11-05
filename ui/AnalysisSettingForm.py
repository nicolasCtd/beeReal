from PyQt5.QtWidgets import QWidget
from ui import AnalysisSettingForm_ui as ui

class AnalysisSettingForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui.Ui_AnalysisSettingForm()
        self.ui.setupUi(self)
        self.initialize()

    def initialize(self):
        self.ui.cubitalCheckBox.setText("Use cubitabl points")
        self.ui.discoidalCheckBox.setText("Use discoidal points")
        self.ui.startAnalysisPushButton.setText("Start analysis")