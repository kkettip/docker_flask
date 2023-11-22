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

## Docker Commands

To build docker image: docker build -t <name of image> . name of image: flaskapp1

To list the images: docker images

To run image: docker run -d -p 5001:5000 <name of image> (docker run -p <host-port>:<container-port> <image-name>)

To get container ID and to see the containers that are running: docker ps

To stop the container: docker stop <container id from list displayed by docker ps>

To remove a container: docker rm <container-id>

To delete all containers: docker system prune -a -f 

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

## Docker Compose Commands:

To build images: docker-compose build

To run containers: docker-compose up -d

To stop containers: docker-compose down

To list containers: docker-compose ps

To remove containers: docker-compose rm

To remove volumes: docker-compose down -v

To delete all: docker-compose down -v --rmi all --remove-orphans

## Observations and Reflections:   
Docker Compose differs from using Docker alone because Docker compose allows mulitiple apps in containers to be run simultaneously. While Docker alone allows for one app to be run at a time. With Docker compose the image does not have to be rebuild everytime changes are made because `docker-compose.yaml` file has the code `volumes` that allows for the detection and update of changes.  Docker alone does not contain the `docker-compose.yaml` file and the image have to be rebuild everytime changes are made.

No challenges or errors occurred when setting up the containers. 
