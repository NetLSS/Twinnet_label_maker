from PIL import Image
from glob import glob
from os import path as osp

result_root_path = r"D:\2020\DS\Project\2020-11-18-EHWA_Teinnetwork_Test\TwinnetTest\Result"
img_ext = "*.png"
"""
FN 폴더 내 형식은 a_b_c_[ref_number].png 형식이어야함.
"""

FN_list = glob(osp.join(result_root_path,"*","FN"))
FN_list += glob(osp.join(result_root_path,"*","*","FN"))

FN_count = {}

for FN_path in FN_list:

    img_list = glob(osp.join(FN_path, img_ext))
    result_dir_summ = FN_path.split("\\")[-3:]
    print(f"[FN list in {result_dir_summ}]")
    print("FN: ", end='')
    for img in img_list:
        base_name = osp.basename(img).replace(".png.png", ".png")
        number = osp.splitext(base_name)[0].split("_")[-1]
        FN_count.setdefault(int(number), 0)
        FN_count[int(number)]+=1
        print(number, end=", ")
    print("\b\b")

print(FN_count)