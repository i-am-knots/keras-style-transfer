import requests
from flask import Flask, json, request

api = Flask(__name__)

def prep_video(bucket, sourceVid):
    response = requests.get('http://localhost:8081/prep-video?bucket=' + bucket + '&source=' + sourceVid)
    return response

def render_frame(bucket, frame, style, iterations):
    response = requests.get('http://localhost:8082/render?bucket=' + bucket + '&source=' + frame + '&style=' + style + '&iterations=' + iterations)
    return response


@api.route('/new-job', methods=['GET'])
def new_job_handler():
    bucket     = request.args.get('bucket')
    sourceVid  = request.args.get('sourceVid')
    style      = request.args.get('style')
    iterations = request.args.get('iterations')
    frame      = request.args.get('frame')
    
    # prepVideoResponse   = prep_video(bucket, source)
    # renderFrameResponse = render_frame(bucket, source, style, size, iterations)
    
    print("Starting Job")
    prep_video(bucket, sourceVid)
    print("Video Prep Complete")
    render_frame(bucket, frame, style, iterations)
    print("Frame Render Complete")

    return "render job done"


if __name__ == '__main__':
    api.run(port=8080) 