from PyQt5.QtWidgets import QWidget
from ui import AnalysisSettingForm_ui as ui

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