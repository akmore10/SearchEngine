import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton,QTableWidgetItem
from Backend.CSVDataSourceRead import CSVDataSourceReader

class CustomPopup(QDialog):
    def __init__(self,MainWindow):
        super().__init__()
        self.initUI()
        self.SearchUi = MainWindow
    def initUI(self):
        self.setWindowTitle("Search Box")
        layout = QVBoxLayout()
        self.setFixedSize(350,100)
        label = QLabel("Enter Your Search Terms :")
        line_edit = QLineEdit()

        # Create a button
        button = QPushButton("OK")
        button.clicked.connect(lambda: self.on_button_clicked(line_edit.text()))

        # Add the label, line edit, and button to the layout

        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        # Set the layout for the dialog
        self.setLayout(layout)

    def on_button_clicked(self, text):
        self.close()