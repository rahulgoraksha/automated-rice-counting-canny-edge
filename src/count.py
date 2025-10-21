import os
import cv2
from preprocess import load_image, to_gray, gaussian_blur, threshold_image
from edge_detection import canny_edge
from contour_analysis import find_contours, count_grains

def process_image(input_path, output_path=None):
    image = load_image(input_path)
    gray = to_gray(image)
    blurred = gaussian_blur(gray)
    binary = threshold_image(blurred)
    edges = canny_edge(binary)
    contours = find_contours(edges)
    grain_count = count_grains(contours)

    print(f"Detected {grain_count} grains in {input_path}")

    # Optionally save output visualization
    if output_path:
        vis = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        cv2.drawContours(vis, contours, -1, (0,255,0), 1)
        cv2.imwrite(output_path, vis)
        print(f"Saved output to {output_path}")

    return grain_count

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Automated rice grain counting")
    parser.add_argument("--input", required=True, help="Path to input image")
    parser.add_argument("--output", help="Path to save output image")
    args = parser.parse_args()

    process_image(args.input, args.output)

