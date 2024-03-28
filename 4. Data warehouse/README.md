## Data Warehouse

For this part I used Google cloud Storage, developed a bucket which was called data-lake-affiliates and following exactly a datalake structure divided into 4 domains:

- Workload: Arrives as is from the ingestion layer through mage.
- Landing: The information to be locked is landed, normally it is changed to parquet.
- Curated: The transformations are carried out with spark.
- Functional: The information is ready to be consumed in some Google BigQuery DWH.

![dwh](https://github.com/CusiTEC/Project-Course-Data-Engineering-/assets/104920177/1d88366a-d843-4cac-b37d-e7abf2ae73a2)

### DWH BigQuery

zoomcamp_dataengineer.db_afiliados.tb_afiliados

![dwh2](https://github.com/CusiTEC/Project-Course-Data-Engineering-/assets/104920177/c67ed42c-84d6-49f6-8688-1a80e1247d0b)
