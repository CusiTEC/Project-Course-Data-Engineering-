## Data Warehouse

Para esta parte use Google cloud Storage, desarrolle un bucket el cual se llamo data-lake-afiliados y siguiendo justamente una estructura de datalake divide en 4 dominios:

- Workload: Llega como esta de la capa de ingesta por medio de mage.
- Landing: Se aterriza la información a trabar normalmente se cambia a parquet.
- Curated: Se proceden a realizar las transformaciones con spark.
- Functional: Se tiene lista la información para consumirse en algun DWH de Google BigQuery.

![dwh](https://github.com/CusiTEC/Project-Course-Data-Engineering-/assets/104920177/1d88366a-d843-4cac-b37d-e7abf2ae73a2)

### DWH BigQuery

zoomcamp_dataengineer.db_afiliados.tb_afiliados

![dwh2](https://github.com/CusiTEC/Project-Course-Data-Engineering-/assets/104920177/c67ed42c-84d6-49f6-8688-1a80e1247d0b)
