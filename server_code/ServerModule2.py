import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from PIL import Image
from pytesseract import pytesseract 
import enum

class language(enum.ENUM):
  ENG = 'eng'

def extract_text(self, image: str, lang: str)  -> str:
  img =Image.open(image)
