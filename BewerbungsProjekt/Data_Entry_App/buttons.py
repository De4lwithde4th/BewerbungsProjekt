from tkinter import ttk
import tkinter as tk
from functions import on_save, on_reset

def setup_buttons(root, variables, notes_inp, status_variable):
    buttons_frame = ttk.Frame(root)
    buttons_frame.grid(sticky='ew')

    save_button = ttk.Button(buttons_frame, text='Save')
    save_button.pack(side='right')
    save_button.configure(command=lambda: on_save(variables, notes_inp, status_variable))

    reset_button = ttk.Button(buttons_frame, text='Reset')
    reset_button.pack(side='right')
    reset_button.configure(command=lambda: on_reset(variables, notes_inp))
