import cv2
import numpy as np

img = np.zeros((480, 640, 3)) #가로 480, 세로 680, 3차원 형태의 공간을 0으로 채움

COLOR = (255,255,0) #색깔
THICKNESS = 3 #두께

cv2.rectangle(img, (100,100), (200,200), COLOR, THICKNESS)
#그릴 위치, 왼쪽 위 좌표, 오른쪽 아래 좌표, 색깔, 두께
cv2.rectangle(img, (300,100), (400,200), COLOR, cv2.FILLED)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()