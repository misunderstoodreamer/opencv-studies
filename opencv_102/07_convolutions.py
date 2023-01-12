# python 07_convolutions.py
# cross correlation

from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2 as cv


def convolve(image, kernel):
    """
    :param image: whole image's matrix
    :param kernel: small matrix that make processing
    :return: convolved image
    """
    # spatial dimensions extraction
    iH, iW = image.shape[:2]
    kH, kW = kernel.shape[:2]

    # the problem of kernel's pixels that are not in the main image pixel
    # in this method replicate padding (mirror padding) applied

    # padding is equal to width of the kernel minus 1 divided by 2
    pad = (kW - 1) // 2

    image = cv.copyMakeBorder(src=image, top=pad, bottom=pad, left=pad, right=pad, borderType=cv.BORDER_REPLICATE)
    output = np.zeros(shape=(iH, iW), dtype="float32")

    # looping kernel across the image and sliding all (x, y)-coordinate
    # sliding window operation

    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            # extract region of interest (ROI) which is overlap of kernel and image of the image by extracting the
            # center region of the current (x, y)-coordinates dimensions
            roi = image[y - pad: y + pad + 1, x - pad:x + pad + 1]

            # doing convolution with element wise multiplication between ROI and the kernel, then summing the matrix
            k = (roi * kernel).sum()

            # finally save (store) the convolved value in the output (x, y)-coordinate of the output image
            output[y - pad, x - pad] = k

    # rescaling the output image to be in the range of 8 bit
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")

    return output


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/3d_pokemon.png",
                help="path to the input image")
args = vars(ap.parse_args())

# adding average blurring in order to smoothing the image

small_blur = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))
large_blur = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))

# sharpen filter
sharpen = np.array((
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0],), dtype="int")

# laplacian filter
laplacian = np.array((
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0],), dtype="int")

# sobel x-axis filter
sobel_x = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1],), dtype="int")

# sobel y-axis filter
sobel_y = np.array((
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1],), dtype="int")

kernel_bank = (
    ("small_blur", small_blur),
    ("large_blur", large_blur),
    ("sharpen", sharpen),
    ("laplacian", laplacian),
    ("sobel_x", sobel_x),
    ("sobel_y", sobel_y),
)


# loading input image and make it gray scaled
image = cv.imread(args["image"])
gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)

for (kernel_name, kernel) in kernel_bank:
    print(f"Applied kernel: {kernel_name}")
    convolved_output = convolve(gray, kernel)
    opencv_output = cv.filter2D(src=gray, ddepth=-1, kernel=kernel)

    # display
    cv.imshow("original", gray)
    cv.imshow(f"{kernel_name} - convolve", convolved_output)
    cv.imshow(f"{kernel_name} - opencv", opencv_output)
    cv.waitKey(0)
    cv.destroyAllWindows()

