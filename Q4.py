# load the libraries
import cv2 as cv
import numpy as np

# Function to perform block averaging
def blockAverage(image, block_size):
    height, width = image.shape[:2]

    # Calculate the number of blocks in image
    blockHeight = height // block_size
    blockWidth = width // block_size

    blocks = image[:blockHeight * block_size, :blockWidth * block_size].reshape(
        blockHeight, block_size, blockWidth, block_size, -1
    )

    block_avg = np.mean(blocks, axis=(1, 3)).astype(np.uint8)

    # Repeat block average
    averagedImage = np.repeat(np.repeat(block_avg, block_size, axis=0), block_size, axis=1)

    return averagedImage


# Load the image
img = cv.imread('Image/bicycle.jpeg', cv.IMREAD_GRAYSCALE)

if img is None:
    print("Error --> Unable to read the image.")
else:

    # block average
    block_3x3 = blockAverage(img, 3)
    block_5x5 = blockAverage(img, 5)
    block_7x7 = blockAverage(img, 7)

    # Show the images
    cv.imshow("Original image", img)
    cv.imshow('block_3x3', block_3x3)
    cv.imshow('block_5x5', block_5x5)
    cv.imshow('block_7x7', block_7x7)



    # save the output
    cv.imwrite('Q4_outputs/block_3x3.jpg', block_3x3)
    cv.imwrite('Q4_outputs/block_5x5.jpg', block_5x5)
    cv.imwrite('Q4_outputs/block_7x7.jpg', block_7x7)


    cv.waitKey(0)
    cv.destroyAllWindows()