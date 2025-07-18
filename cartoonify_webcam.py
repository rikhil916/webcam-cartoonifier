import cv2 
import numpy as np
import matplotlib.pyplot as plt

def edge_mask(img,line_size=7,blur_value=7):
    """
    input:Image
    Output:Edge Mask Image
    """
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#change made here
    gray_blur=cv2.medianBlur(gray,blur_value)

    edges=cv2.adaptiveThreshold(gray_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,line_size,blur_value)
    return edges

def color_quantization(img,k=5):

    #transforming the image
    data=np.float32(img).reshape((-1,3))

    #Determine Criteria 
    criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,20,0.001)

    #implementing K-Means

    _,label,center=cv2.kmeans(data,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    center=np.uint8(center)

    result=center[label.flatten()]

    result=result.reshape(img.shape)

    return result

def cartoonify_frame(frame):

    frame=cv2.resize(frame,(480,360),interpolation=cv2.INTER_NEAREST)

    edges=edge_mask(frame)
    quantized=color_quantization(frame)
    blurred=cv2.bilateralFilter(quantized,d=2,sigmaColor=150,sigmaSpace=150)
    cartoon=cv2.bitwise_and(blurred,blurred,mask=edges)
    return cartoon
    #plt.imshow(c)
    #plt.title("Cartoon Image")
    #plt.show()


    #plt.imshow(org_img)
    #plt.title("Original Image")
    #plt.show()

def run_cartoon_webcam():
    cap=cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Failed to Open Camera")
        return 
    print("Press 'q' to quit")

    while True:
        ret,frame=cap.read()
        if not ret:
            print("Failed to grab frame")
            break 
        
        frame = cv2.flip(frame, 1)
        frame=cv2.resize(frame,(480,360),interpolation=cv2.INTER_NEAREST)
        cartoon=cartoonify_frame(frame)

        combined = np.hstack((frame, cartoon))  # Show original and cartoon side by side
        cv2.imshow("Original | Cartoonified", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 

    cap.release()
    cv2.destroyAllWindows()
    
run_cartoon_webcam()