import cv2
face_cascade = cv2.CascadeClassifier(r"C:/Users/91934/Downloads/haarcascade_frontalface_default.xml")
image = cv2.imread(r"C:\Users\91934\Documents\computervision\kholi.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv2.imshow("img", image)
cv2.waitKey(0)


