import cv2
img = cv2.imread("logo.png")
cv2.imshow("logo sample",img)
cv2.imwrite("Logo.png",img)
cv2.waitKeY(0)
cv2.destroyAllWindows()
