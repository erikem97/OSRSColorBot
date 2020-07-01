import numpy as np
from PIL import ImageGrab
import cv2
import time
import random
import pyautogui as pg
time.sleep(2)


while True:
    printscreen = ImageGrab.grab()
    time.sleep(0.2)
    x,y = pg.position()
    print(x, y)



