import cv2
import numpy as np
from PIL import Image
from glob import glob
from os import path as osp

img_ext = "*.png"

insp_path = r"V:\ADI\DATA\EHWA_ADI2_eraseT_201117-FN-down\test_roi\insp"
insp_label_path = r"V:\ADI\DATA\EHWA_ADI2_eraseT_201117-FN-down\test_roi\insp_label"
ref_path = r"V:\ADI\DATA\EHWA_ADI2_eraseT_201117-FN-down\test_refer"

single_image_path = r"D:\2020\DS\Project\2020-11-18-EHWA_Teinnetwork_Test\TwinnetTest\Data\Ehwa_erase_similar(TP2edge)\0_800_24300_041-2.png"


WIDTH = 200
HEIGHT = 200

INSP_FLAG = False
INSP_LABEL_FLAG = False
REF_FLAG = False

SINGLE_IMAGE_MODE = True


if INSP_FLAG:
    insp_img_list = glob(osp.join(insp_path, img_ext))
    for img in insp_img_list:
        np_img = np.float32(cv2.imread(img, cv2.IMREAD_GRAYSCALE))
        down_shift_img = np.roll(np_img, 50, axis=0)  # Down shift
        #down_shift_img = np.roll(np_img, 1, axis=1)  # Right shift
        cv2.imwrite(img, down_shift_img)

if INSP_LABEL_FLAG:
    insp_label_img_list = glob(osp.join(insp_label_path, img_ext))
    for lbl in insp_label_img_list:
        # region White Label
        # np_img = 255 * np.ones((HEIGHT, WIDTH))
        # cv2.imwrite(lbl, np_img)
        # endregion

        np_img = np.float32(cv2.imread(lbl, cv2.IMREAD_GRAYSCALE))
        down_shift_img = np.roll(np_img, 50, axis=0)  # Down shift
        # down_shift_img = np.roll(np_img, 1, axis=1)  # Right shift
        cv2.imwrite(lbl, down_shift_img)

if REF_FLAG:
    ref_img_list = glob(osp.join(ref_path, img_ext))
    for img in ref_img_list:
        np_img = np.float32(cv2.imread(img, cv2.IMREAD_GRAYSCALE))
        down_shift_img = np.roll(np_img, 50, axis=0)  # Down shift
        #down_shift_img = np.roll(np_img, 1, axis=1)  # Right shift
        cv2.imwrite(img, down_shift_img)

if SINGLE_IMAGE_MODE:
    np_img = np.float32(cv2.imread(single_image_path, cv2.IMREAD_GRAYSCALE))
    down_shift_img = np.roll(np_img, 1, axis=0)
    cv2.imwrite(single_image_path, down_shift_img)