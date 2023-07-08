# Librerías
import requests
import pandas as pd
from datetime import datetime

# Función de extracción
def fetch_data():
    now = datetime.now()
    month = now.strftime('%b').upper()
    year = now.strftime('%Y')
    url = f'http://www.estadistica.ucr.ac.cr/images/EEs/Documentos/Encuestas/Consumidor/Datos/ENCUESTA_CONSUMIDOR_A_{month}_{year}.xlsx'
    response = requests.get(url)
    if response.status_code == 200:
        base = pd.read_excel(response.content)
        base.to_excel("base_data.xlsx", index=False)
                  

fetch_data()
