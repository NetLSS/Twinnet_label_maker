from PIL import Image
import glob
from os import path as osp

image_folder_path = r"V:\ADI\DATA\EHWA_ADI2_unseen_erase(rot270)\refer"
image_folder_path2 = r"V:\ADI\DATA\EHWA_ADI2_unseen_erase(rot270)\test_roi\insp"
image_folder_path3 = r"V:\ADI\DATA\EHWA_ADI2_unseen_erase(rot270)\test_roi\insp_label"

img_ext = "*.png"

images = glob.glob(osp.join(image_folder_path, img_ext))
images += glob.glob(osp.join(image_folder_path2, img_ext))
images += glob.glob(osp.join(image_folder_path3, img_ext))

for img in images:
    image = Image.open(img)
    flip_image = image.transpose(Image.ROTATE_270)
    flip_image.save(img)
    print(img)