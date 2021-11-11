from prep import make_frames
from flask import Flask, json, request

api = Flask(__name__)


@api.route('/prep-video', methods=['GET'])
def video_prep_handler():
    bucket     = request.args.get('bucket')
    source     = request.args.get('source')
    make_frames(bucket, source)
    return "Prep video to frames complete"

if __name__ == '__main__':
    api.run(port=8081) 