## Build Docker Compose image

``` batch
docker-compose up
```

## Feed the DB 
``` batch
python .\db\batch_process.py
```

## Link to the API 

http://localhost:5000/

## Get the full list of drivers in the current season

http://localhost:5000/drivers


## Turn off the Docker images

``` batch
docker-compose down
```