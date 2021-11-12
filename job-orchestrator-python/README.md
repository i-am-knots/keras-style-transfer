# Render Job Orchestrator

## Test
http://localhost:8080/new-job?bucket=test-bucket&style=style.jpg&sourceVid=test.mp4&iterations=25&frame=frame1000.jpg&size=480

http://localhost:8080/new-job?bucket=knots-style-transfer-dev&style=style.jpg&sourceVid=test.mp4&iterations=25&frame=frame1000.jpg&size=480


## Building Docker Image
Build the image
```
docker build -t orchestrator:0.0.1 .
```

### Run with Docker
Run and portforward the container with docker
```
docker run --expose=8081 orchestrator:0.0.1
```

### Deploy to kubernetes with kubectl
Run and portforward the container with kubectl
```
kubectl create namespace orchestrator
kubectl create deployment --image=orchestrator:0.0.1 orchestrator --namespace orchestrator
kubectl expose deployment orchestrator --port=8080 --name=orchestrator-service --namespace orchestrator
kubectl port-forward service/orchestrator-service 8080:8080 --namespace orchestrator
```

Delete and clean up
```
kubectl delete namespace orchestrator --cascade