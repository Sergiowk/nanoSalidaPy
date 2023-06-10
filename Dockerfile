FROM python:3

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#Running the API Sever
CMD [ "python", "post_server.py" ]

