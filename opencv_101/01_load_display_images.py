# python .\01_load_display_images.py --image .\images\hey.png --output ./images/new_image.jpg

import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path of the input image")
ap.add_argument("-o", "--output", required=False, help="path of the output image")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
h, w, c = image.shape[:3]

print("height: {} pixels".format(h))
print("width: {} pixels".format(w))
print("channels: {}".format(c))

cv.imshow("Window", image)
cv.waitKey(0)

if args["output"]:
    cv.imwrite(args["output"], image)
