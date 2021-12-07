import cv2
import os
import glob

import IPython.display as display
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12, 12)
mpl.rcParams['axes.grid'] = False

import numpy as np
import PIL.Image
import time
import functools

import tensorflow_hub as hub
import tensorflow as tf
# Load compressed models from tensorflow_hub
os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'
from tensorflow import keras
from tensorflow.keras.applications import vgg19

def render_frame():

    def tensor_to_image(tensor):
        tensor = tensor*255
        tensor = np.array(tensor, dtype=np.uint8)
        if np.ndim(tensor)>3:
            assert tensor.shape[0] == 1
            tensor = tensor[0]
        return PIL.Image.fromarray(tensor)

    # Load content and style images (see example in the attached colab).
    style_image = plt.imread("style-images/style.jpg")
    print("SET IMAGES SUCCESS")
    # Convert to float32 numpy array, add batch dimension, and normalize to range [0, 1]. Example using numpy:
    
    style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255.
    # Optionally resize the images. It is recommended that the style image is about
    # 256 pixels (this size was used when training the style transfer network).
    # The content image can be any size.
    style_image = tf.image.resize(style_image, (256, 256))

    # Load image stylization module.
    hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

    # Stylize image.
    for file in glob.glob("source-frames/*.jpg"):
        print(file)
        content_image = plt.imread(file)
        content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255.
        outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
        output_name = "output/" + file
        tensor_to_image(outputs[0]).save(output_name)



def make_frames():
    # Get the source video file from GCS
 
    # Make frames from video with set FPS
    video_capture = cv2.VideoCapture("test.mp4")
    video_capture.set(cv2.CAP_PROP_FPS, 30)

    saved_frame_name = 0

    while video_capture.isOpened():
        frame_is_read, frame = video_capture.read()

        if frame_is_read:
            cv2.imwrite(f"source-frames/frame{str(saved_frame_name)}.jpg", frame)
            
            saved_frame_name += 1

        else:
            print("Could not read the frame.")
            return

def build_video():
    img_array = []
    for filename in glob.glob('output/source-frames/*.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)

    out = cv2.VideoWriter('output/test.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, size)
 
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

def main():
    os.mkdir("source-frames")
    os.mkdir("output")
    os.mkdir("output/source-frames")
    make_frames()
    render_frame()
    build_video()


main()