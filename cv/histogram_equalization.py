import cv2
image=cv2.imread(r"C:\Users\91934\Documents\computervision\kholi.jpeg")
gi=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
equalization=cv2.equalizeHist(gi)
cv2.imshow("image",image)
cv2.imshow("gray scale",gi)
cv2.imshow("equalization",equalization)
cv.waitkey(0)
