## Table of contents
* [Project Details](#Project-Details)

## Project-Details
Airflow Mini-Project DAG Scheduling
In this project, we will use Apache Airflow to create a data pipeline to extract online stock market data and deliver analytical results with Yahoo Finance as the data source. Yahoo Finance provides intra-day market price details down a one-minute interval.
Project is created using:
* Docker Desktop installed and should be running
* puckel/docker-airflow:1.10.9 image comes with python 3.7.x (Required Libraries: yfinance,pandas)

Execute docker commands as follows

```
sudo docker compose up --build
sudo docker ps - for listing running containers
sudo docker exec -it <container-id> /bin/bash - to access and run commands inside container

```

Access airflow UI on http:0.0.0.0:8080 and turn on/trigger DAG . On windows access the url localhost:8080


![Alt text](/Screenshots/airflowwebserver.PNG?raw=true "Airflow webserver")

