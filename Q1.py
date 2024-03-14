# load the libraries
import cv2 as cv

# to reduce the intensity level
def intensityLevel(image, levels):
    # factor to scale down intensity levels
    factor = 256 // levels
    reduced_image = (image // factor) * factor
    return reduced_image


# Load the image with gray
img = cv.imread('Image/cat.jpg', cv.IMREAD_GRAYSCALE)

# if for check availability of the loaded image
if img is None:
    print("Error --> Unable to read the image.")
else:
    # reduced image set
    reduced_image_2 = intensityLevel(img, 2)
    reduced_image_4 = intensityLevel(img, 4)
    reduced_image_8 = intensityLevel(img, 8)
    reduced_image_16 = intensityLevel(img, 16)
    reduced_image_32 = intensityLevel(img, 32)
    reduced_image_64 = intensityLevel(img, 64)
    reduced_image_128 = intensityLevel(img, 126)
    reduced_image_256 = intensityLevel(img, 256)

    # Save the images
    cv.imwrite('Q1_outputs/intensiveLevel_2.jpg', reduced_image_2)
    cv.imwrite('Q1_outputs/intensiveLevel_4.jpg', reduced_image_4)
    cv.imwrite('Q1_outputs/intensiveLevel_8.jpg', reduced_image_8)
    cv.imwrite('Q1_outputs/intensiveLevel_16.jpg', reduced_image_16)
    cv.imwrite('Q1_outputs/intensiveLevel_32.jpg', reduced_image_32)
    cv.imwrite('Q1_outputs/intensiveLevel_64.jpg', reduced_image_64)
    cv.imwrite('Q1_outputs/intensiveLevel_128.jpg', reduced_image_128)
    cv.imwrite('Q1_outputs/intensiveLevel_256.jpg', reduced_image_256)

    # Display the images
    cv.imshow('intensiveLevel_2', reduced_image_2)
    cv.imshow('intensiveLevel_4', reduced_image_4)
    cv.imshow('intensiveLevel_8', reduced_image_8)
    cv.imshow('intensiveLevel_16', reduced_image_16)
    cv.imshow('intensiveLevel_32', reduced_image_32)
    cv.imshow('intensiveLevel_64', reduced_image_64)
    cv.imshow('intensiveLevel_128', reduced_image_128)
    cv.imshow('intensiveLevel_256', reduced_image_256)


    cv.waitKey(0)
    cv.destroyAllWindows()
