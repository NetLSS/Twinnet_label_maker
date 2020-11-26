import cv2
import numpy as np
from glob import glob
from os import path as osp
import os

"""
twinnet test
이대 측 에서 train 시킨 모델사용하기 위한 형식
"""

HEIGHT = 200
WIDTH  = 200
IMAGE_TYPE = "png"
IS_DUBUG = True

insp_ref_inverse = False

refer_image_path = r"V:\ADI\DATA\EHWA_ADI2_Exp_ArtificialD\refer"
insp_image_path = r"V:\ADI\DATA\EHWA_ADI2_Exp_ArtificialD\test_roi\insp"
# refer_label_path = r"D:\2020\DS\Project\2020-11-18-EHWA_Teinnetwork_Test\TwinnetTest\Data"
insp_label_path = r"V:\ADI\DATA\EHWA_ADI2_Exp_ArtificialD\test_roi\insp_label"
save_full_path = r"D:\2020\DS\Project\2020-11-18-EHWA_Teinnetwork_Test\TwinnetTest\Data\EHWA_ADI2_Exp_ArtificialD(inspRefInverse)"

if not osp.exists(save_full_path):
    os.makedirs(save_full_path)

refer_image_files = glob(osp.join(refer_image_path, f"*.{IMAGE_TYPE}"))
insp_image_files = glob(osp.join(insp_image_path, f"*.{IMAGE_TYPE}"))
# refer_label_files = # zero image
insp_label_files = glob(osp.join(insp_label_path, f"*.{IMAGE_TYPE}"))

if IS_DUBUG:
    print(refer_image_files)

for ref_img in refer_image_files:
    ref_label_number = int(osp.splitext(osp.basename(ref_img))[0])
    if IS_DUBUG:
        print(ref_label_number)

for insp_img_file in insp_image_files:
    test_img = np.zeros((HEIGHT, WIDTH * 4))

    ref_label_number = int(osp.splitext(osp.basename(insp_img_file))[0].split("_")[-1])

    if IS_DUBUG:
        print(ref_label_number)

    ref_img_file = None

    for ref_img_f in refer_image_files:
        current_number = int(osp.splitext(osp.basename(ref_img_f))[0])
        if ref_label_number == current_number:
            ref_img_file = ref_img_f
            break

    assert ref_img_file is not None

    if not osp.exists(osp.join(insp_label_path, osp.basename(insp_img_file))):
        assert False

    insp_label_file = osp.join(insp_label_path, osp.basename(insp_img_file))

    """
    insp_img_file
    ref_img_file
    insp_label_file
    """

    insp_img = np.float32(cv2.imread(insp_img_file, cv2.IMREAD_GRAYSCALE))
    ref_img = np.float32(cv2.imread(ref_img_file, cv2.IMREAD_GRAYSCALE))
    insp_label_img = np.float32(cv2.imread(insp_label_file, cv2.IMREAD_GRAYSCALE))


    if insp_ref_inverse:
        test_img[:, 0 * WIDTH: 1 * WIDTH] = insp_img
        test_img[:, 1 * WIDTH: 2 * WIDTH] = ref_img
        test_img[:, 2 * WIDTH: 3 * WIDTH] = insp_label_img  # Refer Label
        # test_img[:, 3 * WIDTH: 4 * WIDTH] =  # insp_label
    else:
        test_img[:, 0 * WIDTH: 1 * WIDTH] = ref_img
        test_img[:, 1 * WIDTH: 2 * WIDTH] = insp_img
        # test_img[:, 2 * WIDTH: 3 * WIDTH] = # Refer Label
        test_img[:, 3 * WIDTH: 4 * WIDTH] = insp_label_img

    cv2.imwrite(osp.join(save_full_path, osp.basename(insp_img_file)), test_img)
