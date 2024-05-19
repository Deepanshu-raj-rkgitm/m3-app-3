import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import requests

@anvil.server.callable
def get_image_text(image_file):
    api_url = 'https://api.api-ninjas.com/v1/imagetotext'
    files = {'image': ('image.jpg', image_file.get_bytes(), image_file.content_type)}
    response = requests.post(api_url, files=files)
    return response.json()

