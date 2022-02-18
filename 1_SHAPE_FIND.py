#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 10:33:06 2021
@author: fabien
"""
import cv2,os
import numpy as np, pylab as plt

################################### PARAMETER
FILENAME = "Typischer-Kirchenplan.png"

################################### EDGE DETECTION
# img import
img_original = cv2.imread(os.getcwd() + os.path.sep + FILENAME)
#edges = cv2.Canny(img_original,100,200)

# extract thresh contours
imgray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
im2, contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# find max lenght index
lenght = np.array([img.shape[0] for img in im2])
idx_lenght = np.where(lenght==lenght.max())[0][0]

################################### SHAPE PLOT
curve = im2[idx_lenght][:,0].T
plt.imshow(img_original)
plt.plot(curve[0],curve[1], 'r',linewidth=2)
plt.savefig('PLAN_CURVE.svg')
plt.savefig('PLAN_CURVE.png', dpi=360)
