import cv2

def make_frames(bucket, source):
    video_capture = cv2.VideoCapture(source)
    video_capture.set(cv2.CAP_PROP_FPS, 60)

    saved_frame_name = 0

    while video_capture.isOpened():
        frame_is_read, frame = video_capture.read()

        if frame_is_read:
            cv2.imwrite(f"../frame-render/source-images/frame{str(saved_frame_name)}.jpg", frame)
            saved_frame_name += 1

        else:
            print("Could not read the frame.")
            return