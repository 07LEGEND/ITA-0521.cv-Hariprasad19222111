import cv2
video=cv2.VideoCapture(r"C:\Users\91934\Documents\computervision\WhatsApp Video 2024-07-24 at 08.51.49_b80473a7.mp4")
while True:
    ret,frame=video.read()
    cv2.imshow("out put",frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cap.release()


