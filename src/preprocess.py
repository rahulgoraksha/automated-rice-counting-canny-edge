import cv2
import numpy as np

def gaussian_blur(image, ksize=(5,5), sigma=0):
    return cv2.GaussianBlur(image, ksize, sigma)

def threshold_image(gray, thresh=127, maxval=255):
    _, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return binary

def load_image(path):
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {path}")
    return image

def to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
