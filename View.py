"""https://www.pythontutorial.net/tkinter/tkinter-mvc/
/home/cir/Escritorio/cir/apuntes/devnet/mvc
modificado por Cirino Silva Tovar el 9 sep 2022
para que acepte el nombre y lo guarde
"""

import re
import tkinter as tk
from tkinter import ttk

class View(ttk.Frame):
  def __init__(self, parent):
    super().__init__(parent)
    # create widgets
    # label
    self.label = ttk.Label(self, text='Email:')
    self.label.grid(row=1, column=0)
    self.labeln = ttk.Label(self, text='name:')
    self.labeln.grid(row=2, column=0)
    # email entry
    self.email_var = tk.StringVar()
    self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
    self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)
    # name entry
    self.name_var = tk.StringVar()
    self.name_entry = ttk.Entry(self, textvariable=self.name_var, width=30)
    self.name_entry.grid(row=2, column=1, sticky=tk.NSEW)
    # save button
    self.save_button = ttk.Button(self, text='Save', command=self.saveButton)
    self.save_button.grid(row=1, column=3, padx=10)
    # message
    self.message_label = ttk.Label(self, text='', foreground='red')
    self.message_label.grid(row=3, column=1, sticky=tk.W)
    # set the controller
    self.controller = None

  def setController(self, controller):
    # Set the controller:param controller:return:"""
    self.controller = controller

  def saveButton(self):
    # Handle button click event:return: """
    if self.controller:
      self.controller.save(self.email_var.get(), self.name_var.get())

  def show_error(self, message):
    #Show an error message:param message:return:"""
    self.message_label['text'] = message
    self.message_label['foreground'] = 'red'
    self.message_label.after(3000, self.hide_message)
    self.email_entry['foreground'] = 'red'

  def show_success(self, message):
    # Show a success message:param message:return: """
    self.message_label['text'] = message
    self.message_label['foreground'] = 'green'
    self.message_label.after(3000, self.hide_message)
    # reset the form
    self.email_entry['foreground'] = 'black'
    self.email_var.set('')
    self.name_entry['foreground'] = 'black'
    self.name_var.set('')

  def hide_message(self):
    # Hide the message:return:"""
    self.message_label['text'] = ''
    
