# titanic-prediction

Based on [Titanic: Prediction Competition](https://www.kaggle.com/c/titanic), this app allows users to input passenger information and run a prediction for the survival on the Titanic incident.

The backend consists on an api implemented with FastApi and containing a picked predicition model.

Running backend on docker:  
```
cd titanic-prediction  
docker build -f Dockerfile.api -t titanic-api .  
docker run --rm -p 5000:80 titanic-api  
```

The api documentation can be found on http://0.0.0.0:5000/docs

The frontend is a react app and can also run on a docker container:  
```
docker build -f Dockerfile.ui -t titanic-ui .
docker run --rm -p 3000:80 titanic-ui
```

Running the app with `docker-compose`:
```
docker-compose up --build
```