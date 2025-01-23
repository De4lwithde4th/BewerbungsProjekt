from datetime import datetime
from pathlib import Path
import csv
import tkinter as tk

records_saved = 0

def initialize_variables(root):
    variables = dict()
    notes_inp = tk.Text(root, width=75, height=10)
    status_variable = tk.StringVar()
    return variables, notes_inp, status_variable

def on_reset(variables, notes_inp):
    for variable in variables.values():
        if isinstance(variable, tk.BooleanVar):
            variable.set(False)
        else:
            variable.set('')
    notes_inp.delete('1.0', tk.END)

def on_save(variables, notes_inp, status_variable):
    global records_saved
    datestring = datetime.today().strftime("%Y-%m-%d")
    filename = f"abq_data_record_{datestring}.csv"
    newfile = not Path(filename).exists()

    data = {}
    fault = variables['Equipment Fault'].get()
    for key, variable in variables.items():
        if fault and key in ('Light', 'Humidity', 'Temperature'):
            data[key] = ''
        else:
            try:
                data[key] = variable.get()
            except tk.TclError:
                status_variable.set(f'Error in field: {key}. Data was not saved')
               
