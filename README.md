# docker_flask_homework

## Part One: Dockerizing a Single Flask Application
Steps to Dockerize the Flask application
1. create flask app with Dockerfile
2. Dockerfile should contain the following code:
   
    3. `FROM python:3.10-slim-buster`
       
    5. `WORKDIR /app`
       
    7. `COPY . /app/`
       
    9. `RUN pip install -r requirements.txt`
        
    11. `EXPOSE 5000`
        
    13. `CMD ["python", "app.py"]`
        
9. Run Docker command `docker build -t <name of image> .` to build the docker image and `docker run -d -p 5001:5000 <name of image>` to run the image.

## Part Two: Multi-Container Setup with Docker Compose
Steps for Multi-Container Setup with Docker Compose
1. create 2 different folders with each containing a flask app, requirements/txt and Dockerfile
2. create docker-compose.yaml file that contains version, services, app name, build, ports and volumes. The following is an example:

          `version: '3'`
            `services:`
              `flask_app_1: #name of container`
                `build: ./flask1`
                `ports:`
                  `- "5001:5000"`
                `volumes:`
                  `- ./flask1:/app`
              `flask_app_2:`
               `build: ./flask2`
                `ports:`
                  `- "5002:5000"`
                `volumes:`
                 `- ./flask2:/app`

3. Run Docker compose commands `docker-compose build` to build images and `docker-compose up -d` to run containers.
