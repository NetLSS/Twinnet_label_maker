import cv2
import numpy as np
from PIL import Image
from glob import glob
from os import path as osp

img_ext = "*.png"

insp_path = r"V:\ADI\DATA\EHWA_ADI2_Exp_erase_similar(shiftD20)\test_roi\insp"
insp_label_path = r"V:\ADI\DATA\EHWA_ADI2_Exp_erase_similar(shiftD20)\test_roi\insp_label"

WIDTH = 200
HEIGHT = 200

insp_img_list = glob(osp.join(insp_path, img_ext))
insp_label_img_list = glob(osp.join(insp_label_path, img_ext))

for img in insp_img_list:
    np_img = np.float32(cv2.imread(img, cv2.IMREAD_GRAYSCALE))
    down_shift_img = np.roll(np_img, 10, axis=0)  # Down shift
    #down_shift_img = np.roll(np_img, 1, axis=1)  # Right shift
    cv2.imwrite(img, down_shift_img)

for lbl in insp_label_img_list:
    np_img = 255 * np.ones((HEIGHT, WIDTH))
    cv2.imwrite(lbl, np_img)

