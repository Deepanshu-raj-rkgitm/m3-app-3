from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
def button_1_click(self, **event_args):
        try:
            glucose = float(self.text_box_number1.text)
            number2 = float(self.text_box_number2.text)
            decimal_value = float(self.text_box_decimal.text)
        except ValueError:
            alert("Please enter valid numbers.")
            return

   
 