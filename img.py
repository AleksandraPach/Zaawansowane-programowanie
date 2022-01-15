import glob
import cv2
from scipt import detector

path = glob.glob("img/*jpg")

for filename in path:
    img = detector(cv2.imread(filename))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
