# volume control bar for mac , test

import os
import cv2

def volume_control(level):
    volme_str = 'osascript -e "set Volume ' + str(level) + '"'
    os.system(volme_str)

def find_ROI(img_target, img_gui):
    img2, contours, hierachy = cv2.findContours(img_target, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt = contours[0]
    # cv2.drawContours(img_gui, contours, 0, (0,0,255), 2)
    return cnt
#
def show_pee(img,x,y):
    img2 = img.copy()
    cv2.line(img2,(x,y),(150,478), (0,241,255),3)
    cv2.imshow('volume_control_bar', img2)

def mouse_interactive(event, x, y, flags, param):
    global peeing, cx, cy, cnt, level, img_gui
    if event == cv2.EVENT_MOUSEMOVE:
        peeing = True
        retval = cv2.pointPolygonTest(cnt,(x,y),False)
        if retval <= 0 :
            level = 0
            show_pee(img_gui,x,y)
        else:
            level = 4
            show_pee(img_gui,x,y)
        volume_control(level)
        peeing = False
        print(level)

if __name__ == '__main__':
    peeing = False

    img_gui = cv2.imread('data/gui.jpg', cv2.IMREAD_COLOR)
    img_target = cv2.imread('data/gui_target.png', cv2.IMREAD_GRAYSCALE)

    cnt = find_ROI(img_target, img_gui)
    level = 1

    cv2.namedWindow('volume_control_bar')
    cv2.imshow('volume_control_bar', img_gui)
    cv2.setMouseCallback('volume_control_bar', mouse_interactive)

    # cv2.imshow('test', img_gui)
    cv2.waitKey()
    cv2.destroyAllWindows()

