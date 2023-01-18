"""#https://www.pythontutorial.net/tkinter/tkinter-mvc/
/home/cir/Escritorio/cir/apuntes/devnet/mvc
modificado por Cirino Silva Tovar el 9 sep 2022
para que acepte el nombre y lo guarde
"""

import tkinter as tk
from Model import Model
from View import View
from Controller import Controller

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('Tkinter MVC Demo')
    # create a model
    model = Model('hello@pythontutorial.net', 'python tutorial')
    # create a view and place it on the root window
    view = View(self)
    view.grid(row=0, column=0, padx=10, pady=10)
    view.grid(row=1, column=0, padx=10, pady=10)
    # create a controller
    controller = Controller(model, view)
    # set the controller to view
    view.setController(controller)

if __name__ == '__main__':
    app = App()
    app.mainloop()
    print("Hola") <--- Modificación.
    
