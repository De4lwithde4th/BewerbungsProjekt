import tkinter as tk
from tkinter import ttk
from gui_elements import create_gui
from buttons import setup_buttons
from functions import initialize_variables



# Hauptprogramm starten
if __name__ == "__main__":
    root = tk.Tk()
    root.title("ABQ DATA Entry Application")
    root.columnconfigure(0, weight=1)

    # Variablen initialisieren
    variables, notes_inp, status_variable = initialize_variables(root)

    # GUI-Elemente erstellen
    create_gui(root, variables, notes_inp, status_variable)

    # Buttons einrichten
    setup_buttons(root, variables, notes_inp, status_variable)

    # Hauptschleife starten
    root.mainloop()
