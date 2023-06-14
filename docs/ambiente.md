# Configuración

# Index
+ [Prerrequisitos](#prerrequisitos)
+ [GitHub](#GitHub)
+ [Creación del ambiente](#creación-del-ambiente)

## Prerrequisitos 

+ Python
+ Anaconda
+ PowerBI

## GitHub

1. Inicialmente se debe descargar `git` en la computadora, para esto pueden accesar al siguiente, descargarlo y seguir las instrucciones de instalación correspondiente. Este está disponible sistemas Windows o MacOS. Por otro lado, **_es necesario contar con una cuenta de GitHub_**. 

- [Descargar Git](https://git-scm.com/downloads)

2. Ahora, para configurar el repositorio de datos:

    **1.1** Abrir Microsoft PowerShell un interpretador
    ![Interpretadores](/imagenes/power.png)

    **1.2** Una vez abierto, abran la ubicación donde quieren clonar la carpeta del repositorio, por ejemplo: Documentos o Escritorio. Para eso, se ejecuta el siguiente comando
    
    ```{powershell}
    cd 'C:\Users\Marco\Documents'
    ```
    **1.3** Ahora, para clonar el repositorio ejecutan el siguiente comando en el interpretador:

    ```{git}
    git clone https://github.com/antonioespinoza98/ICC-dashboard.git
    ``` 
    <span style="color: red; font-weight: bold;">NOTA</span>
    Personas externas **no colaboradores** de la Escuela de Estadística de la Universidad de Costa Rica que deseen utilizar este repositorio, deberán primero utilizar la opción `Fork` en GitHub para utilizar este repositorio, debido a que esto protege el código original y permite la colaboración abierta mediante *pull requests*.

    ![fork](/imagenes/fork.png) 

    Una vez que se haya realizado esto, el comando `git clone` debería ser el URL del repositorio en su cuenta. 

    **1.4** Una vez que se tenga el repositorio de datos en la computadora local, se puede utilizar el interpretador de confianza para manipular el código, como Visual Studio Code.

    **1.5** También es importante que si está trabajando de forma local con el repositorio, debe crear una rama de trabajo propia donde pueda guardar los cambios. 

    ```{git}
    checkout branch -b marco
    ```

## Creación del ambiente

Una vez que se tenga configurado el repositorio de forma local, hay que crear el ambiente. El ambiente en Python consiste en una forma de manejar las versiones de Python y los paquetes se que van a utilizar para el desarrollo del código, esto permite ajustar la configuración ante un eventual *bug*.

1. Primeramente, asegurarse que el archivo `config.yml` esté disponible en los archivos, luego, correr el siguiente comando:

```{git}
conda env create -f config.yml
```





















