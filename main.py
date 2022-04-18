import pyautogui
import keyboard
import time

time.sleep(3)
pyautogui.press("space")

while True:
        # take screenshot of every frame in infinite loop:
        im = pyautogui.screenshot()
        # get COOrdinates of any white space(WS) of the screen:
        # pyautogui.MousePosition() or pyautogui.position()
        # get the current RGB values of WS on these found coordinates:
        screen = im.getpixel((214, 189))
        # get RGB values of distances befor  e the dino on following COOrdinates:
        # x vars for the trees AND we have 4x in case any is missed because of the increasing speed of the game
        x1 = im.getpixel((800, 277))
        x2 = im.getpixel((723, 277))
        x3 = im.getpixel((820, 277))
        x4 = im.getpixel((705, 277))
        # y vars for the birds:
        y1 = im.getpixel((752, 253))
        y2 = im.getpixel((765, 253))
        y3 = im.getpixel((723, 253))
        y4 = im.getpixel((705, 253))

        # if bg of the screen white:
        if screen[0] == 255:
            # if distance before dino not white:
            if x1[0] != 255 or x2[0] != 255 or x3[0] != 255 or x4[0] != 255 or y1[0] != 255 or y2[0] != 255 or y3[
                0] != 255 or y4[0] != 255:
                pyautogui.press("space")
                time.sleep(0.0001)

        # if bg of the screen black:
        else:
            # if distance before dino not black:
            if x1[0] != 0 or x2[0] != 0 or x3[0] != 0 or x4[0] != 0 or y1[0] != 0 or y2[0] != 0 or y3[0] != 0 or y4[0] != 0:
                pyautogui.press("space")
                time.sleep(0.0001)

        if keyboard.is_pressed("e"):
            break

