# python 05_rotate.py

import argparse
import cv2 as cv
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/bojack.png",
                help="path to the input image")
args = vars(ap.parse_args())

image = cv.imread(args['image'])
cv.imshow("Original", image)
cv.waitKey(0)

# grab the dimensions of the image and calculate the center of the image

h, w = image.shape[:2]

cX, cY = w // 2, h // 2

M = cv.getRotationMatrix2D(center=(cX, cY), angle=45, scale=1)
# warpAffine = Affine Transformation
rotated = cv.warpAffine(src=image, M=M, dsize=(w, h))
cv.imshow("Rotated by 45 degree", rotated)
cv.waitKey(0)

M = cv.getRotationMatrix2D(center=(cX, cY), angle=-90, scale=1)
# warpAffine = Affine Transformation
rotated = cv.warpAffine(src=image, M=M, dsize=(w, h))
cv.imshow("Rotated by -90 degree", rotated)
cv.waitKey(0)

# rotate from arbitrary point
M = cv.getRotationMatrix2D(center=(30, 50), angle=20, scale=1)
rotated = cv.warpAffine(src=image, M=M, dsize=(w, h))
cv.imshow("Rotated by 20 degree with arbitrary point", rotated)
cv.waitKey(0)

# make it clear, imutils lib could be used
rotated = imutils.rotate(image=image, angle=-25, center=(100, 100), scale=1.0)
cv.imshow("Rotated by 25 degree with arbitrary point + imultils lib", rotated)
cv.waitKey(0)

# when you rotate, information may lost (cropped). to prevent this use rotate_bound
# https://pyimagesearch.com/2017/01/02/rotate-images-correctly-with-opencv-and-python/
rotated = imutils.rotate_bound(image=image, angle=45)
cv.imshow("Rotated by 45 degree without crop", rotated)
cv.waitKey(0)

