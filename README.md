# docker_flask_homework

Steps to to Dockerize the Flask application
1. create flask app with Dockerfile
2. Dockerfile should contain the following code:
  3. `FROM python:3.10-slim-buster`
  4. `WORKDIR /app`
  5. `COPY . /app/`
  6. `RUN pip install -r requirements.txt`
  7. `EXPOSE 5000`
  8. `CMD ["python", "app.py"]`
9. Run Docker command `docker build -t <name of image> .` to build the docker image and dockerize the container

