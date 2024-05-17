from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables
from datetime import datetime

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


def manu_button(self, **event_args):
        try:
            glucose = float(self.glucose.text)
            blood_pressure = float(self.bp.text)
            skin_thic = float(self.skin_thic.text)
            insulin = float(self.insulin.text)
            dpf = float(self.dpf.text)
            bmi = float(self.bmi.text)
            age = float(self.age.text)
            preg = self.preg.items = [("Yes", True), ("No", False)]
            preg = self.preg.selected_value
            timestamp = datetime.now()
        except ValueError:
            alert("Please enter valid numbers.")
            return
           
          
 self.clear_inputs()

def clear_inputs(self): 
        self.glucose.text = ""
        self.bp.text = ""
        self.skin_thic.text = ""
        self.insulin.text = ""
        self.bmi.text = ""
        self.dpf.text = ""
        self.age.text =""
        self.preg.selected_value = None
        
        # Notify the user that the form was submitted
        alert("Data submitted successfully!")

