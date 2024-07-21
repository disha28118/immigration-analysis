import cv2
from mediapipe.python.solutions import face_detection
from mediapipe.python.solutions import drawing_utils

video=cv2.VideoCapture(0)
with face_detection.FaceDetection() as detector:
    while video.isOpened():
        status,frame=video.read()
        if not status:
            break

        frame.flags.writeable=False
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=detector.process(frame)
        frame.flags.writeable=True
        frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)

        if results.detections:
            print("faces detected")
            for detection in results.detections:
                drawing_utils.draw_detection(frame,detection)
        cv2.imshow("Face Detection",frame)
        if cv2.waitKey(10)==27:
            break
video.release()
