from frame import render_frame
from flask import Flask, json, request

api = Flask(__name__)

def test_render_frame(bucket, source, style):
    print("this is a mock render")
    print("the bucket is", bucket)
    print("the source is", source)
    print("the style is", style)


@api.route('/render', methods=['GET'])
def render_handler():
    bucket     = request.args.get('bucket')
    source     = request.args.get('source')
    style      = request.args.get('style')
    size       = request.args.get('size')
    iterations = request.args.get('iterations')
    
    render_frame(bucket, source, style, size, iterations)
    
    return "Frame render complete"

@api.route('/render-test', methods=['GET'])
def get_render_test():
    bucket = request.args.get('bucket')
    source = request.args.get('source')
    style  = request.args.get('style')
    size   = request.args.get('size')

    test_render_frame(bucket, source, style, size)
    return "Done"

if __name__ == '__main__':
    api.run(port=8082) 