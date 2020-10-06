import cv2
import numpy as np
import pyautogui

img = pyautogui.screenshot()
image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
cv2.imwrite("screenshot.png", image)
cv2.imshow("screenshot", image)

