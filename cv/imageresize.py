import cv2
image=cv2.imread(r"C:\Users\91934\Documents\computervision\dhoni.jpeg")
big_resize=cv2.resize(image,(600,600))
sma_resize=cv2.resize(image,(300,300))
cv2.imshow("big resize image",big_resize)
cv2.imshow("small resize image",sma_resize)
cv2.waitkey(0)
