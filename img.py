import cv2
import imutils
from scipt import detector

img1 = cv2.imread('img/img1.jpg')
img1 = imutils.resize(img1, width=450)
img1 = detector(img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

img2 = cv2.imread('img/img2.jpg')
img2 = imutils.resize(img2, width=500)
img2 = detector(img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

img3 = cv2.imread('img/img3.jpg')
img3 = imutils.resize(img3, width=700)
img3 = detector(img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

img4 = cv2.imread('img/img4.jpg')
img4 = imutils.resize(img4, width=700)
img4 = detector(img4)
cv2.waitKey(0)
cv2.destroyAllWindows()