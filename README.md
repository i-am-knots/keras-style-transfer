# keras-style-transfer
Repository for deploying a Keras Tensorflow nural style transfer implementation to GCP

## Render Frame
Microservice to render a single frame with an api to listen for paramaters

### Example API Request
```
HTTP GET - localhost:8080/render?bucket=gcs-bucket-name&style=style.jpg&source=test.png&iterations=10
```

### Test locally
```
cd frame_render
python3 render-api.py
```
