import numpy as np
import argparse
import cv2
import sys,os

path = os.path.dirname(os.path.abspath(__file__))
print(path)



ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", 
    # required = True,
	help = "path to the image file") 

args = vars(ap.parse_args())

if args['image'] == None:
    raise Exception('You should put a image name')
else:

    img = cv2.imread(os.path.join(path,args["image"]),0)
    size = np.size(img)

    skel = np.zeros(img.shape,np.uint8)
    ret,img = cv2.threshold(img,127,255,0)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    done = False

    while( not done):
        eroded = cv2.erode(img,element)
        temp = cv2.dilate(eroded,element)
        temp = cv2.subtract(img,temp)
        skel = cv2.bitwise_or(skel,temp)
        img = eroded.copy()
 
        zeros = size - cv2.countNonZero(img)
        if zeros==size:
            done = True
 
    cv2.imshow("skel",skel)
    print(type(skel))
    cv2.waitKey(0)
    cv2.destroyAllWindows()