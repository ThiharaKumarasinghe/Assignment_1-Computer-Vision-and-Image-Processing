# load the libraries
import cv2 as cv
import numpy as np

# To rotate image with given angle
def rotateImage(image, angle):
    # define the center
    center = tuple(np.array(image.shape[1::-1]) / 2)

    # get rotate
    rotation_matrix = cv.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv.warpAffine(image, rotation_matrix, image.shape[1::-1], flags=cv.INTER_LINEAR)
    return rotated_image


# Load the image
img = cv.imread('Image/women.jpeg')

if img is None:
    print("Error --> Unable to read the image.")
else:

    # Rotate the image
    rotat45 = rotateImage(img, 45)
    rotat90 = rotateImage(img, 90)

    # Show the spatial images
    cv.imshow("Original image", img)
    cv.imshow('rotated 45', rotat45)
    cv.imshow('rotated 90', rotat90)


    # save the output
    cv.imwrite('Q3_outputs/rotated45.jpg', rotat45)
    cv.imwrite('Q3_outputs/rotated90.jpg', rotat90)

    cv.waitKey(0)
    cv.destroyAllWindows()