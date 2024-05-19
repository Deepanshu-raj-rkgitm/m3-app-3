import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from PIL import Image
from pytesseract import pytesseract 
import enum

pytesseract.pytesseract.tesseract_cmd = '_/theme/tesseract-ocr-setup-3.02.02.exe'
def extract_text_from_image(file):
    # Read the image file
    img = Image.open(file)
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(img)
    return text