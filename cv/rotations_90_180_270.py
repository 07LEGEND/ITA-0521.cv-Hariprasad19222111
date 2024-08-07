import cv2
image=cv2.imread(r"C:\Users\91934\Documents\computervision\kholi.jpeg")
rotate_90=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
rotate_180=cv2.rotate(image,cv2.ROTATE_180)
rotate_270=cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("90 degree",rotate_90)
cv2.imshow("180 degree",rotate_180)
cv2.imshow("270_degree",rotate_270)
cv.waitkey(0)
