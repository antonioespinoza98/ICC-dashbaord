import requests
import pandas as pd


url = "https://estadistica.ucr.ac.cr/images/EEs/Documentos/Encuestas/Consumidor/Datos/ENCUESTA_CONSUMIDOR_A_MAY_2023.xlsx"
response = requests.get(url)


base = pd.read_excel(response.content)

base.to_excel("datos.xlsx", index=False)