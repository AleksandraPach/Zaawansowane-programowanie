import pytesseract
import cv2


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
img1 = cv2.imread('img/img1.jpg')
img2 = cv2.imread('img/img2.jpg')
img3 = cv2.imread('img/img3.jpg')
img4 = cv2.imread('img/img4.jpg')
img5 = cv2.imread('img/img5.jpg')

img_convert = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


def read_image(img) -> str:
    return pytesseract.image_to_string(img)


print(read_image(img1))
print(read_image(img_convert))
# print(read_image(img2))
# print(read_image(img3))
# print(read_image(img4))
# print(read_image(img5))
