# Link shortener with FastAPI
> a simple link shortener with FastAPI

My practice for using FastAPI.
In this exercise, a link shortening system is built and it is tried to be optimized as much as possible.

Technologies such as Docker and Redis are also used in this exercise.


# How to Run?
You can run this project in two ways, manually and using Docker

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