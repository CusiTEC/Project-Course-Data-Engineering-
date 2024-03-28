## Data Ingestion

For this part I used GCP, as we saw in the course, a VM instance was used, which we configured to install MAGE and carry out all the orchestration processes.

MAGE allowed us to perform the ingestion ETL towards Google Cloud Storage, previously we must have defined the .json file and in addition to configure the io_config.yaml file to establish a connection.

You can view the files used from the ingest ETL:
### data_loader.py
![python](https://github.com/CusiTEC/Project-Course-Data-Engineering-/assets/104920177/d8349508-6515-4a15-a8d8-f85118a16b2f)


### data_exporter.py
![python2](https://github.com/CusiTEC/Project-Course-Data-Engineering-/assets/104920177/51e0463e-35fd-4530-a545-1714d379a0bc)
