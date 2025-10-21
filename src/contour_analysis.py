import cv2

def find_contours(edges):
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def count_grains(contours, min_area=50):
    """Count as grain any contour with area > min_area."""
    count = sum(1 for cnt in contours if cv2.contourArea(cnt) > min_area)
    return count

