from os import path as osp
import glob
import shutil

insp_path = r"V:\ADI\DATA\EHWA_ADI2_Exp_ArtificialD\test_roi\insp"
refer_path = r"V:\ADI\DATA\EHWA_ADI2_Exp_split_Dataset\refer"

refer_save_path = r"V:\ADI\DATA\EHWA_ADI2_Exp_ArtificialD\refer"

insp_list = glob.glob(insp_path+"\\*.png")

print(insp_list)

insp_list = [x.split("_")[-1].split(".")[0] for x in insp_list]  # ref number only
insp_list = set(insp_list)
insp_list = list(insp_list)
print(insp_list)

not_exist_list = []

for insp in insp_list:
    insp += ".png"
    if osp.exists(osp.join(refer_path,insp)):
        shutil.copy(osp.join(refer_path,insp), osp.join(refer_save_path, insp))
    else:
        not_exist_list.append(insp)


print(f"not exist files: {not_exist_list}")

