# load the libraries

import cv2 as cv
import numpy as np



# Load the image

original_img = cv.imread('Image/cat.jpg')
image = cv.resize(original_img, (800, 600))

if image is None:
    print("Error: Unable to read the image.")
else:
    # Display the image
    cv.imshow('Image', image)
    # Wait for any key press and then close the window
    cv.waitKey(0)
    cv.destroyAllWindows()
