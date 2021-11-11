# Video Prep microservice
Takes a given video from a location, breaks it into frames using the python ffmpeg wrapper.

## Running Locally
```
pip install requirements.txt
sudo apt-get update
sudo apt-get install ffmpeg libsm6 libxext6  -y
python3 prep-video-api.py
```

### Test API
```
http://localhost:8081/prep-video?bucket=test-bucket&source=test.mp4
```

## Building Docker Image
Build the image
```
docker build -t prep-video:0.0.1 .
```

### Run with Docker
Run and portforward the container with docker
```
docker run --expose=8081 prep-video:0.0.1
```

### Deploy to kubernetes with kubectl
Run and portforward the container with kubectl
```
kubectl create namespace prep-video
kubectl create deployment --image=prep-video:0.0.1 prep-video --namespace prep-video
kubectl expose deployment prep-video --port=8081 --name=prep-video-service --namespace prep-video
kubectl port-forward service/prep-video-service 8081:8081 --namespace prep-video
```

Delete and clean up
```
kubectl delete namespace prep-video --cascade
```






