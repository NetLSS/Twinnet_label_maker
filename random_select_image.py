import glob
from os import path as osp
import random
import shutil

"""
refer 에서 임의로 선택된 이미지를 결과 폴더에 복사
"""

target_path = r"V:\ADI\DATA\EHWA_ADI2_Exp_split_Dataset\refer"
img_ext = "*.png"
img_ext_only = "png"

copy_path = r"V:\ADI\DATA\EHWA_ADI2_Exp_erase_similar(완전다른)\test_refer"

max_copy_imabe_num = 50

images = glob.glob(osp.join(target_path, img_ext))

already = []

for i in range(max_copy_imabe_num):
    rd_int = random.randint(0, len(images))
    while rd_int in already:
        rd_int = random.randint(0, len(images))
    already.append(rd_int)

    shutil.copy2(images[rd_int], osp.join(copy_path, f"{i+1}.{img_ext_only}"))
