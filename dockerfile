FROM python:3.10-slim-bullseye

RUN apt-get update\
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential default-libmysqlclient-dev \
    && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app
ENV JWT_SECRET=humpe_toh_hai_hi_no \
    MYSQL_HOST=localhost \
    MYSQL_USER=root \
    MYSQL_PASSWORD=mysql@123 \
    MYSQL_DB=feedback \
    MYSQL_PORT=3306

RUN pip install --no-cache-dir --requirement /app/requirements.txt

COPY . /app

EXPOSE 9000

CMD ["python3", "server.py"]