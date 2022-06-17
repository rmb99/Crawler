# Kilid interview

Crawler for crawling dollar price and plot charts.

## Getting started
For start crawling first create db in your docker compose:
1. docker-compose up
2. Install requirements

### Create database:
3. docker exec -it pg-kilid createdb -U pg kilid

### Creat tables
4. python create_model.py

### Crawl the web : 
5. python dollar.py

### Plot the charts:
6. python plot.py



