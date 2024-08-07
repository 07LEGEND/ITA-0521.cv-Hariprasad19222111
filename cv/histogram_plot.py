import cv2
from matplotlib import pyplot as plt
image=cv2.imread(r"C:\Users\91934\Documents\computervision\dhoni.jpeg")
b,g,r=cv2.split(image)
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()
cv2.imshow("image",image)
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
cv.waitkey(0)
