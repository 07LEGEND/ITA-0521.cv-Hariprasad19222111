import cv2
import numpy as np
im_source=cv2.imread(r"C:\Users\91934\Documents\computervision\kholi.jpeg")
source=np.array([[141,131],[45,57],[111,212],[68,90]])
im_destination=cv2.imread(r"C:\Users\91934\Documents\computervision\dhoni.jpeg")
destination=np.array([[133,136],[111,112],[100,120],[100,200]])
h,status=cv2.findHomography(source,destination)
image_out=cv2.warpPerspective(im_source,h,(im_destination.shape[1],im_destination.shape[0]))
cv2.imshow("Source Image", im_source)
cv2.imshow("Destination Image", im_destination)
cv2.imshow("Warped Source Image", image_out)
cv2.waitKey(0)

                
