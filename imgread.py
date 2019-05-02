import numpy as np 
import cv2
inputs=cv2.imread('img/cute.jpg')
cv2.imshow('img',inputs)

#Dimension of image
print(inputs.shape)
print('Height of img:',int(inputs.shape[0]))
print('Width of img:',int(inputs.shape[1]))

#write image
cv2.imwrite('cute1.png',inputs)
cv2.waitKey()
cv2.destroyAllWindows()

