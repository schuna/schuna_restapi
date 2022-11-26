### Docker build & run

> docker build -t restapi-flask-python . <br>
> docker run -dp 5000:5000 --name flask-restapi -w /app -v ${PWD}:/app restapi-flask-python 