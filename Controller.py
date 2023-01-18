"""#https://www.pythontutorial.net/tkinter/tkinter-mvc/
/home/cir/Escritorio/cir/apuntes/devnet/mvc
modificado por Cirino Silva Tovar el 9 sep 2022
para que acepte el nombre y lo guarde
"""

class Controller:
  def __init__(self, model, view):
    self.model = model
    self.view = view

  def save(self, email, name):
    """ Save the email :param email: return: """
    try:
      # save the model
      self.model.email = email
      self.model.name = name
      self.model.save()
      # show a success message
      self.view.show_success('The email {email} saved !')

    except ValueError as error:
      # show an error message
      self.view.show_error(error)
      
