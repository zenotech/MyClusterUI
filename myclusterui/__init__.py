
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

class NoDefault:
    pass


class ConfiguratorWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        # Destroying the C++ object right after closing the dialog box,
        # otherwise it may be garbage-collected in another QThread
        # (e.g. the editor's analysis thread in Spyder), thus leading to
        # a segmentation fault on UNIX or an application crash on Windows
        self.setAttribute(Qt.WA_DeleteOnClose)

        bbox = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Apply
                                |QDialogButtonBox.Cancel)
        self.apply_btn = bbox.button(QDialogButtonBox.Apply)
        self.connect(bbox, SIGNAL("accepted()"), SLOT("accept()"))
        self.connect(bbox, SIGNAL("rejected()"), SLOT("reject()"))
        self.connect(bbox, SIGNAL("clicked(QAbstractButton*)"),
                     self.button_clicked)

        self.job_script = self.create_lineedit('Job Script','script')
        self.job_name = self.create_lineedit('Job Name','name')
        self.job_output = self.create_lineedit('Job Output','name')
        self.project_name = self.create_lineedit('Project/Account','name')
        self.queue_widget, self.queue_box = self.create_combobox('Queue', [('hybrid 38','hybrid:hybrid.q')], 'name')
        self.num_tasks = self.create_spinbox('Number tasks', '', 'option', NoDefault, 1, 1, 1, 'total number of tasks')
        self.task_per_node = self.create_spinbox('Task per node', '', 'option', NoDefault, 1, 2, 2, 'tasks per node')
        self.runtime = self.create_spinbox('Runtime', 'hrs', 'option', NoDefault, 1, 36, 1, 'runtime in hrs')
        self.app_script = self.create_lineedit('Application Script','name')
        
        
        hsplitter = QSplitter()
        #hsplitter.addWidget(self.pages_widget)

        btnlayout = QHBoxLayout()
        btnlayout.addStretch(1)
        btnlayout.addWidget(bbox)

        vlayout = QVBoxLayout()
        #vlayout.addWidget(hsplitter)
        
        vlayout.addWidget(self.job_script)
        vlayout.addWidget(self.job_name)
        vlayout.addWidget(self.job_output)
        vlayout.addWidget(self.project_name)
        vlayout.addWidget(self.queue_widget)
        vlayout.addWidget(self.num_tasks)
        vlayout.addWidget(self.task_per_node)
        vlayout.addWidget(self.runtime)
        vlayout.addWidget(self.app_script)
        vlayout.addSpacing(10)
        vlayout.addLayout(btnlayout)

        self.setLayout(vlayout)

        self.setWindowTitle("MyCluster Configurator")


    def show_and_raise(self):
        self.show()
        self.raise_()

    def button_clicked(self, button):
        if button is self.apply_btn:
            # Apply button was clicked
            pass

    def create_lineedit(self, text, option, default=NoDefault,
                        tip=None, alignment=Qt.Horizontal):
        label = QLabel(text)
        label.setWordWrap(True)
        edit = QLineEdit()
        layout = QVBoxLayout() if alignment == Qt.Vertical else QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(edit)
        layout.setContentsMargins(0, 0, 0, 0)
        if tip:
            edit.setToolTip(tip)
        #self.lineedits[edit] = (option, default)
        widget = QWidget(self)
        widget.setLayout(layout)
        return widget

    def create_spinbox(self, prefix, suffix, option, default=NoDefault,
                       min_=None, max_=None, step=None, tip=None):
        if prefix:
            plabel = QLabel(prefix)
        else:
            plabel = None
        if suffix:
            slabel = QLabel(suffix)
        else:
            slabel = None
        spinbox = QSpinBox()
        if min_ is not None:
            spinbox.setMinimum(min_)
        if max_ is not None:
            spinbox.setMaximum(max_)
        if step is not None:
            spinbox.setSingleStep(step)
        if tip is not None:
            spinbox.setToolTip(tip)
        #self.spinboxes[spinbox] = (option, default)
        layout = QHBoxLayout()
        for subwidget in (plabel, spinbox, slabel):
            if subwidget is not None:
                layout.addWidget(subwidget)
        layout.addStretch(1)
        layout.setContentsMargins(0, 0, 0, 0)
        widget = QWidget(self)
        widget.setLayout(layout)
        return widget
    
    def create_combobox(self, text, choices, option, default=NoDefault,
                        tip=None):
        """choices: couples (name, key)"""
        label = QLabel(text)
        combobox = QComboBox()
        if tip is not None:
            combobox.setToolTip(tip)
        for name, key in choices:
            combobox.addItem(name, key)#to_qvariant(key))
        #self.comboboxes[combobox] = (option, default)
        layout = QHBoxLayout()
        for subwidget in (label, combobox):
            layout.addWidget(subwidget)
        layout.addStretch(1)
        layout.setContentsMargins(0, 0, 0, 0)
        widget = QWidget(self)
        widget.setLayout(layout)
        return widget, combobox


def main():
    app = QApplication(sys.argv)

    frame = ConfiguratorWindow()
    
    frame.show_and_raise()
        
    sys.exit(app.exec_())