import cv2
import skimage
from skimage.transform import resize
from PIL import Image
import numpy as np
import pickle

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
path =[]
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,path

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y


    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                path.append((x,y))
                ix,iy = x,y
                cv2.line(img,(ix,iy),(x,y),(255), 13)
            else:
                cv2.line(img,(ix,iy),(x,y),(0),10)

            for coordinate in range(len(path)):
                if coordinate < len(path)-1:
                    cv2.line(img,path[coordinate],path[coordinate+1],(255), 13)
                else:
                    break

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if drawing == False:
            path = []
        """if mode == True:
            cv2.line(img,(ix,iy),(x,y),(0,0,255))
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)"""

        drawn_img = (img).astype(np.uint8)
        print drawn_img
        drawn_img = cv2.resize(img,(28,28),interpolation = cv2.INTER_AREA)
        cv2.imshow('image2',drawn_img)
        print drawn_img.shape
        print drawn_img
        drawn_img = (drawn_img).astype(np.uint8)
        cv2.imwrite('drawn_img.png',drawn_img)
        print "saved"
        """im = Image.open('drawn_img.png')"""

        """ im.thumbnail(28,28)"""


img = np.zeros((256,256), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('n'):
        import Trained_Network
        reload(Trained_Network)
        with open('biases.pkl','rb') as f:
            biases = pickle.load(f)
        with open('weights.pkl','rb') as f:
            weights = pickle.load(f)
        test1 = Trained_Network.Testing(biases,weights, "")
        test1.test()
        break

"""def main():
    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('m'):
            mode = not mode
        elif k == ord('n'):
            return drawn_img
            break
"""
"""while(1):
    cv2.imshow('image',img)
    p = cv2.waitKey(1) & 0xFF
    if p == ord('n'):
        img = np.zeros((28,28,3), np.uint8)
    elif p == 27:
        break"""

cv2.destroyAllWindows()
