
# import the necessary packages
import numpy as np
import argparse
# import imutils
import cv2
import sys,os

path =os.path.dirname(os.path.abspath(__file__))
print(path)
#

def draw_grid(img, line_color=(0, 255, 0), thickness=1, type_=cv2.LINE_AA, pxstep=20):
    '''(ndarray, 3-tuple, int, int) -> void
    draw gridlines on img
    line_color:
        BGR representation of colour
    thickness:
        line thickness
    type:
        8, 4 or cv2.LINE_AA
    pxstep:
        grid line frequency in pixels
    '''
    x = pxstep
    y = pxstep
    while x < img.shape[1]:
        cv2.line(img, (x, 0), (x, img.shape[0]), color=line_color, lineType=type_, thickness=thickness)
        x += pxstep

    while y < img.shape[0]:
        cv2.line(img, (0, y), (img.shape[1], y), color=line_color, lineType=type_, thickness=thickness)
        y += pxstep
    return img    
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
    size = np.size(image)
    skel = np.zeros(image.shape,np.uint8)
    blur = cv2.GaussianBlur(image,(5,5),0)
    # Smoothing to reduce noice
    # hist = cv2.calcHist([blur],[0],None,[256],[0,256])
    # #https://docs.opencv.org/2.4/modules/imgproc/doc/histograms.html?highlight=calchist
    # hist_norm = hist.ravel()/hist.max()
    ret, thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # image = thresh[200: 400 , 100 : 300]
    image = draw_grid(thresh)
    # print(type(image))
    element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    #So what happends is that, 
    #all the pixels near boundary will be discarded depending upon the size of kernel. 
    #So the thickness or size of the foreground object decreases or simply white region decreases in the image. 
    #It is useful for removing small white noises (as we have seen in colorspace chapter), 
    # detach two connected objects etc.
    done = False

    while( not done):
        eroded = cv2.erode(image,element)
        temp = cv2.dilate(eroded,element)
        temp = cv2.subtract(image,temp)
        skel = cv2.bitwise_or(skel,temp)
        img = eroded.copy()

        zeros = size - cv2.countNonZero(img)
        if zeros ==size:
            done = True

    cv2.imshow('image',skel)
    # cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)