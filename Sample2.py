import cv2
image = cv2.imread("sample1.jpg")
grayImg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite("GrayImg.jpg",grayImg)
cv2.imshow("Original",image)
cv2.imshow("GrayImg",grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
