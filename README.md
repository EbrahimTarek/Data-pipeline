# Data-pipeline
ETL with python 

## The pipeline
![image](https://user-images.githubusercontent.com/93515671/230722315-af3fca53-924c-436c-a62c-f2e29fc778bd.png)

## Steps
- Download the ZIP file containing all of the sales transactions, then convert it into a CSV file. [Extract](https://github.com/EbrahimTarek/Data-pipeline/blob/main/extract.py)
- Establish a Postgresql connection to transfer data from a CSV file to the Postgres database SQL. [Base](https://github.com/EbrahimTarek/Data-pipeline/blob/main/Base.py)
- Create tables in Postgres database SQL . one for raw data & another for transformed tables.[Tables](https://github.com/EbrahimTarek/Data-pipeline/blob/main/tables.py)
- Apply various transformations to a CSV file then uploading data to the "ppr_raw_all" table in Postgresql. [Transform](https://github.com/EbrahimTarek/Data-pipeline/blob/main/transform.py)
- In the database, load data from the "ppr_raw_all" table to the "ppr_clean_all" table. [load](https://github.com/EbrahimTarek/Data-pipeline/blob/main/load.py)
- [Create insights view for stakeholders].(https://github.com/EbrahimTarek/Data-pipeline/blob/main/create_insights_view.py)
