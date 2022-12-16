### Docker build & run

> docker build -t restapi-flask-python . <br>
> docker run -dp 80:80 --name flask-restapi -w /app -v ${PWD}:/app restapi-flask-python 