import cv2
#reading image
image = cv2.imread("dr.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_image = 255 - gray_image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=255.0)
ims0  = cv2.resize(image,(600,600))
cv2.imshow("Original Image", ims0)
ims = cv2.resize(pencil_sketch,(600,600))
cv2.imshow("Pencil Sketch of Dog", ims)

cv2.waitKey(0)
