from os import path as osp
import glob
import shutil

root_folder_paths = [r"D:\2020\DS\Project\2020-11-18-EHWA_Teinnetwork_Test\TwinnetTest\DATA_done",
                     r"D:\2020\DS\Project\2020-11-18-EHWA_Teinnetwork_Test\TwinnetTest\DATA_SET"]

folder_list = []

for path in root_folder_paths:
    folder_list += glob.glob(osp.join(path,"*"))

for folder in folder_list:
    print(osp.basename(folder))