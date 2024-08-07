import cv2
import numpy as np
image=cv2.imread(r"C:\Users\91934\Documents\computervision\dhoni.jpeg")
gi=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
kernal= np.ones((5,5),np.uint8)
dilated_image=cv2.dilate(gi,kernal,iterations=1)
cv2.imshow("gray scale",gi)
cv2.imshow("dialted image",dilated_image)
cv2.waitkey(0)
