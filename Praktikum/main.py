import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from data_enty_form import DataEntryForm


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moderne GUI mit PySide6")
        self.setGeometry(100, 100, 900, 600)

        # Dark Theme Stylesheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2E2E2E;
                color: #DCDCDC;
            }
            QLabel, QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox, QTextEdit, QPushButton, QCheckBox, QRadioButton {
                background-color: #3E3E3E;
                color: #DCDCDC;
                border: 1px solid #555555;
                border-radius: 4px;
                padding: 5px;
            }
            QPushButton {
                background-color: #555555;
                border: none;
            }
            QPushButton:hover {
                background-color: #666666;
            }
            QCheckBox, QRadioButton {
                padding: 2px;
            }
            QGroupBox {
                border: 1px solid #555555;
                border-radius: 5px;
                padding: 10px;
            }
        """)

        # Instanz des Formulars erstellen und als zentrales Widget festlegen
        form = DataEntryForm()
        self.setCentralWidget(form)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
