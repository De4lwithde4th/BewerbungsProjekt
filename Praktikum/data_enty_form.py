import csv
from datetime import datetime
from pathlib import Path

from PySide6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QHBoxLayout, QPushButton, QMessageBox
from lab_selection import LabSelection
from enviroment_data import EnvironmentData
from plant_data import PlantData
from files_selector import FileSelector  # Import der neuen Datei


class DataEntryForm(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        # Datei-Selector hinzufügen
        self.file_selector = FileSelector()
        main_layout.addWidget(self.file_selector)

        # Formular Layout
        form_layout = QFormLayout()

        # Komponenten hinzufügen
        self.lab_selection = LabSelection()
        self.environment_data = EnvironmentData()
        self.plant_data = PlantData()

        # Komponenten dem Formular hinzufügen
        form_layout.addRow(self.lab_selection)
        form_layout.addRow(self.environment_data)
        form_layout.addRow(self.plant_data)

        # Buttons
        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save")
        self.reset_button = QPushButton("Reset")
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.reset_button)

        # Button-Aktionen verbinden
        self.save_button.clicked.connect(self.save_data)
        self.reset_button.clicked.connect(self.reset_form)

        # Layouts kombinieren
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def save_data(self):
        """Sammelt die Eingabedaten und speichert sie in einer CSV-Datei."""
        # Dateipfad aus dem FileSelector abrufen
        file_path = self.file_selector.get_file_path()
        if not file_path:
            file_path = "data_entries.csv"  # Standardpfad, falls nichts ausgewählt wurde

        file = Path(file_path)

        # Daten aus den Komponenten sammeln
        lab = self.lab_selection.get_selected_lab()
        temperature = self.environment_data.temperature_input.value()
        equipment_fault = self.environment_data.equipment_fault_checkbox.isChecked()
        plants = self.plant_data.plants_input.value()
        blossoms = self.plant_data.blossoms_input.value()
        min_height = self.plant_data.min_height_input.value()
        max_height = self.plant_data.max_height_input.value()
        med_height = self.plant_data.med_height_input.value()

        # Aktuelles Datum und Uhrzeit
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Daten in eine Liste umwandeln
        row = [
            timestamp,
            lab,
            temperature,
            "Yes" if equipment_fault else "No",
            plants,
            blossoms,
            min_height,
            max_height,
            med_height,
        ]

        # Header der CSV-Datei
        headers = [
            "Timestamp",
            "Lab",
            "Temperature (°C)",
            "Equipment Fault",
            "Plants",
            "Blossoms",
            "Min Height (cm)",
            "Max Height (cm)",
            "Median Height (cm)",
        ]

        # Prüfen, ob die Datei existiert, und Header hinzufügen, falls sie neu ist
        try:
            file_exists = file.exists()

            with file.open("a", newline="") as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(headers)  # Schreibe die Header, wenn die Datei neu ist
                writer.writerow(row)

            QMessageBox.information(self, "Success", f"Data saved successfully to:\n{file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save data: {e}")

    def reset_form(self):
        """Setzt alle Eingabefelder zurück."""
        self.lab_selection.reset()
        self.environment_data.temperature_input.setValue(4.00)  # Standardwert setzen
        self.environment_data.equipment_fault_checkbox.setChecked(False)
        self.plant_data.plants_input.setValue(0)
        self.plant_data.blossoms_input.setValue(0)
        self.plant_data.min_height_input.setValue(0.00)
        self.plant_data.max_height_input.setValue(0.00)
        self.plant_data.med_height_input.setValue(0.00)