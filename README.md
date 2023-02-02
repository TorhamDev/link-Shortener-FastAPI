# Link shortener with FastAPI
> a simple link shortener with FastAPI

My practice for using FastAPI.
In this exercise, a link shortening system is built and it is tried to be optimized as much as possible.

Technologies such as Docker and Redis are also used in this exercise.

## Technologies used:
![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)
![image](https://img.shields.io/badge/redis-CC0000.svg?&style=for-the-badge&logo=redis&logoColor=white)
![image](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![image](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)

# How to Run?
You can run this project in three ways. manually, using docker-compose and using Docker

## Manually
```bash

# clone the project
git clone https://github.com/TorhamDev/link-Shortener-FastAPI.git

cd link-Shortener-FastAPI

# install libs
pip install -r requirements.txt

# run the projct
uvicorn main:app --host 0.0.0.0 --port 8080
```

## Using docker-compose
```bash
# clone the project
git clone https://github.com/TorhamDev/link-Shortener-FastAPI.git

cd link-Shortener-FastAPI

# Run and build project
docker-compose up --build  -d

```


## Using docker 
```bash
# clone the project
git clone https://github.com/TorhamDev/link-Shortener-FastAPI.git

cd link-Shortener-FastAPI

# building docker image
docker build -t fast-api-link .

# run the project on 8080 port
docker run -d -p 8080:8080 fast-api-link
```



# License
[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)