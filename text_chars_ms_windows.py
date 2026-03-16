""" DRAW TEXT CHARACTERS | MICROSOFT WINDOWS (v1.0) """
""" WRITTEN BY DOGAN YIGIT YENIGUN (toUpperCase78) """
import numpy as np
import cv2
from text_chars_ms_windows_draw_bg import calculate_bg_text_chars_ms_windows

def draw_text_chars_ms_windows(img, text="Your text goes here.", color=(255,255,255), x=10, y=10, s=2, bg=False):
    x_init = x
    if len(text) == 0:    # Do nothing if the text is empty
        return img
    if bg == True:
        calculate_bg_text_chars_ms_windows(img, text, color, x, y, s)
    for letter in text:
        # print(ord(letter), end="  ")
        if ord(letter) == 10:      # new line
            x = x_init;   y += s*13
        elif ord(letter) == 32:    # space
            x += s*3
        elif ord(letter) == 33:    # exclamation mark
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*8)), (x+(s*1)-1,y+(s*9)-1), color, -1)
            x += s*2
        elif ord(letter) == 34:    # double quote
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y), (x+(s*4)-1,y+(s*3)-1), color, -1)
            x += s*5
        elif ord(letter) == 35:    # hashtag
            cv2.rectangle(img, (x+(s*1),y), (x+(s*2)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y), (x+(s*5)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*2)), (x+(s*6)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*6)), (x+(s*6)-1,y+(s*7)-1), color, -1)
            x += s*7
        elif ord(letter) == 36:    # dollar sign
            cv2.rectangle(img, (x+(s*2),y), (x+(s*3)-1,y+(s*10)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*2)), (x+(s*5)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*1)), (x+(s*4)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*2)), (x+(s*1)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*4)), (x+(s*2)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*5)), (x+(s*4)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*6)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*7)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            x += s*6
        elif ord(letter) == 37:    # percentage
            cv2.rectangle(img, (x+(s*1),y), (x+(s*3)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*2)), (x+(s*3)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*1)), (x+(s*4)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*7)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*6)), (x+(s*2)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*5)), (x+(s*3)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*4)), (x+(s*4)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*3)), (x+(s*5)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*2)), (x+(s*6)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*6),y+(s*1)), (x+(s*7)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*7)), (x+(s*4)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*6)), (x+(s*6)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*8)), (x+(s*6)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*6),y+(s*7)), (x+(s*7)-1,y+(s*8)-1), color, -1)
            x += s*8
        elif ord(letter) == 38:    # ampersand
            cv2.rectangle(img, (x+(s*1),y), (x+(s*2)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*1)), (x+(s*3)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*2)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*5)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*3)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*5)), (x+(s*3)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*5)), (x+(s*5)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*6)), (x+(s*4)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*8)), (x+(s*5)-1,y+(s*9)-1), color, -1)
            x += s*6
        elif ord(letter) == 39:    # apostrophe
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*3)-1), color, -1)
            x += s*2
        elif ord(letter) == 40:    # open parentheses
            cv2.rectangle(img, (x+(s*1),y), (x+(s*2)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*10)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*10)), (x+(s*2)-1,y+(s*11)-1), color, -1)
            x += s*3
        elif ord(letter) == 41:    # close parentheses
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*1)), (x+(s*2)-1,y+(s*10)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*10)), (x+(s*1)-1,y+(s*11)-1), color, -1)
            x += s*3
        elif ord(letter) == 42:    # asterisk
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*3)), (x+(s*1)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*2)), (x+(s*2)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*1)), (x+(s*3)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*3)), (x+(s*3)-1,y+(s*4)-1), color, -1)
            x += s*4
        elif ord(letter) == 43:    # plus
            cv2.rectangle(img, (x,y+(s*5)), (x+(s*5)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*3)), (x+(s*3)-1,y+(s*8)-1), color, -1)
            x += s*6
        elif ord(letter) == 44:    # comma
            cv2.rectangle(img, (x,y+(s*9)), (x+(s*1)-1,y+(s*10)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*2)-1,y+(s*9)-1), color, -1)
            x += s*3
        elif ord(letter) == 45:    # minus (hyphen)
            cv2.rectangle(img, (x,y+(s*5)), (x+(s*2)-1,y+(s*6)-1), color, -1)
            x += s*3
        elif ord(letter) == 46:    # full stop
            cv2.rectangle(img, (x,y+(s*8)), (x+(s*1)-1,y+(s*9)-1), color, -1)
            x += s*2
        elif ord(letter) == 47:    # forward slash
            cv2.rectangle(img, (x,y+(s*7)), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*5)), (x+(s*2)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*3)), (x+(s*3)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y), (x+(s*4)-1,y+(s*3)-1), color, -1)
            x += s*5
        elif ord(letter) == 48:    # number 0
            cv2.rectangle(img, (x+(s*1),y), (x+(s*4)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*1)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            x += s*6
        elif ord(letter) == 49:    # number 1
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*2)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y), (x+(s*3)-1,y+(s*9)-1), color, -1)
            x += s*4
        elif ord(letter) == 50:    # number 2
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y), (x+(s*4)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*1)), (x+(s*5)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*4)), (x+(s*4)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*5)), (x+(s*3)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*6)), (x+(s*2)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*7)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*8)), (x+(s*5)-1,y+(s*9)-1), color, -1)
            x += s*6
        elif ord(letter) == 51:    # number 3
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y), (x+(s*4)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*1)), (x+(s*5)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*4)), (x+(s*4)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*5)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*7)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            x += s*6
        elif ord(letter) == 52:    # number 4
            cv2.rectangle(img, (x+(s*3),y), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*6)), (x+(s*5)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*1)), (x+(s*3)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*2)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*5)), (x+(s*1)-1,y+(s*6)-1), color, -1)
            x += s*6
        elif ord(letter) == 53:    # number 5
            cv2.rectangle(img, (x,y), (x+(s*5)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*4)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*4)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*7)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            x += s*6
        elif ord(letter) == 54:    # number 6
            cv2.rectangle(img, (x+(s*1),y), (x+(s*4)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*1)), (x+(s*5)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*4)), (x+(s*4)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*5)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            x += s*6
        elif ord(letter) == 55:    # number 7
            cv2.rectangle(img, (x,y), (x+(s*5)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*1)), (x+(s*5)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*2)), (x+(s*4)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*4)), (x+(s*3)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*6)), (x+(s*2)-1,y+(s*9)-1), color, -1)
            x += s*6
        elif ord(letter) == 56:    # number 8
            cv2.rectangle(img, (x+(s*1),y), (x+(s*4)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*4)), (x+(s*4)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*5)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*1)), (x+(s*5)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*5)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            x += s*6
        elif ord(letter) == 57:    # number 9
            cv2.rectangle(img, (x+(s*1),y), (x+(s*4)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*4)), (x+(s*4)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*1)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*7)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            x += s*6
        elif ord(letter) == 58:    # colon
            cv2.rectangle(img, (x,y+(s*8)), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*3)), (x+(s*1)-1,y+(s*4)-1), color, -1)
            x += s*2
        elif ord(letter) == 59:    # semicolon
            cv2.rectangle(img, (x,y+(s*9)), (x+(s*1)-1,y+(s*10)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*2)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*2)-1,y+(s*4)-1), color, -1)
            x += s*3
        elif ord(letter) == 60:    # less than
            cv2.rectangle(img, (x+(s*3),y+(s*2)), (x+(s*4)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*3)), (x+(s*3)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*4)), (x+(s*2)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*5)), (x+(s*1)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*6)), (x+(s*2)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*7)), (x+(s*3)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            x += s*5
        elif ord(letter) == 61:    # equal sign
            cv2.rectangle(img, (x,y+(s*4)), (x+(s*5)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*6)), (x+(s*5)-1,y+(s*7)-1), color, -1)
            x += s*6
        elif ord(letter) == 62:    # greater than
            cv2.rectangle(img, (x,y+(s*2)), (x+(s*1)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*2)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*4)), (x+(s*3)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*5)), (x+(s*4)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*6)), (x+(s*3)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*7)), (x+(s*2)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*8)), (x+(s*1)-1,y+(s*9)-1), color, -1)
            x += s*5
        elif ord(letter) == 63:    # question mark
            cv2.rectangle(img, (x+(s*1),y), (x+(s*4)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*1)), (x+(s*5)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*4)), (x+(s*4)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*5)), (x+(s*3)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*8)), (x+(s*3)-1,y+(s*9)-1), color, -1)
            x += s*6
        elif ord(letter) == 64:    # at sign
            cv2.rectangle(img, (x+(s*3),y), (x+(s*7)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*7),y+(s*1)), (x+(s*9)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*8),y+(s*2)), (x+(s*9)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*9),y+(s*3)), (x+(s*10)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*7),y+(s*6)), (x+(s*10)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*6)), (x+(s*6)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*4)), (x+(s*4)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*3)), (x+(s*7)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*6),y+(s*4)), (x+(s*7)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*1)), (x+(s*3)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*2)), (x+(s*2)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*3)), (x+(s*1)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*7)), (x+(s*2)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*3)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*9)), (x+(s*8)-1,y+(s*10)-1), color, -1)
            x += s*11
        elif ord(letter) == 65:    # capital A
            cv2.rectangle(img, (x,y+(s*7)), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*4)), (x+(s*2)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*2)), (x+(s*3)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y), (x+(s*4)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*2)), (x+(s*5)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*4)), (x+(s*6)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*6),y+(s*7)), (x+(s*7)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*6)), (x+(s*5)-1,y+(s*7)-1), color, -1)
            x += s*8
        elif ord(letter) == 66:    # capital B
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y), (x+(s*4)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*4)), (x+(s*4)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*1)), (x+(s*5)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*5)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            x += s*6
        elif ord(letter) == 67:    # capital C
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y), (x+(s*5)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*1)), (x+(s*6)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*5)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*7)), (x+(s*6)-1,y+(s*8)-1), color, -1)
            x += s*7
        elif ord(letter) == 68:    # capital D
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y), (x+(s*4)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*1)), (x+(s*5)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*7)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*2)), (x+(s*6)-1,y+(s*7)-1), color, -1)
            x += s*7
        elif ord(letter) == 69:    # capital E
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y), (x+(s*5)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*4)), (x+(s*4)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*5)-1,y+(s*9)-1), color, -1)
            x += s*6
        elif ord(letter) == 70:    # capital F
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y), (x+(s*5)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*4)), (x+(s*4)-1,y+(s*5)-1), color, -1)
            x += s*6
        elif ord(letter) == 71:    # capital G
            cv2.rectangle(img, (x+(s*1),y), (x+(s*5)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*1)), (x+(s*6)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*7)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*4)), (x+(s*6)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*4)), (x+(s*5)-1,y+(s*5)-1), color, -1)
            x += s*7
        elif ord(letter) == 72:    # capital H
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y), (x+(s*6)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*4)), (x+(s*5)-1,y+(s*5)-1), color, -1)
            x += s*7
        elif ord(letter) == 73:    # capital I
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*9)-1), color, -1)
            x += s*2
        elif ord(letter) == 74:    # capital J
            cv2.rectangle(img, (x+(s*3),y), (x+(s*4)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*3)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*6)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            x += s*5
        elif ord(letter) == 75:    # capital K
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*2)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*2)), (x+(s*3)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*1)), (x+(s*4)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y), (x+(s*5)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*5)), (x+(s*3)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*6)), (x+(s*4)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*7)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*8)), (x+(s*6)-1,y+(s*9)-1), color, -1)
            x += s*7
        elif ord(letter) == 76:    # capital L
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*5)-1,y+(s*9)-1), color, -1)
            x += s*6
        elif ord(letter) == 77:    # capital M
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*2)), (x+(s*2)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*4)), (x+(s*3)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*6)), (x+(s*4)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*4)), (x+(s*5)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*2)), (x+(s*6)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*6),y), (x+(s*7)-1,y+(s*9)-1), color, -1)
            x += s*8
        elif ord(letter) == 78:    # capital N
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*1)), (x+(s*2)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*3)), (x+(s*3)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*5)), (x+(s*4)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*6)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y), (x+(s*6)-1,y+(s*9)-1), color, -1)
            x += s*7
        elif ord(letter) == 79:    # capital O
            cv2.rectangle(img, (x+(s*1),y), (x+(s*5)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*1)), (x+(s*6)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*5)-1,y+(s*9)-1), color, -1)
            x += s*7
        elif ord(letter) == 80:    # capital P
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y), (x+(s*5)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*4)), (x+(s*5)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*1)), (x+(s*6)-1,y+(s*4)-1), color, -1)
            x += s*7
        elif ord(letter) == 81:    # capital Q
            cv2.rectangle(img, (x+(s*1),y), (x+(s*5)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*1)), (x+(s*6)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*5)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*6)), (x+(s*4)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*7)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*9)), (x+(s*6)-1,y+(s*10)-1), color, -1)
            x += s*7
        elif ord(letter) == 82:    # capital R
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y), (x+(s*5)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*4)), (x+(s*5)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*1)), (x+(s*6)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*5)), (x+(s*6)-1,y+(s*9)-1), color, -1)
            x += s*7
        elif ord(letter) == 83:    # capital S
            cv2.rectangle(img, (x+(s*1),y), (x+(s*4)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*1)), (x+(s*5)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*4)), (x+(s*4)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*5)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*7)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            x += s*6
        elif ord(letter) == 84:    # capital T
            cv2.rectangle(img, (x,y), (x+(s*5)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*1)), (x+(s*3)-1,y+(s*9)-1), color, -1)
            x += s*6
        elif ord(letter) == 85:    # capital U
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y), (x+(s*6)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*5)-1,y+(s*9)-1), color, -1)
            x += s*7
        elif ord(letter) == 86:    # capital V
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*2)), (x+(s*2)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*5)), (x+(s*3)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*7)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*5)), (x+(s*5)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*2)), (x+(s*6)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*6),y), (x+(s*7)-1,y+(s*2)-1), color, -1)
            x += s*8
        elif ord(letter) == 87:    # capital W
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*2)), (x+(s*2)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*5)), (x+(s*3)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*7)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*5)), (x+(s*5)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*2)), (x+(s*6)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*6),y+(s*5)), (x+(s*7)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*7),y+(s*7)), (x+(s*8)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*8),y+(s*5)), (x+(s*9)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*9),y+(s*2)), (x+(s*10)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*10),y), (x+(s*11)-1,y+(s*2)-1), color, -1)
            x += s*12
        elif ord(letter) == 88:    # capital X
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*2)), (x+(s*2)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*3)), (x+(s*3)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*4)), (x+(s*4)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*3)), (x+(s*5)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*2)), (x+(s*6)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*6),y), (x+(s*7)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*5)), (x+(s*3)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*6)), (x+(s*2)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*7)), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*5)), (x+(s*5)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*6)), (x+(s*6)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*6),y+(s*7)), (x+(s*7)-1,y+(s*9)-1), color, -1)
            x += s*8
        elif ord(letter) == 89:    # capital Y
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*2)), (x+(s*2)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*3)), (x+(s*3)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*3)), (x+(s*5)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*2)), (x+(s*6)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*6),y), (x+(s*7)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*4)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            x += s*8
        elif ord(letter) == 90:    # capital Z
            cv2.rectangle(img, (x,y), (x+(s*7)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*6),y+(s*1)), (x+(s*7)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*2)), (x+(s*6)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*3)), (x+(s*5)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*4)), (x+(s*4)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*5)), (x+(s*3)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*6)), (x+(s*2)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*7)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*8)), (x+(s*7)-1,y+(s*9)-1), color, -1)
            x += s*8
        elif ord(letter) == 91:    # open square brackets
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*11)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y), (x+(s*2)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*10)), (x+(s*2)-1,y+(s*11)-1), color, -1)
            x += s*3
        elif ord(letter) == 92:    # backslash
            cv2.rectangle(img, (x,y), (x+(s*1),y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*2)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*5)), (x+(s*3)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*7)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            x += s*5
        elif ord(letter) == 93:    # close square brackets
            cv2.rectangle(img, (x+(s*1),y), (x+(s*2)-1,y+(s*11)-1), color, -1)
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*10)), (x+(s*1)-1,y+(s*11)-1), color, -1)
            x += s*3
        elif ord(letter) == 94:    # circumflex
            cv2.rectangle(img, (x,y+(s*2)), (x+(s*1)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*1)), (x+(s*2)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y), (x+(s*3)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*1)), (x+(s*4)-1,y+(s*2)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*2)), (x+(s*5)-1,y+(s*3)-1), color, -1)
            x += s*6
        elif ord(letter) == 95:    # underscore
            cv2.rectangle(img, (x,y+(s*10)), (x+(s*6)-1,y+(s*11)-1), color, -1)
            x += s*7
        elif ord(letter) == 96:    # backquote
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*1)), (x+(s*2)-1,y+(s*2)-1), color, -1)
            x += s*3
        elif ord(letter) == 97:    # small a
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*4)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*4)), (x+(s*5)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*6)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*5)), (x+(s*4)-1,y+(s*6)-1), color, -1)
            x += s*6
        elif ord(letter) == 98:    # small b
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*4)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*4)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            x += s*6
        elif ord(letter) == 99:    # small c
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*4)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*4)), (x+(s*5)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*4)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*7)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            x += s*6
        elif ord(letter) == 100:   # small d
            cv2.rectangle(img, (x+(s*4),y), (x+(s*5)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*4)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*4)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            x += s*6
        elif ord(letter) == 101:   # small e
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*4)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*5)), (x+(s*4)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*4)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*4)), (x+(s*5)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*7)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            x += s*6
        elif ord(letter) == 102:   # small f
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y), (x+(s*2)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*2)-1,y+(s*4)-1), color, -1)
            x += s*3
        elif ord(letter) == 103:   # small g
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*5)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*4)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*4)), (x+(s*5)-1,y+(s*10)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*10)), (x+(s*4)-1,y+(s*11)-1), color, -1)
            x += s*6
        elif ord(letter) == 104:   # small h
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*4)), (x+(s*2)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*3)), (x+(s*4)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*4)), (x+(s*5)-1,y+(s*9)-1), color, -1)
            x += s*6
        elif ord(letter) == 105:   # small i
            cv2.rectangle(img, (x,y+(s*3)), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*1)-1), color, -1)
            x += s*2
        elif ord(letter) == 106:   # small j
            cv2.rectangle(img, (x,y+(s*3)), (x+(s*1)-1,y+(s*11)-1), color, -1)
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*1)-1), color, -1)
            x += s*2
        elif ord(letter) == 107:   # small k
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*5)), (x+(s*2)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*4)), (x+(s*3)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*3)), (x+(s*4)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*6)), (x+(s*3)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*7)), (x+(s*4)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*8)), (x+(s*5)-1,y+(s*9)-1), color, -1)
            x += s*6
        elif ord(letter) == 108:   # small l
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*9)-1), color, -1)
            x += s*2
        elif ord(letter) == 109:   # small m
            cv2.rectangle(img, (x,y+(s*3)), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*3)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*4)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*3)), (x+(s*6)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*6),y+(s*4)), (x+(s*7)-1,y+(s*9)-1), color, -1)
            x += s*8
        elif ord(letter) == 110:   # small n
            cv2.rectangle(img, (x,y+(s*3)), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*4)), (x+(s*2)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*3)), (x+(s*4)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*4)), (x+(s*5)-1,y+(s*9)-1), color, -1)
            x += s*6
        elif ord(letter) == 111:   # small o
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*4)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*4)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*4)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            x += s*6
        elif ord(letter) == 112:   # small p
            cv2.rectangle(img, (x,y+(s*3)), (x+(s*1)-1,y+(s*11)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*4)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*4)), (x+(s*5)-1,y+(s*8)-1), color, -1)
            x += s*6
        elif ord(letter) == 113:   # small q
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*4)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*4)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*3)), (x+(s*5)-1,y+(s*11)-1), color, -1)
            x += s*6
        elif ord(letter) == 114:   # small r
            cv2.rectangle(img, (x,y+(s*3)), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*2)-1,y+(s*4)-1), color, -1)
            x += s*3
        elif ord(letter) == 115:   # small s
            cv2.rectangle(img, (x+(s*3),y+(s*4)), (x+(s*4)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*3)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*4)), (x+(s*1)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*5)), (x+(s*2)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*6)), (x+(s*3)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*7)), (x+(s*4)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*3)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*7)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            x += s*5
        elif ord(letter) == 116:   # small t
            cv2.rectangle(img, (x,y+(s*1)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*2)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*2)-1,y+(s*9)-1), color, -1)
            x += s*3
        elif ord(letter) == 117:   # small u
            cv2.rectangle(img, (x,y+(s*3)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*8)), (x+(s*3)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*7)), (x+(s*4)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*3)), (x+(s*5)-1,y+(s*9)-1), color, -1)
            x += s*6
        elif ord(letter) == 118:   # small v
            cv2.rectangle(img, (x,y+(s*3)), (x+(s*1)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*5)), (x+(s*2)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*7)), (x+(s*3)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*5)), (x+(s*4)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*3)), (x+(s*5)-1,y+(s*5)-1), color, -1)
            x += s*6
        elif ord(letter) == 119:   # small w
            cv2.rectangle(img, (x,y+(s*3)), (x+(s*1)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*7)), (x+(s*2)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*5)), (x+(s*3)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*3)), (x+(s*4)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*5)), (x+(s*5)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*7)), (x+(s*6)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*6),y+(s*3)), (x+(s*7)-1,y+(s*7)-1), color, -1)
            x += s*8
        elif ord(letter) == 120:   # small x
            cv2.rectangle(img, (x,y+(s*3)), (x+(s*1)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*7)), (x+(s*1)-1,y+(s*9)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*5)), (x+(s*3)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*3)), (x+(s*4)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*7)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            x += s*5
        elif ord(letter) == 121:   # small y
            cv2.rectangle(img, (x+(s*1),y+(s*3)), (x+(s*2)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*4),y+(s*3)), (x+(s*5)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*7)), (x+(s*4)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*8)), (x+(s*3)-1,y+(s*10)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*10)), (x+(s*2)-1,y+(s*11)-1), color, -1)
            x += s*6
        elif ord(letter) == 122:   # small z
            cv2.rectangle(img, (x,y+(s*3)), (x+(s*4)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*4)), (x+(s*4)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*5)), (x+(s*3)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*6)), (x+(s*2)-1,y+(s*7)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*7)), (x+(s*1)-1,y+(s*8)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*8)), (x+(s*4)-1,y+(s*9)-1), color, -1)
            x += s*5
        elif ord(letter) == 123:   # open curve brackets
            cv2.rectangle(img, (x+(s*2),y), (x+(s*3)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*1)), (x+(s*2)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*5)), (x+(s*1)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*6)), (x+(s*2)-1,y+(s*10)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*10)), (x+(s*3)-1,y+(s*11)-1), color, -1)
            x += s*4
        elif ord(letter) == 124:   # vertical pipe
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*10)-1), color, -1)
            x += s*2
        elif ord(letter) == 125:   # close curve brackets
            cv2.rectangle(img, (x,y), (x+(s*1)-1,y+(s*1)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*1)), (x+(s*2)-1,y+(s*5)-1), color, -1)
            cv2.rectangle(img, (x+(s*2),y+(s*5)), (x+(s*3)-1,y+(s*6)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*6)), (x+(s*2)-1,y+(s*10)-1), color, -1)
            cv2.rectangle(img, (x,y+(s*10)), (x+(s*1)-1,y+(s*11)-1), color, -1)
            x += s*4
        elif ord(letter) == 126:   # tilde
            cv2.rectangle(img, (x,y+(s*3)), (x+(s*1)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*1),y+(s*2)), (x+(s*3)-1,y+(s*3)-1), color, -1)
            cv2.rectangle(img, (x+(s*3),y+(s*3)), (x+(s*5)-1,y+(s*4)-1), color, -1)
            cv2.rectangle(img, (x+(s*5),y+(s*2)), (x+(s*6)-1,y+(s*3)-1), color, -1)
            x += s*7
    return img