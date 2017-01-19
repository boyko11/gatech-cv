import numpy as np
import cv2

image = cv2.imread('1.wide.png')
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('1.wide.grayscale.png',grayscale_image)
image_blue = np.copy(image)[:, :, 0]
cv2.imwrite('1.wide.blue.png',image_blue)
image_green = np.copy(image)[:, :, 1]
cv2.imwrite('1.wide.green.png',image_green)
image_red = np.copy(image)[:, :, 2]
cv2.imwrite('1.wide.red.png',image_red)

print "DONE"

