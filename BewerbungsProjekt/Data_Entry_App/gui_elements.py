import tkinter as tk
from tkinter import ttk

def create_gui(root, variables, notes_inp, status_variable):
    ttk.Label(
        root, text="ABQ DATA Entry Application", font=("TkDefaultFont", 16)
    ).grid()

    drf = ttk.Frame(root)
    drf.grid(padx=10, sticky=(tk.E + tk.W))
    drf.columnconfigure(0, weight=1)

    r_info = ttk.LabelFrame(drf, text="Record Information")
    r_info.grid(sticky=(tk.W + tk.E))
    for i in range(3):
        r_info.columnconfigure(i, weight=1)

    # Record Information
    variables['Date'] = tk.StringVar()
    ttk.Label(r_info, text='Date').grid(row=0, column=0)
    ttk.Entry(r_info, textvariable=variables['Date']).grid(row=1, column=0, sticky=(tk.W + tk.E))

    # Time Selection
    time_values = ['8:00', '12:00', '16:00', '20:00']
    variables['Time'] = tk.StringVar()
    ttk.Label(r_info, text='Time').grid(row=0, column=1)
    ttk.Combobox(r_info, textvariable=variables['Time'], values=time_values).grid(row=1, column=1, sticky=(tk.W + tk.E))

    # Technician
    variables['Technician'] = tk.StringVar()
    ttk.Label(r_info, text='Technician').grid(row=0, column=2)
    ttk.Entry(r_info, textvariable=variables['Technician']).grid(row=1, column=2, sticky=(tk.W + tk.E))

    # Lab Selection (Radiobuttons)
    variables['Lab'] = tk.StringVar()
    ttk.Label(r_info, text='Lab').grid(row=2, column=0)
    labframe = ttk.Frame(r_info)
    for lab in ('A', 'B', 'C'):
        ttk.Radiobutton(labframe, value=lab, text=lab, variable=variables['Lab']).pack(side=tk.LEFT, expand=True)
    labframe.grid(row=3, column=0, sticky=(tk.W + tk.E))

    # Plot Selection (Dropdown)
    variables['Plot'] = tk.IntVar()
    ttk.Label(r_info, text='Plot').grid(row=2, column=1)
    ttk.Combobox(r_info, textvariable=variables['Plot'], values=list(range(1, 21))).grid(row=3, column=1, sticky=(tk.W + tk.E))

    # Seed Sample
    variables['Seed Sample'] = tk.StringVar()
    ttk.Label(r_info, text='Seed Sample').grid(row=2, column=2)
    ttk.Entry(r_info, textvariable=variables['Seed Sample']).grid(row=3, column=2, sticky=(tk.W + tk.E))

    # Environment Data
    e_info = ttk.LabelFrame(drf, text="Environment Data")
    e_info.grid(sticky=(tk.W + tk.E))
    for i in range(3):
        e_info.columnconfigure(i, weight=1)

    # Temperature (Spinbox for float values)
    variables['Temperature'] = tk.DoubleVar()
    ttk.Label(e_info, text='Temperature (°C)').grid(row=0, column=2)
    ttk.Spinbox(e_info, textvariable=variables['Temperature'], from_=4, to=40, increment=.01).grid(row=1, column=2, sticky=(tk.W + tk.E))

    # Equipment Fault (Checkbox)
    variables['Equipment Fault'] = tk.BooleanVar(value=False)
    ttk.Checkbutton(e_info, variable=variables['Equipment Fault'], text='Equipment Fault').grid(row=2, column=0, sticky=tk.W, pady=5)

    # Plant Data
    p_info = ttk.LabelFrame(drf, text="Plant Data")
    p_info.grid(sticky=(tk.W + tk.E))
    for i in range(3):
        p_info.columnconfigure(i, weight=1)

    # Plants (Spinbox)
    variables['Plants'] = tk.IntVar()
    ttk.Label(p_info, text='Plants').grid(row=0, column=0)
    ttk.Spinbox(p_info, textvariable=variables['Plants'], from_=0, to=20, increment=1).grid(row=1, column=0, sticky=(tk.W + tk.E))

    # Blossoms (Spinbox)
    variables['Blossoms'] = tk.IntVar()
    ttk.Label(p_info, text='Blossoms').grid(row=0, column=1)
    ttk.Spinbox(p_info, textvariable=variables['Blossoms'], from_=0, to=1000, increment=1).grid(row=1, column=1, sticky=(tk.W + tk.E))

    # Min Height (Spinbox)
    variables['Min Height'] = tk.DoubleVar()
    ttk.Label(p_info, text='Min Height (cm)').grid(row=2, column=0)
    ttk.Spinbox(p_info, textvariable=variables['Min Height'], from_=0, to=1000, increment=0.01).grid(row=3, column=0, sticky=(tk.W + tk.E))

    # Max Height (Spinbox)
    variables['Max Height'] = tk.DoubleVar()
    ttk.Label(p_info, text='Max Height (cm)').grid(row=2, column=1)
    ttk.Spinbox(p_info, textvariable=variables['Max Height'], from_=0, to=1000, increment=0.01).grid(row=3, column=1, sticky=(tk.W + tk.E))

    # Median Height (Spinbox)
    variables['Med Height'] = tk.DoubleVar()
    ttk.Label(p_info, text='Median Height (cm)').grid(row=2, column=2)
    ttk.Spinbox(p_info, textvariable=variables['Med Height'], from_=0, to=1000, increment=0.01).grid(row=3, column=2, sticky=(tk.W + tk.E))

    # Notes
    ttk.Label(drf, text="Notes").grid()
    notes_inp.grid(sticky=(tk.W + tk.E))

    # Status Anzeige
    ttk.Label(root, textvariable=status_variable).grid(sticky=(tk.W + tk.E), row=99, padx=10)
