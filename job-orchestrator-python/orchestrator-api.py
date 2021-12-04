import requests
from google.cloud import storage
from flask import Flask, request
from preppod import new_prep_pod

api = Flask(__name__)

def prep_video(bucket, sourceVid):
    response = requests.get('http://localhost:8081/prep-video?bucket=' + bucket + '&source=' + sourceVid)
    return response

def render_frame(bucket, frame, style, iterations, size):
    response = requests.get('http://localhost:8082/render?bucket=' + bucket + '&source=' + frame + '&style=' + style + '&iterations=' + iterations + "&size=" + size)
    return response

def get_jobs(bucket):
    # Get the source frames from GCS
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket)
    totalFrames = []

    for blob in storage_client.list_blobs(bucket, prefix='source-frames/'):
        totalFrames.append(blob.name)  

    jobs = [totalFrames[x:x+5] for x in range(0, len(totalFrames), 5)]

    return jobs
    
    

@api.route('/new-job', methods=['GET'])
def new_job_handler():
    bucket     = request.args.get('bucket')
    sourceVid  = request.args.get('sourceVid')
    style      = request.args.get('style')
    iterations = request.args.get('iterations')
    frame      = request.args.get('frame')
    size       = request.args.get('size')
      
    print("Starting Job")
    #prep_video(bucket, sourceVid)
    print("Video Prep Complete. Source frames output to: " + bucket + "/source-frames/")
    #jobs = get_jobs(bucket)
    print("Successfully read source frames from GCS")
    api_response = new_prep_pod()

    
    
    #render_frame(bucket, frame, style, iterations, size)
    #print("Frame Render Complete")

    return str(api_response)


if __name__ == '__main__':
    api.run(port=8080) 