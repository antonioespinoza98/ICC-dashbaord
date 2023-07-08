# ICC-dashboard

El objetivo de este repositorio es compartir el código utilizado para la creación del dashboard de la Encuesta de Confianza al Consumidor, con la idea de que cualquier persona pueda aportar retroalimentación.

## Autores

1. Marco Espinoza Marín
2. Sofía Carvajal Fallas
3. Daniel López Júarez 
4. Ariana Chacón Navarro
5. Bryan Monge Blanco

## Ambiente

1. El primer paso es configurar el ambiente. Para esto, seguir las instrucciones en [configurar ambiente](./docs/ambiente.md).

## Datos
Hay dos formas de extraer los datos:

1. Mediante el archivo de código `datos.py` el cual puede guardar los datos en un archivo de excel.
2. Directamente copiar el código en Power BI para obtener los datos de forma automática.

Los datos se obtuvieron de la página oficial de la Escuela de Estadística de la Universidad de Costa Rica, para obtenerlos se utilizó una Interfaz de Programación de Aplicaciones o por sus siglas en inglés *API*.

<span style="color: red; font-weight: bold;">NOTA</span>

Este código extrae los datos **manualmente**.

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

### Detectar automáticamente el interpretador

Inicialmente, y tomando en consideración los prerrequisitos de la instalación de Anaconda, se debe verificar en Power BI que detecta la dirección en donde Anaconda está instalado. 

1. Para esto, se dirige a la parte superior izquierda en **Archivo**


![archivo](/imagenes/archivo.png)

2. El segundo paso es en **Opciones y configuración** > **Opciones**

3. El tercer paso es verificar que Power BI reconozca la dirección de la instalación de Python, para esto al lado derecho dar click en **Creación de scripts de Python**. Este debería tener una dirección como se muestra en la imagen de abajo. En caso de que no se encuentre este se puede buscar manualmente dando click en el menú desplegable. Si en caso no sabe donde instaló Anaconda, puede abrir Anaconda Prompt y correr la siguiente línea de código:

```{cmd}
where anaconda
```

![python](/imagenes/path.png)

Luego da click en aceptar.

### Extraer la base de datos desde un script de python

Para extraer la base de datos directamente desde la página de la Escuela de Estadística, se siguen los siguientes pasos:

1. En la pestaña de **Inicio** click en **Obtener Datos**

![datos](/imagenes/datos.png)

2. Luego de esto, dar click en la última opción > **Más**

![mas](/imagenes/mas.png)

3. Esto va abrir la siguiente pestaña, en el buscador escriben `Python` y debería aparecer algo como se muestra en la siguiente imagen:

![script](/imagenes/script.png)

4. Por último, eso abre una terminal de `Python`, donde solamente deben colocar el código que se dio previamente y dar click en **aceptar**, como se muestra de la siguiente manera:

![extra](/imagenes/extraccion.png)

5. Por último eso debería extraer la base de datos de la página de la Escuela de Estadística de la Universidad de Costa Rica y debería verse de la siguiente manera:

![final](/imagenes/final.png)

Esto indica que la base puede ser cargada. Si es necesario se pueden aplicar transformaciones ya que esta es la base de datos cruda, por lo que se recomienda revisar con detalle los datos. 

Este proceso tiene la ventaja de que es reproducible con cualquier dirección web, lo que permite adaptar el dashboard a distintos tipos de datos y uso que se le quiera dar, especialmente en la visualización de indicadores.

## GitHub Actions

Por otro lado, este sistema de extracción está automatizado por medio de `GitHub Actions` el cual permite hacer la solicitud de los datos cada período de tiempo, el cual nosotros determinamos es cada mes. Esto significa que cada vez que la Escuela de Estadística sube un archivo de datos `.xlsx` del ICC, este código automáticamente extrae ese archivo y en el repositorio el archivo denominado `datos.xlsx` se va a actualizar con la última versión, lo cual permite que el usuario final tenga acceso a este archivo de datos sin necesidad de manualmente descargarlos. 

Para refrescar el repositorio:

```{git}
git pull origin desarollo
```

<span style="color: red; font-weight: bold;">NOTA</span>

Recordar estar en la rama creada para la replicación de este proceso. 

## Trabajo futuro

Para futuras implementaciones se recomienda explorar la forma de automatizar la creación del dashboard, para que así los usuarios no tengan que manualmente pasar el archivo a Power BI. 
Por otro lado, también se pueden crear archivos de `python` que realicen la limpieza de los datos y que estos se ejecuten mediante GitHub Actions. 

- [ ] Automatización de Power BI
- [ ] Automatización de Indicadores
