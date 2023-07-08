# ICC-dashboard

El objetivo de este repositorio es compartir el código utilizado para la creación del dashboard de la Encuesta de Confianza al Consumidor, con la idea de que cualquier persona pueda aportar retroalimentación.

## Ambiente

1. El primer paso es configurar el ambiente. Para esto, seguir las instrucciones en [configurar ambiente](./docs/ambiente.md).

## Datos
Hay dos formas de extraer los datos:

1. Mediante el archivo de código `datos.py` el cual puede guardar los datos en un archivo de excel.
2. Directamente copiar el código en Power BI para obtener los datos de forma automática.

Los datos se obtuvieron de la página oficial de la Escuela de Estadística de la Universidad de Costa Rica, para obtenerlos se utilizó una Interfaz de Programación de Aplicaciones o por sus siglas en inglés *API*.

Para efectos del Dashboard, este código es necesario para extraer los datos que se van a utilizar y poder replicar este ejemplo. Por lo tanto, pueden revisar el archivo `datos.py` para copiar y pegar el código en pasos siguientes. No obstante, aquí desgloso las líneas de código. 

```{python}
import requests
import pandas as pd


url = "http://www.estadistica.ucr.ac.cr/images/EEs/Documentos/Encuestas/Consumidor/Datos/ENCUESTA_CONSUMIDOR_A_MAY_2023.xlsx"
response = requests.get(url)

base = pd.read_excel(response.content)
```

- Se utiliza la librería `requests` para hacer las solicitud de extracción (**_GET_**) de los datos.
- La librería `Pandas` para convertir la solicitud en un formato entendible como lo es un set de datos. 
- La variable `url` es un tipo string y es donde se almacena la dirección web de la ubicación de los datos en formato `xlsx`, luego la variable response contiene la respuesta de la consulta al servidor. Por último, esto se almacenó en una variable denominada `base`.

## Dashboard

- agregar un archivo de power BI para que lo prueban probar

