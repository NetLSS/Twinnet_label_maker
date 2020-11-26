from os import path as osp
import os
import glob
import shutil
import numpy as np
import cv2


"""
   : np.r_[[a], [b]]
   : np.vstack([a, b])
   : np.concatenate((c, d), axis = 1) # for 2D ~ array
"""

result_root_path1 = r"D:\2020\DS\Project\2020-11-18-EHWA_Teinnetwork_Test\TwinnetTest\Result\EHWA_ADI2_Exp_ArtificialD\th0"
result_root_path2 = r"D:\2020\DS\Project\2020-11-18-EHWA_Teinnetwork_Test\TwinnetTest\Result\EHWA_ADI2_Exp_ArtificialD(inspRefInverse)\th0"
save_path = r"D:\2020\DS\Project\2020-11-18-EHWA_Teinnetwork_Test\TwinnetTest\Result_custom\EHWA_ADI2_Exp_ArtificialD(inspRefInverse)-1"

if not osp.exists(save_path):
    os.makedirs(save_path)

result_list1 = glob.glob(osp.join(result_root_path1, "*", "*.png"))
result_list2 = glob.glob(osp.join(result_root_path2, "*", "*.png"))

for r1 in result_list1:
    for r2 in result_list2:
        if osp.basename(r1) == osp.basename(r2):
            r1_img = np.float32(cv2.imread(r1, cv2.IMREAD_GRAYSCALE))
            r2_img = np.float32(cv2.imread(r2, cv2.IMREAD_GRAYSCALE))
            white_vbar = 255 * np.ones((10, r1_img.shape[1]))
            save_img = np.vstack([r1_img,white_vbar, r2_img])
            path = f'{save_path}/{osp.basename(osp.dirname(r1))}_{osp.basename(osp.dirname(r2))}_{osp.basename(r1)}'
            print(path)
            cv2.imwrite(path, save_img)
            result_list2.remove(r2)