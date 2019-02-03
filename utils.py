import numpy.random as nprnd
import numpy as np
import cv2
import scipy.io as sio
import matplotlib.pyplot as plt

def resize(img, new_size, h, w):
    """
    Changes the largest side of an image to the new size and changes the other to maintain the aspect ratio.

    Args:
        img (BGR Matrix): The image that is going to be resized.
        new_size (integer): The value wanted for the biggest side of the image.

    Returns:
        BGR Matrix: The image resized to the new value keeping the aspect ratio.
    """
    if h > w:
        new_h = 640
        new_w = round((640 * w) / h)
    else:
        new_h = round((640 * h) / w)
        new_w = 640
    img = cv2.resize(img, (new_w, new_h))
    return img
