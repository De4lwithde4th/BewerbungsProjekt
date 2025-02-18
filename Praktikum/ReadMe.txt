Dieses Kleine Projekt ist im Sinne meiner Bewerbungsaussagen für ein Praktikumsplatz.

Dieses Projekt ist eine Grafischeoberfläche(GUI) die für die Dateneingabe von Pflanzendaten sind. Die GUI wurde in Python 3.8 erichtet, und mit folgenden Framewokrs ausgestattet: PySide6, datetime, pathlib, sys.




Features:

Dark Theme: Einheitliches dunkles Design für eine moderne Optik.

Dynamisches Formular: Eingabefelder für Temperatur, Pflanzenanzahl, Blütenanzahl, Höhenangaben und Laborauswahl.

Dateiauswahl: Möglichkeit, eine CSV-Datei zur Speicherung der Daten auszuwählen.

Daten speichern: Speichert die eingegebenen Informationen in einer CSV-Datei.

Reset-Funktion: Setzt alle Eingabefelder zurück.

Diagrammanzeige: Visualisierung der gespeicherten Pflanzendaten in Diagrammform.




Benötigte Abhängigkeiten installieren:

pip install PySide6, datetime, pathlib, sys.




Verwendung:

Starten der Anwendung

python main.py

Eingabe von Daten

Laborauswahl treffen (A, B oder C).

Temperaturwert setzen.

"Equipment Fault" Checkbox aktivieren, falls erforderlich.

Anzahl der Pflanzen und Blüten eingeben.

Minimale, maximale und Median-Höhe eingeben.

Datei zur Speicherung der Daten auswählen oder Standarddatei verwenden.

Auf "Save" klicken, um die Daten in einer CSV-Datei zu speichern.

Zurücksetzen der Eingaben

Durch Klicken auf "Reset" werden alle Eingabefelder zurückgesetzt.

Datenanalyse mit Diagrammen

Die gespeicherten Pflanzendaten können als Diagramm visualisiert werden.

Temperatur- und Höhenverteilungen können dargestellt werden.


├── main.py                 # Hauptprogramm mit der MainWindow-Klasse
├── data_entry_form.py      # Formular zur Dateneingabe
├── lab_selection.py        # Laborauswahl als QGroupBox mit Radiobuttons
├── environment_data.py     # Eingabefelder für Temperatur und Equipment Fault
├── plant_data.py           # Eingabefelder für Pflanzen- und Blütendaten
├── file_selector.py        # Dateiauswahl für CSV-Datei
├── data_visualization.py   # Modul zur Darstellung von Diagrammen
└── README.md               # Diese Datei



Erstellt von Mar-Andre