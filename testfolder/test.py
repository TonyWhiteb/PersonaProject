
# import the necessary packages
import numpy as np
import argparse
# import imutils
import cv2
import sys,os

path =os.path.dirname(os.path.abspath(__file__))
print(path)

 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", 
    # required = True,
	help = "path to the image file") 
    # import help text and add argument when we excute our py file    
args = vars(ap.parse_args()) # setup a dictionary
# print(ap.parse_args().image)

# load the image and convert it to grayscale
if args['image'] == None:
    raise Exception('You should put a image name')
else:
    image = cv2.imread(os.path.join(path,args["image"]),0)
    blur = cv2.GaussianBlur(image,(5,5),0)
    # Smoothing to reduce noice
    # hist = cv2.calcHist([blur],[0],None,[256],[0,256])
    # #https://docs.opencv.org/2.4/modules/imgproc/doc/histograms.html?highlight=calchist
    # hist_norm = hist.ravel()/hist.max()
    ret, thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('image',thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)