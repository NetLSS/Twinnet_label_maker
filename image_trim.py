import cv2 #cv2 임포트
from os import path as osp
from glob import glob


target_img = r"Z:\sslee\project\2020-12-03-contour\[bf_total]unet-conv2_compound0.7_adam(0.001)-2020-12-02(11h50m)\2020-12-03(13h19m)\FP\1_1274(iou_0.00).bmp"
desktop_path = r"C:\Users\sangsu lee\Desktop"

target_path = r"Z:\sslee\project\2020-12-03-contour\FP"
target_img_list = glob(osp.join(target_path, "*.bmp"))
save_path = r"D:\2020\DS\Project\2020-12-07-contour_image\FP"

def im_trim (img): #함수로 만든다
    x = 640+2+640+2+640+2; y = 0; #자르고 싶은 지점의 x좌표와 y좌표 지정
    w = 640; h = 640; #x로부터 width, y로부터 height를 지정
    img_trim = img[y:y+h, x:x+w] #trim한 결과를 img_trim에 담는다
    #cv2.imwrite('org_trim.jpg',img_trim) #org_trim.jpg 라는 이름으로 저장
    return img_trim #필요에 따라 결과물을 리턴

# org_image = cv2.imread(target_img) #test.jpg 라는 파일을 읽어온다
# trim_image = im_trim(org_image) #trim_image 변수에 결과물을 넣는다
print(target_img_list)
for file in target_img_list:
    print(file)
    org_image = cv2.imread(file)  # test.jpg 라는 파일을 읽어온다
    trim_image = im_trim(org_image)  # trim_image 변수에 결과물을 넣는다
    cv2.imwrite(osp.join(save_path, osp.basename(file)), trim_image)

# cv2.imwrite(osp.join(desktop_path, osp.basename(target_img)), trim_image)
# print(osp.join(desktop_path, osp.basename(target_img)).replace("\\","\\\\"))