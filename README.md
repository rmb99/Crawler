# Kilid interview

Crawler for crawling dollar price and plot charts.

## Getting started
For start crawling first create db in your docker compose:
1. docker-compose up


### Create database:
2. docker exec -it pg-kilid createdb -U pg kilid

### Install requirements
3. pip install -r requirements.txt

### Creat tables
4. python create_model.py

### Crawl the web : 
5. python dollar.py

### Plot the charts:
6. python plot.py



