import glob
from os import path as osp
import os

target_path = r"V:\ADI\DATA\EHWA_ADI2_Exp_erase_similar(same)\test_refer"

img_ext = "*.png"
img_ext_only = "png"

images = glob.glob(osp.join(target_path, img_ext))

for f in images:
    number = int(osp.splitext(osp.basename(f))[0].split("_")[-1])
    print(number)
    os.rename(f, osp.join(osp.dirname(f), f"{number}.{img_ext_only}"))