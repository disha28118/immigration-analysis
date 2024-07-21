import cv2

video=cv2.VideoCapture(r"C:\Users\Hp\OneDrive\Pictures\Snapchat-793221183.mp4")
while True:
    status,frame=video.read()
    print(status,frame)
    if not status:
        break
    #make changes from this line
    newframe=frame*10
    bw=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("video frame",frame)
    cv2.imshow("new video frame",newframe)
    cv2.imshow("b/w",bw)
    if cv2.waitKey(1)==27:
        break
    video.release()
    cv2.destroyAllWindows()
