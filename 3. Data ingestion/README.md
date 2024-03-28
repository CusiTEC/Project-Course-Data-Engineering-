## Data Ingestion

Para esta parte use GCP, tal cual lo vimos en el curso se uso una instancia de VM, la cual configuramos para instalar MAGE y realizar todo los procesos de orquestación.

MAGE permitio realizar el ETL de ingesta hacia Google Cloud Storage, previamente debemos tener definido el archivo .json y ademas de configurar el archivo io_config.yaml para establer una conexion.

Se puede visualizar los archivos usados del ETL de ingesta:

### data_loader.py
![python](https://github.com/CusiTEC/Project-Course-Data-Engineering-/assets/104920177/d8349508-6515-4a15-a8d8-f85118a16b2f)


### data_exporter.py
![python2](https://github.com/CusiTEC/Project-Course-Data-Engineering-/assets/104920177/51e0463e-35fd-4530-a545-1714d379a0bc)
