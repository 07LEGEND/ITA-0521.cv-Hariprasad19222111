import cv2
image=cv2.imread(r"C:\Users\91934\Documents\computervision\dhoni.jpeg")
gi=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gb=cv2.GaussianBlur(gi,(15,15),0)
cn=cv2.Canny(gi,100,200,0)
cv2.imshow("orignal image",image)
cv2.imshow("gray scale image",gi)
cv2.imshow("gaussian blur",gb)
cv2.imshow("canny",cn)
cv.waitkey(0)
