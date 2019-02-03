# coding: utf-8

import os
import os.path
import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import shutil
import sys
#custom
import utils

arg = sys.argv
print(arg)

if arg[1] == 'training':
  #training
  pos_img_dir = './original_trainingdata/OK/'
  pos_img_files = os.listdir(pos_img_dir)
  neg_img_dir = './original_trainingdata/NG/'
  neg_img_files = os.listdir(neg_img_dir)
elif arg[1] == 'test':
  #test
  pos_img_dir = './original_trainingdata/OK_test/'
  pos_img_files = os.listdir(pos_img_dir)
  neg_img_dir = './original_trainingdata/NG_test/'
  neg_img_files = os.listdir(neg_img_dir)
else:
  print('arg should be training or test')
  sys.exit()

X = []
y = []
resize_to = 640
#des = None

print ('start loading ' + str(len(pos_img_files)-1) + ' positive files')
for pos_img_file in pos_img_files:
  pos_filepath = pos_img_dir + pos_img_file
  # not include hidden files
  root, ext = os.path.splitext(pos_filepath)
  if ext == ".JPG" :
    print(pos_filepath)
    pos_img = cv2.imread(pos_filepath)
    h, w, channels = pos_img.shape
    if h > resize_to or w > resize_to:
        pos_img = utils.resize(pos_img, resize_to, h, w)
    gray_pos= cv2.cvtColor(pos_img,cv2.COLOR_BGR2GRAY)

    #orb
    orb = cv2.ORB_create()
    kp_orb, des = orb.detectAndCompute(gray_pos, None)
    img_orb = cv2.drawKeypoints(gray_pos, kp_orb, None)

    #akaze
    #akaze = cv2.AKAZE_create()
    #kp_akaze, des = akaze.detectAndCompute(gray_pos, None)
    #img_akaze = cv2.drawKeypoints(gray_pos, kp_akaze, None)

    #fast
    #detect keypoints
    #fast = cv2.FastFeatureDetector_create()
    #kp_fast = fast.detect(pos_img, None)
    #img_fast = cv2.drawKeypoints(gray_pos, kp_fast, None)

    #brisk
    #brisk = cv2.BRISK_create()
    #kp_brisk = brisk.detect(gray_pos, None)
    #kp_brisk, des = brisk.compute(gray_pos, kp_brisk)
    #img_brisk = cv2.drawKeypoints(gray_pos, kp_brisk, None)

    #X = np.array(des, dtype=np.float32)
    #X.append(des)
    #y.append(1)

    #show image
    #plt.imshow(img_fast),plt.show()

    #modify output directory
    ex_dir = root + "_OK" + ext
    #cv2.imwrite(ex_dir, img_fast)
    cv2.imwrite(ex_dir, img_orb)
    #cv2.imwrite(ex_dir, img_akaze)
    #cv2.imwrite(ex_dir, img_brisk)

print ('start loading ' + str(len(neg_img_files)-1) + ' negative files')
for neg_img_file in neg_img_files:
  neg_filepath = neg_img_dir + neg_img_file
  # not include hidden files
  root, ext = os.path.splitext(neg_filepath)
  if ext == ".JPG" :
    print(neg_filepath)
    neg_img = cv2.imread(neg_filepath)
    h, w, channels = neg_img.shape
    if h > resize_to or w > resize_to:
        neg_img = utils.resize(neg_img, resize_to, h, w)
    gray_neg= cv2.cvtColor(neg_img,cv2.COLOR_BGR2GRAY)

    #fast
    #fast = cv2.FastFeatureDetector_create()
    #kp_fast = fast.detect(neg_img, None)
    #kp_fast, des = fast.compute(pos_img, kp_fast)
    #img_fast = cv2.drawKeypoints(gray_neg, kp_fast, None)
    #plt.imshow(img_fast),plt.show()

    #orb
    kp_orb, des = orb.detectAndCompute(gray_neg, None)
    img_orb = cv2.drawKeypoints(gray_neg, kp_orb, None)

    #akaze
    #kp_akaze, des = akaze.detectAndCompute(gray_neg, None)
    #img_akaze = cv2.drawKeypoints(gray_neg, kp_akaze, None)

    #brisk
    #brisk = cv2.BRISK_create()
    #kp_brisk = brisk.detect(gray_neg, None)
    #kp_brisk, neg_des = brisk.compute(gray_neg, kp_brisk)
    #img_brisk = cv2.drawKeypoints(gray_neg, kp_brisk, None)

    #X = np.vstack((X, np.array(neg_des)))
    #X.append(neg_des)
    #y.append(0)

    #modify output directory
    ex_dir = root + "_NG" + ext
    #cv2.imwrite(ex_dir, img_brisk)
    #cv2.imwrite(ex_dir, img_fast)
    cv2.imwrite(ex_dir, img_orb)
    #cv2.imwrite(ex_dir, img_akaze)
