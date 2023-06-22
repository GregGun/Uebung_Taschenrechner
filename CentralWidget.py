import PyQt6
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QSlider, QHBoxLayout, QTextBrowser, QGridLayout, QLabel, QLineEdit, QTextBrowser
from PyQt6.QtCore import pyqtSlot, Qt, QSize


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.binLabel = QLabel("Binärzahl 0 - 1111 1111", self)
        self.binLineEdit = QLineEdit(self)
        self.binLineEdit.setInputMask("Bbbbbbbb")
        self.binLineEdit.setText("0")

        self.hexaLabel = QLabel("Hexadezimalzahl 0 - FF", self)
        self.hexaLineEdit = QLineEdit(self)
        self.hexaLineEdit.setInputMask("Hh")
        self.hexaLineEdit.setText("0")

        self.ergebnis = QLabel("Ergebnis: ", self)
        self.ergebnis_text = QTextBrowser(self)

        self.binLineEdit.editingFinished.connect(self.calc)
        self.hexaLineEdit.editingFinished.connect(self.calc)

        layout = QGridLayout(self)
        layout.addWidget(self.binLabel, 1, 1)
        layout.addWidget(self.binLineEdit, 1, 2)
        layout.addWidget(self.hexaLabel, 2, 1)
        layout.addWidget(self.hexaLineEdit, 2, 2)
        layout.addWidget(self.ergebnis, 3, 1)
        layout.addWidget(self.ergebnis_text, 3, 2)

        self.setLayout(layout)

    @pyqtSlot()
    def calc(self):

        is_valid = True

        is_valid = is_valid and self.binLineEdit.hasAcceptableInput()
        is_valid = is_valid and self.hexaLineEdit.hasAcceptableInput()

        if is_valid:
            str_bin = self.binLineEdit.text()
            str_hex = self.hexaLineEdit.text()

        if str_bin != "0" and str_hex:
            self.ergebnis_text.append(str_bin + " + " + str_hex)
        else:
            print("Fehler")
