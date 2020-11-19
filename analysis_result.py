from PIL import Image
from glob import glob
from os import path as osp
from matplotlib import pyplot as plt
import numpy as np

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
    print(f"total FP: {len(img_list)}")


FN_count = dict(sorted(FN_count.items(), key=(lambda x: x[1]), reverse=False))
print(FN_count)

x = list(FN_count.keys())
y = list(FN_count.values())

print(x)
print(y)

plt.barh([str(key) for key in x],y)
plt.xticks(fontsize=10)
plt.xlabel("FN count")
plt.ylabel("image number")
plt.show()