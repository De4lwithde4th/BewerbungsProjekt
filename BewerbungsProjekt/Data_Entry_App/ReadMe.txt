Die DATA Entry Application ist eine benutzerfreundliche GUI-Anwendung, die mit Python und dem Tkinter-Framework entwickelt wurde. Die Anwendung ermöglicht es Benutzern, Datensätze effizient einzugeben, zu speichern und bei Bedarf zurückzusetzen. Sie ist speziell für das Erfassen von Umgebungs- und Pflanzendaten konzipiert, eignet sich jedoch auch für ähnliche Aufgaben der Dateneingabe.


Funktionsweise der GUI:
Felder für Datum, Zeit, Technikername, Labor, Parzellen-ID und Samenprobe.

Eingabe von Umgebungsdaten wie Temperatur, Anzahl der Pflanzen, Blüten sowie Pflanzenhöhe.

Weitere Auswahl für Equipment-Fehlern.

Speicherfunktion:
Speichern der eingegebenen Daten in einer CSV-Datei.
Automatische Erstellung einer neuen Datei für jeden Tag.

Zurücksetzen der Felder:
Alle Felder und Notizen können mit einem Klick auf den Reset-Button zurückgesetzt werden.

Notizbereich:
Freitextfeld für zusätzliche Bemerkungen.
Statusanzeige:
Echtzeit-Feedback zu Speichervorgängen oder Fehlern bei der Eingabe.


WICHTIG/IMPORTANT!!!

Installation, und Voraussetzungen sind Python 3.7 oder höher sowie tkinter, datetime, csv und pathlib um diesen Code zu Runnen.

Führen sie den Befehl. Python main.py.




Dateneingabe:
Füllen Sie die erforderlichen Felder aus.
Wählen Sie den Labortyp, die Parzellen-ID und andere Werte aus den Dropdown-Menüs oder Spinboxen aus.
Daten speichern:
Klicken Sie auf Save, um die eingegebenen Daten in einer CSV-Datei zu speichern.
Zurücksetzen:
Klicken Sie auf Reset, um alle Eingaben zu löschen und mit einer leeren Eingabemaske zu starten.

Dateiformat:
Die gespeicherten Daten werden im CSV-Format abgelegt. Jede Datei wird im aktuellen Arbeitsverzeichnis gespeichert und nach dem Schema abq_data_record_<YYYY-MM-DD>.csv benannt.
 
