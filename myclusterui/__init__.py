
import sys

from PySide.QtGui import (QWidget, QDialog, QListWidget, QListWidgetItem,
                                QVBoxLayout, QStackedWidget, QListView,
                                QHBoxLayout, QDialogButtonBox, QCheckBox,
                                QMessageBox, QLabel, QLineEdit, QSpinBox,
                                QPushButton, QFontComboBox, QGroupBox,
                                QComboBox, QColor, QGridLayout, QTabWidget,
                                QRadioButton, QButtonGroup, QSplitter,
                                QStyleFactory, QScrollArea,QApplication,QIcon,
                                QDoubleSpinBox )
from PySide.QtCore import Qt, QSize, SIGNAL, SLOT, Slot



class ConfiguratorWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle("MyCluster Configurator")

    def show_and_raise(self):
        self.show()
        self.raise_()

def main():
    app = QApplication(sys.argv)

    frame = ConfiguratorWindow()
    
    frame.show_and_raise()
        
    sys.exit(app.exec_())