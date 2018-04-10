"""
Project Information:
    Author      : Rahul Ambati
    Co-Authors  : Pallab Maji
    Date        :
    Project     : PoesNet - Pose Estimation Network

Functional Information:
    Aim     : To visualize the points in the annotations files onto their respective frames
    Inputs  :
    Outputs :

"""

import cv2
import os
import json
import natsort
from mat4py import *

#Alter the path below to point to the .mat file you wish to read.
data = loadmat(r'C:\Users\rahulambati\Documents\ML\Posetrack_Dataset\annotations\annotations\val\000342_mpii_relpath_5sec_testsub.mat')

#Just so we can see what the the format is like
#You can uncomment if you'd like to save the json
# with open("readable.json", "w") as f:
#     json.dump(data, f, indent=4)

image_list = []
joint_list = None

# Create list of LABELLED IMAGES
for i, j in enumerate(data['annolist']["is_labeled"]):
    if j == 1:
        image_list.append((i, data["annolist"]["image"][i]["name"]))
#
# Take a look at how the paths are below.
# They'll start from "images/folder_name/folder_name/image_name"
# Dataset when extracted will have a subfolder called "images"
# ensure this script is in the same directory.
print(image_list)

#Iterates through image list and plots points
for image in image_list:
    index = image[0]
    frame = cv2.imread("posetrack_data" + "/" + image[1])
    for k in data["annolist"]["annorect"][index]["annopoints"]:
        for num in k['point']['id']:
            x = int(k['point']['x'][num])
            y = int(k['point']['y'][num])
            cv2.circle(frame, (x, y), 3, (255, 0, 0), 1)

    cv2.imshow("thing", frame)
    cv2.waitKey(1)
