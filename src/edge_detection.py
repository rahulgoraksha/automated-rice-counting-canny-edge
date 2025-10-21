import cv2

def canny_edge(gray, low_threshold=50, high_threshold=150):
    edges = cv2.Canny(gray, low_threshold, high_threshold)
    return edges
