import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui

# 750, 500, 1050, 700
tile_cord1 = [(780, 650), (850, 650), (930, 650), (1010, 650)]
tile_cord2 = [(780, 500), (850, 500), (930, 500), (1010, 500)]
tile_cord3 = [(780, 530), (850, 530), (930, 530), (1010, 530)]
tile_cord4 = [(780, 560), (850, 560), (930, 560), (1010, 560)]
tile_cord5 = [(780, 590), (850, 590), (930, 590), (1010, 590)]
tile_cord = [tile_cord1, tile_cord2, tile_cord3, tile_cord4, tile_cord5]
check_cord = [(10, 30), (10, 105), (10, 180), (10, 255)]

screen = np.array(ImageGrab.grab(bbox=(750, 650, 1050, 700)))
screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
for i in range(4):
    if screen[check_cord[i][0]][check_cord[i][1]] < 170:
        pyautogui.click(tile_cord1[i])
        break
pkt = 1
k = 2
while True:
    if pkt % 300 == 0 or pkt % 500 == 0:
        tile_cord2 = tile_cord[k]
        k = k + 1

    screen = np.array(ImageGrab.grab(bbox=(750, 480, 1050, 500)))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    for i in range(4):
        if screen[check_cord[i][0]][check_cord[i][1]] < 160:
            pyautogui.click(tile_cord2[i])
            pkt += 1
            print(pkt)


