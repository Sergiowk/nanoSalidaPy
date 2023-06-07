## Install requirements
``` batch
pip install -r requirements.txt
```

## Build Docker image
- Start Docker Desktop
- Build image
``` batch
docker build -t local-mysql .
```
- Run container
``` batch
docker run -dp 3306:3306 local-mysql
```

## Batch instructions
- Feeding the DB 
``` batch
python .\batch_process.py
```

## Activate virtualenv
``` batch
.\python_modules\Scripts\activate.ps1
```

## Run the API
``` batch
python .\post_server.py
```

## Link to the API 

http://127.0.0.1:5000/drivers