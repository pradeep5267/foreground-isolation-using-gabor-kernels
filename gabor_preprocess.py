import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys

import matplotlib.pyplot as plt, argparse, numpy as np, math, sys, copy

try:
    img_fn = sys.argv[1]
except:
    img_fn = './table.jpg'

img = cv2.imread(img_fn)
if img is None:
    print ('Failed to load image file:', img_fn)
    sys.exit(1)

def build_filters():
    count = 0
    filters = []
    ksize = 13
    for theta in np.arange(0, np.pi, np.pi / 16):
        count =count+1
        kern = cv2.getGaborKernel((ksize, ksize), 4.0, 1.37446, 10.0, 0.5, 0, ktype=cv2.CV_32F)
        kern /= 1.5*kern.sum()
        filters.append(kern)
    return filters

def process(img, filters):
    accum = np.zeros_like(img)
    count = 0
    for kern in filters:
        count+=1
        fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
        np.maximum(accum, fimg, accum)
        filter_no = str(count)
        if count==8:
            return accum

def preprocessImage(img):

    #blur using kernel size 13x13
    blur = cv2.GaussianBlur(img, (13, 13), 2)
    kernel = np.ones((7, 7), np.uint8)
    img_erosion = cv2.erode(blur, kernel, iterations=1)
    
    mask_maker = img_erosion

    edges = cv2.Canny(mask_maker, 50, 70)
    kernel = np.ones((5, 5), np.uint8)
    img_edges = cv2.dilate(edges, kernel, iterations=1)
    
    #Draw contours
    ####################################
    imgArea = img.shape[0]*img.shape[1]
    contours, hierarchy = cv2.findContours(img_edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c)<imgArea/850: #changed to 850, a better approach would be to dynamically assign the values based on image size
            mask_x,mask_y,mask_w,mask_h = cv2.boundingRect(c)
            cv2.rectangle(img_edges,(mask_x,mask_y),(mask_x+mask_w,mask_y+mask_h),(0,0,0),-1)
    ####################################
    return img_edges


#gabor filtering
####################################################################
filters = build_filters()
res1 = process(img, filters)
res1= cv2.GaussianBlur(res1,(13,13),2)
####################################################################

#'Tactical Preprocessing'
####################################################################
res2 = preprocessImage(res1)
####################################################################
# cv2.imsave
cv2.imshow('result', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()