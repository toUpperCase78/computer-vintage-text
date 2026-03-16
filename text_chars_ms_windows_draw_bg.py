""" CALCULATE BACKGROUND FOR TEXT CHARACTERS | MICROSOFT WINDOWS (v1.0) """
""" WRITTEN BY DOGAN YIGIT YENIGUN (toUpperCase78) """
import numpy as np
import cv2

def calculate_bg_text_chars_ms_windows(img, text, color, x, y, s):
    blue = color[0] // 2;   green = color[1] // 2;   red = color[2] // 2
    bg_color = (blue, green, red)
    x_init = x
    for letter in text:
        if ord(letter) == 10:      # new line
            x = x_init;   y += s*13
        elif ord(letter) == 32:    # space
            x += s*3
        # 1 PIXEL: punctuation ! ' . :, capital I, small i j l, punctuation |
        elif ord(letter) in [33, 46, 58, 73, 105, 106, 108, 124]:
            cv2.rectangle(img, (x-(s*3), y-(s*3)), (x+(s*4)-1,y+(s*12)-1), bg_color, -1)
            x += s*2
        # 2 PIXELS: punctuation ' ( ) , - ; [ ] `, small f r t
        elif ord(letter) in [39, 40, 41, 44, 45, 59, 91, 93, 96, 102, 114, 116]:
            cv2.rectangle(img, (x-(s*3), y-(s*3)), (x+(s*5)-1,y+(s*12)-1), bg_color, -1)
            x += s*3
        # 3 PIXELS: punctuation " *, number 1, punctuation { }
        elif ord(letter) in [34, 42, 49, 123, 125]:
            cv2.rectangle(img, (x-(s*3), y-(s*3)), (x+(s*6)-1,y+(s*12)-1), bg_color, -1)
            x += s*4
        # 4 PIXELS: punctuation / < >, capital J, punctuation \, small s x z
        elif ord(letter) in [47, 60, 62, 74, 92, 115, 120, 122]:
            cv2.rectangle(img, (x-(s*3), y-(s*3)), (x+(s*7)-1,y+(s*12)-1), bg_color, -1)
            x += s*5
        # 5 PIXELS: punctuation $ & +, number 0 2 3 4 5 6 7 8 9, punctuation = ?, capital B E F L S T, punctuation ^, small a b c d e g h l n o p q u v y
        elif ord(letter) in [36, 38, 43, 48, 50, 51, 52, 53, 54, 55, 56, 57, 61, 63, 66, 69, 70, 76, 83, 84, 94, 97, 98, 99, 100, 101, 103, 104, 107, 110, 111, 112, 113, 117, 118, 121]:
            cv2.rectangle(img, (x-(s*3), y-(s*3)), (x+(s*8)-1,y+(s*12)-1), bg_color, -1)
            x += s*6
        # 6 PIXELS: punctuation #, capital C D G H K N O P Q R U, punctuation _ ~
        elif ord(letter) in [35, 67, 68, 71, 72, 75, 78, 79, 80, 81, 82, 85, 95, 126]:
            cv2.rectangle(img, (x-(s*3), y-(s*3)), (x+(s*9)-1,y+(s*12)-1), bg_color, -1)
            x += s*7
        # 7 PIXELS: punctuation %, capital A M V X Y Z, small m w
        elif ord(letter) in [37, 65, 77, 86, 88, 89, 90, 109, 119]:
            cv2.rectangle(img, (x-(s*3), y-(s*3)), (x+(s*10)-1,y+(s*12)-1), bg_color, -1)
            x += s*8
        # 10 PIXELS: punctuation @
        elif ord(letter) in [64]:
            cv2.rectangle(img, (x-(s*3), y-(s*3)), (x+(s*13)-1,y+(s*12)-1), bg_color, -1)
            x += s*11
        # 11 PIXELS: capital W
        elif ord(letter) in [87]:
            cv2.rectangle(img, (x-(s*3), y-(s*3)), (x+(s*14)-1,y+(s*12)-1), bg_color, -1)
            x += s*12
    return img