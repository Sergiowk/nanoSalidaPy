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