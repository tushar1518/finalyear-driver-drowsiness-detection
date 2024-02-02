import cv2
cap=cv2.VideoCapture()
while(cap.isOpened()):
    success,frame=cap.read()
    if not success:
        break
    frame=cv2.resize(frame,(600,400))
    cv2.putText(frame,"Live",(100,300))
    cv2.imshow("vid",frame)
