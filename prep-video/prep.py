import cv2
import os
from google.cloud import storage


def make_frames(bucket, source):
    # Get the source video file from GCS
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket)
    blob = bucket.blob("source-videos/" + source)
    blob.download_to_filename(source)
    
    # Make frames from video with set FPS
    video_capture = cv2.VideoCapture(source)
    video_capture.set(cv2.CAP_PROP_FPS, 60)

    saved_frame_name = 0

    while video_capture.isOpened():
        frame_is_read, frame = video_capture.read()

        if frame_is_read:
            destination_blob_name = f"source-frames/frame{str(saved_frame_name)}.jpg"


            cv2.imwrite(f"frame{str(saved_frame_name)}.jpg", frame)
            
            blob = bucket.blob(destination_blob_name)
            blob.upload_from_filename(f"frame{str(saved_frame_name)}.jpg")
            os.remove(f"frame{str(saved_frame_name)}.jpg")

            saved_frame_name += 1


        else:
            print("Could not read the frame.")
            return

def main():
    make_frames(bucket, source)

main()