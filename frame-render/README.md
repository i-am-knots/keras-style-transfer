# Render Frame
Microservice to render a single frame with an api to listen for paramaters

### Example API Request
```
HTTP GET - localhost:8082/render?bucket=gcs-bucket-name&style=style.jpg&source=test.png&iterations=10&size=720
```

### Test locally
```
cd frame_render
python3 render-api.py
```
