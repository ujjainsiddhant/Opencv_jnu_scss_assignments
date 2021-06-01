import cv2 as cv
path=r'C:\Users\UJJAIN\Desktop\python program\opencv\photos\SIDD.jpg'
img=cv.imread(path , 1)
cv.imshow('MY PIC',img)
cv.waitKey(0)