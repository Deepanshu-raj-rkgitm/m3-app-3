import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import re

# Function to extract a field using a regex pattern
def extract_field(content, pattern, field_name):
    match = re.search(pattern, content, re.IGNORECASE)
    if match:
        return match.group(1)
    else:
        print(f"Pattern for {field_name} not found in content.")
        return None

@anvil.server.callable
def extract_and_save(file):
    try:
        content = file.get_bytes().decode('utf-8')
    except UnicodeDecodeError:
        # Try another encoding if UTF-8 fails
        content = file.get_bytes().decode('latin1')
    
    # Define patterns for each field
    patterns = {
        "glucose": r"glucose:\s*(\d+)",
        "bp": r"bp:\s*(\d+)",
        "skin_thickness": r"skin thickness:\s*(\d+)",
        "insulin": r"insulin:\s*(\d+)",
        "bmi": r"bmi:\s*([\d.]+)",
        "dpf": r"dpf:\s*([\d.]+)",
        "age": r"age:\s*(\d+)",
        "pregnancies": r"pregnancies:\s*(\d+)"
    }
    
    # Extract the fields using regular expressions
    extracted_data = {}
    for key, pattern in patterns.items():
        extracted_data[key] = extract_field(content, pattern, key)
        if extracted_data[key] is None:
            raise ValueError(f"Could not find {key} in the provided file.")
    
    # Convert to appropriate types
    glucose = int(extracted_data["glucose"])
    bp = int(extracted_data["bp"])
    skin_thickness = int(extracted_data["skin_thickness"])
    insulin = int(extracted_data["insulin"])
    bmi = float(extracted_data["bmi"])
    dpf = float(extracted_data["dpf"])
    age = int(extracted_data["age"])
    pregnancies = int(extracted_data["pregnancies"])
    
    # Save to the database
    app_tables.medical_records.add_row(glucose=glucose, bp=bp, skin_thickness=skin_thickness,
                                       insulin=insulin, bmi=bmi, dpf=dpf, age=age, pregnancies=pregnancies)

    return {
        "glucose": glucose,
        "bp": bp,
        "skin_thickness": skin_thickness,
        "insulin": insulin,
        "bmi": bmi,
        "dpf": dpf,
        "age": age,
        "pregnancies": pregnancies
    }



