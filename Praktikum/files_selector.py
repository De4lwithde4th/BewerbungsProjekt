from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton, QFileDialog


class FileSelector(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        # Textfeld zur Anzeige des ausgewählten Pfads
        self.file_path_input = QLineEdit()
        self.file_path_input.setPlaceholderText("Select CSV file location...")
        layout.addWidget(self.file_path_input)

        # Button zum Öffnen des Datei-Dialogs
        self.select_button = QPushButton("Browse")
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)

        self.setLayout(layout)

    def select_file(self):
        """Öffnet den Datei-Dialog zur Auswahl oder Erstellung einer CSV-Datei."""
        file_path, _ = QFileDialog.getSaveFileName(self, "Select CSV File", "", "CSV Files (*.csv);;All Files (*)")
        if file_path:
            self.file_path_input.setText(file_path)

    def get_file_path(self):
        """Gibt den aktuellen Dateipfad zurück."""
        return self.file_path_input.text()
