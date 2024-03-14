# load the libraries
import cv2 as cv
import numpy as np

# To perform simple spatial average
def spatialAverage(image,size):
    kernel = np.ones((size, size), dtype=np.float32) / (size * size)
    averaged_image = cv.filter2D(image, -1, kernel)
    return averaged_image


# Load the image with gray
img = cv.imread('Image/bicycle.jpeg', cv.IMREAD_GRAYSCALE)

if img is None:
    print("Error --> Unable to read the image.")
else:

    # Spatial the image
    spatial_3x3 = spatialAverage(img, 3)
    spatial_10x10 = spatialAverage(img, 10)
    spatial_20x20 = spatialAverage(img, 20)

    # Show the spatial images
    cv.imshow("Original image", img)
    cv.imshow('Spatial 3x3', spatial_3x3)
    cv.imshow('Spatial 10x10', spatial_10x10)
    cv.imshow('Spatial 20x20', spatial_20x20)

    # save the output
    cv.imwrite('Q2_outputs/spatial_3x3.jpg', spatial_3x3)
    cv.imwrite('Q2_outputs/spatial_10x10.jpg', spatial_10x10)
    cv.imwrite('Q2_outputs/spatial_20x20.jpg', spatial_20x20)

    cv.waitKey(0)
    cv.destroyAllWindows()