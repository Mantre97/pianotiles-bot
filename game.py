import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui

tile_cord_start = [(780, 650), (850, 650), (930, 650), (1010, 650)]
tile_cord_game = [(780, 500), (850, 500), (930, 500), (1010, 500)]
check_cord = [(10, 30), (10, 105), (10, 180), (10, 255)]


def update_tile_cord_game(number):
    for counter, value in enumerate(tile_cord_game):
        tile_cord_game[counter] = (value[0], value[1] + number)


screen = np.array(ImageGrab.grab(bbox=(750, 650, 1050, 700)))
screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
for i in range(4):
    if screen[check_cord[i][0]][check_cord[i][1]] < 170:
        pyautogui.click(tile_cord_start[i])
        break
pt = 1

while True:
    if pt % 250 == 0:
        update_tile_cord_game(30)

    screen = np.array(ImageGrab.grab(bbox=(750, 480, 1050, 500)))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    for i in range(4):
        if screen[check_cord[i][0]][check_cord[i][1]] < 160:
            pyautogui.click(tile_cord_game[i])
            print(pt)
            pt += 1
