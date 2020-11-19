from PIL import Image
import glob
from os import path as osp

image_folder_path = r"V:\ADI\DATA\EHWA_ADI2_Exp_erase_similar(fliptblr)\test_refer"
image_folder_path2 = r"V:\ADI\DATA\EHWA_ADI2_Exp_erase_similar(fliptblr)\test_roi\insp"
image_folder_path3 = r"V:\ADI\DATA\EHWA_ADI2_Exp_erase_similar(fliptblr)\test_roi\insp_label"

img_ext = "*.png"

images = glob.glob(osp.join(image_folder_path, img_ext))
images += glob.glob(osp.join(image_folder_path2, img_ext))
images += glob.glob(osp.join(image_folder_path3, img_ext))

for img in images:
    image = Image.open(img)
    flip_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    flip_image.save(img)