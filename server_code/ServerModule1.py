import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables
from datetime import datetime

@anvil.server.callable
def add_medrecords(glucose, bp, skinthic, insulin, bmi, dpf, age):
    # Ensure all values are properly converted to the expected data types if necessary
    try:
        glucose = float(glucose)
        bp = float(bp)
        skinthic = float(skinthic)
        insulin = float(insulin)
        bmi = float(bmi)
        dpf = float(dpf)
        age = int(age)
    except ValueError:
        raise ValueError("Invalid input: Please ensure all fields are filled with the correct data types.")

    # Add a new row to the medical_records table
    app_tables.medical_records.add_row(
        glucose=glucose,
        bp=bp,
        skinthic=skinthic,
        insulin=insulin,
        bmi=bmi,
        dpf=dpf,
        age=age,
        timestamp=datetime.now()
    )
