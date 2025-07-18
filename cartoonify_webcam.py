import cv2
import numpy as np

def edge_mask(img, line_size=7, blur_value=7):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, blur_value)
    edges = cv2.adaptiveThreshold(
        gray_blur, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        line_size, blur_value
    )
    return edges

def color_quantization(img, k=5):
    data = np.float32(img).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
    _, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(img.shape)
    return result

def cartoonify_frame(frame, line_size=7, blur_value=7, k=5):
    edges = edge_mask(frame, line_size, blur_value)
    quantized = color_quantization(frame, k)
    blurred = cv2.bilateralFilter(quantized, d=2, sigmaColor=150, sigmaSpace=150)
    cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
    return cartoon
