import cv2

video=cv2.VideoCapture(0)
codec=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter("output.avi",codec,20.0,(640,480))
while True:
    status,frame=video.read()
    print(status,frame)
    if not status:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    output.write(gray)
    cv2.imshow("video frame",frame)
    if cv2.waitKey(1)==27:
        break
video.release()
output.release()
cv2.destroyAllWindows()