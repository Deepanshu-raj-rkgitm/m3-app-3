from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime

class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)

    def manu_button_click(self, **event_args):
        glucose = self.glucose_box.text 
        bp = self.bp_box.text
        skinthic = self.skinthic_box.text
        insulin = self.insulin_box.text
        bmi = self.bmi_box.text
        dpf = self.dpf_box.text
        age = self.age_box.text
        preg = self.preg_box.text
        
        try:
            # Call the server function
            anvil.server.call('add_medrecords', glucose, bp, skinthic, insulin, bmi, dpf, age, preg)
            Notification('Your Medical Record has been Submitted!').show()
            self.clear_inputs()
        except Exception as e:
            Notification(f'Error submitting medical record: {str(e)}').show()

    def clear_inputs(self):
        self.glucose_box.text = ""
        self.bp_box.text = ""
        self.skinthic_box.text = ""
        self.insulin_box.text = ""
        self.bmi_box.text = ""
        self.dpf_box.text = ""
        self.age_box.text = ""
        self.preg_box.text = ""

    

    

