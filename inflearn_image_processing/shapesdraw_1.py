#일부 영역 색칠
#빈 스케치북 준비
import cv2
import numpy as np

img = np.zeros((480, 640, 3)) #가로 480, 세로 680, 3차원 형태의 공간을 0으로 채움

img[100:200, 200:300] = (255,255,255)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()