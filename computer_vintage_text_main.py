""" COMPUTER VINTAGE TEXT (v1.0) """
""" WRITTEN BY DOGAN YIGIT YENIGUN (toUpperCase78) """
import numpy as np
import cv2
import sys, os
from text_chars_ms_windows import draw_text_chars_ms_windows
# USAGE: python computer_vintage_text_main.py 1 <width> <height> <bg_red> <bg_green> <bg_blue>
#        python computer_vintage_text_main.py 1 900 900 25 50 20
#        python computer_vintage_text_main.py 2 <image_file_name>
#        python computer_vintage_text_main.py 2 black_bg.jpg

if len(sys.argv) < 2:
    raise ValueError("Mode must be entered!")
mode = sys.argv[1]
if not mode.isdigit():
    raise TypeError("Mode must be an integer!")
mode = int(mode)
if mode != 1 and mode != 2:
    raise ValueError("Mode must be either 1 or 2!")

if mode == 1:     # MODE 1: Fully flat background with defined resolution and color
    fname = "image1.jpg"
    if len(sys.argv) < 4:
        raise ValueError("Resolution value must be entered!")
    height = sys.argv[3];   width = sys.argv[2]
    if not height.isdigit() or not width.isdigit():
        raise TypeError("Resolution value must be derived from integers!")
    height = int(height);    width = int(width)
    if height >= 200 and height <= 1080 and width >= 200 and width <= 1920:
        img = np.uint8(np.zeros((height,width,3)))
    else:
        raise ValueError("Resolution value must be at least 200x200 and at most 1920x1080!")
    if len(sys.argv) < 7:
        raise ValueError("Background color value must be entered!")
    bg_red = sys.argv[4];   bg_green = sys.argv[5];   bg_blue = sys.argv[6]
    if not bg_red.isdigit() or not bg_green.isdigit() or not bg_blue.isdigit():
        raise TypeError("Background color value must be derived from integers!")
    bg_red = int(bg_red);   bg_green = int(bg_green);   bg_blue = int(bg_blue)
    if bg_red >= 0 and bg_red <= 255 and bg_green >= 0 and bg_green <= 255 and bg_blue >= 0 and bg_blue <= 255:
        img[:,:,0] = bg_blue;   img[:,:,1] = bg_green;   img[:,:,2] = bg_red
    else:
        raise ValueError("Background color value must be between 0 and 255!")
elif mode == 2:   # MODE 2: Select an image as background; must exist in the 'Input' folder
    if len(sys.argv) < 3:
        raise ValueError("Image file name must be entered!")
    fname = sys.argv[2]
    input_files = os.listdir('Input')
    if not fname in input_files:
        raise ValueError("The specified file name was not found in the Input folder!")
    img = cv2.imread('Input/'+fname)

texts = []
with open('text_to_insert.txt') as text_to_insert:
    red = 0;   green = 0;   blue = 0;   x_pos = 0;   y_pos = 0;   size = 0;   bg = False
    for line in text_to_insert:
        if line.startswith('#'):
            continue
        elif line.startswith('>'):
            params = line[2:].split()
            red = int(params[0]);   green = int(params[1]);   blue = int(params[2])
            x_pos = int(params[3]);   y_pos = int(params[4]);   size = int(params[5]);   bg = bool(int(params[6]))
            # print(red, green, blue, x_pos, y_pos, size, bg)
        elif "----" in line:
            texts.append([text, red, green, blue, x_pos, y_pos, size, bg])
        else:
            text = line[:].replace('\\n','\n')

for t in texts:
    img = draw_text_chars_ms_windows(img, t[0], (t[3], t[2], t[1]), t[4], t[5], t[6], t[7])

# Standalone test with the one mandatory parameter
# img = draw_text_chars_ms_windows(img)

# Standalone test with all supported text characters and all parameters
# text = "ABCDEFGHIJKLMN\nOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n0123456789\n?!&%#/\\()[]{}|$@+-<=>*^~_.,:;'\"`"
# PARAMETERS: Target image, Text to draw, Text color (BGR), Top-left (x,y) position, Font size
# img = draw_text_chars_ms_windows(img, text, (0, 255, 160), 25, 25, 5, False)

# Standalone test with different text colors with backgrounds and all parameters
# text = "The quick brown fox jumps over the lazy dog."
# img = draw_text_chars_ms_windows(img, text, (255, 0, 0), 20, 365, 2, True)
# img = draw_text_chars_ms_windows(img, text, (0, 255, 0), 23, 400, 3, True)
# img = draw_text_chars_ms_windows(img, text, (0, 0, 255), 26, 450, 4, True)
# img = draw_text_chars_ms_windows(img, text, (0, 255, 255), 29, 515, 5, True)
# img = draw_text_chars_ms_windows(img, text, (255, 255, 0), 32, 595, 6, True)
# img = draw_text_chars_ms_windows(img, text, (255, 0, 255), 35, 690, 7, True)
# img = draw_text_chars_ms_windows(img, text, (255, 255, 255), 38, 800, 8, True)

while True:
    cv2.imshow("Computer Vintage Text - MS Windows", img)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:           # Press ESC to quit
        break
    elif k == ord('s'):   # Press S to save the image with the inserted text
        ext_ind = fname.find('.jpg')
        if ext_ind == -1:
            ext_ind = fname.find('.png')
        cv2.imwrite('Output/'+fname[:ext_ind]+'_out.jpg', img)
        print("Image was saved")
        break

cv2.destroyAllWindows()
