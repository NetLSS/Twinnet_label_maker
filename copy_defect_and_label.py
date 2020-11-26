import numpy as np
import cv2
import os
import random
import datetime as dt

"""
원본이미지, label파일(0 or 255로 구성)을 생성
복사 경우 이미지 특정 부분을 따와서 복사/붙여넣기 가능 (마우스 우클릭)
"""

curr_idx = 0
filter_size = 1
clicked = False
clicked_R = False
show_label = False
edited = False
cropping = False
w_flag = False
h_flag = False
w_offset = 2
h_offset = 5

current_w_offset = 2
current_h_offset = 5

timestamp_save_mode = True


def extractImg(filepath):
    global curr_idx, show_label, filter_size, edited
    edited = False
    imgpath = filepath[0]
    lblpath = filepath[1]
    label_savepath = r"V:\ADI\DATA\EHWA_ADI2_Exp_ArtificialD\test_roi\insp_label"  # "D:\public\Hee1\ADI\For_Check_Data\defect_data"
    insp_savepath = r"V:\ADI\DATA\EHWA_ADI2_Exp_ArtificialD\test_roi\insp"  # "D:\public\Hee1\ADI\For_Check_Data\defect_data\insp"  # -------------------
    print(imgpath)
    img = cv2.imread(imgpath, 0)
    h, w = img.shape[:2]
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    label = cv2.imread(lblpath, 0) if os.path.exists(lblpath) else np.zeros((h, w))
    cv2.namedWindow("img", 0)
    cv2.namedWindow("lbl", 0)


    temp_img = np.copy(img)
    temp_label = np.copy(label)
    if label.max() == 1:
        label *= 255

    def paint(image, x, y, filter_size):
        global edited
        edited = True
        if filter_size == 1:
            image[y][x] = 255
            return image

        h, w = image.shape[:2]
        fz = int(filter_size / 2)
        stx = x - fz
        edx = x + fz
        sty = y - fz
        edy = y + fz
        if stx < 0:
            stx = 0
        if sty < 0:
            sty = 0
        if stx >= w:
            stx = w - 1
        if edy >= h:
            edy = h - 1
        image[sty:edy, stx:edx] = 255

        return image

    def tt(event, x, y, flags, param):
        global clicked, gv, cropping, crop, w_offset, h_offset, edited, h_flag, w_flag, clicked_R, current_w_offset, current_h_offset
        nonlocal label

        if event == cv2.EVENT_LBUTTONDOWN:
            clicked = True
            label = paint(label, x, y, filter_size)
            gv = 85
            img[y][x] = (gv, gv, gv)  # -------------------
            # label[y][x] = 255

        elif event == cv2.EVENT_RBUTTONDOWN:  # ---------------------------------------------우클릭으로 이미지 떼서 붙임
            if cropping == False:
                crop = img[y - h_offset:y + h_offset, x - w_offset:x + w_offset]
                current_w_offset = w_offset
                current_h_offset = h_offset
                cv2.imshow('crop', crop)
                cropping = True
            else:
                clicked_R = True
                edited = True
                img[y - current_h_offset:y + current_h_offset, x - current_w_offset:x + current_w_offset] = crop
                label[y - current_h_offset:y + current_h_offset, x - current_w_offset:x + current_w_offset] = 255
    #  elif event == cv2.EVENT_RBUTTONUP:
            # cropping = True

        elif event == cv2.EVENT_MOUSEWHEEL:

            cropping = False
            if flags > 0:
                if flags & cv2.EVENT_FLAG_SHIFTKEY:
                    h_offset += 1
                    print(f"h_offset: {2 * h_offset}")
                else:
                    w_offset += 1
                    print(f"w_offset: {2 * w_offset}")

            else:
                if flags & cv2.EVENT_FLAG_SHIFTKEY:
                    h_offset -= 1
                    if h_offset <= 0:
                        h_offset = 1
                    print(f"h_offset: {2 * h_offset}")
                else:
                    w_offset -= 1
                    if w_offset <= 0:
                        w_offset = 1
                    print(f"w_offset: {2 * w_offset}")



        elif event == cv2.EVENT_MOUSEMOVE:

            if clicked:
                label = paint(label, x, y, filter_size)
            elif clicked_R:
                img[y - current_h_offset:y + current_h_offset, x - current_w_offset:x + current_w_offset] = crop
                label[y - current_h_offset:y + current_h_offset, x - current_w_offset:x + current_w_offset] = 255
                # label[y][x] = 255
            # print("x:{}, y:{}".format(x, y))
            if flags & cv2.EVENT_FLAG_SHIFTKEY:
                img[y - current_h_offset:y + current_h_offset, x - current_w_offset:x + current_w_offset] = crop
                label[y - current_h_offset:y + current_h_offset, x - current_w_offset:x + current_w_offset] = 255
                if not edited:
                    edited = True

        elif event == cv2.EVENT_LBUTTONUP:
            clicked = False

        elif event == cv2.EVENT_RBUTTONUP:
            clicked_R = False



    cv2.setMouseCallback("img", tt)

    while (1):
        global w_flag, h_flag, cropping
        if show_label:
            if label.sum() > 0:
                row, col = label.nonzero()
                img[row, col] = (0, 255, 0)  # show label in green in image
        cv2.imshow("img", img)
        cv2.imshow("lbl", label)
        key = cv2.waitKey(22)

        if key == 27:  # esc
            curr_idx = 999999999
            break

        elif key == 122 or key == 90:  # z | Z
            label = np.zeros_like(img[:, :, 0])
        elif key == 99:  # c(clear)
            # cropping = False
            break
        elif key == 97:  # a
            curr_idx -= 1
            if edited:
                print(f"image saved: {os.path.join(label_savepath, os.path.basename(lblpath))}")
                print(f"image saved: {os.path.join(insp_savepath, os.path.basename(lblpath))}")

                if timestamp_save_mode:
                    timestamp = str(dt.datetime.now().timestamp())
                    label_file_name = f"{timestamp}_{lblpath.split('_')[-1]}"
                    cv2.imwrite(os.path.join(label_savepath, os.path.basename(label_file_name)), label)
                    cv2.imwrite(os.path.join(insp_savepath, os.path.basename(label_file_name)), img)
                    break

                cv2.imwrite(os.path.join(label_savepath, os.path.basename(lblpath)), label)
                cv2.imwrite(os.path.join(insp_savepath, os.path.basename(lblpath)), img)  # -------------------
            break

        # elif key == 119:  # w
        #     w_flag = True
        #     break
        #
        # elif key == 104:  # h
        #     h_flag = True
        #     break

        elif key == 98:  # b
            show_label = not show_label
            print("SHOW LABEL :", show_label)
            if not show_label:
                img = np.copy(temp_img)

        elif key == 100:  # d
            curr_idx += 1
            print(curr_idx)
            if edited:
                print(f"image saved: {os.path.join(label_savepath, os.path.basename(lblpath))}")
                print(f"image saved: {os.path.join(insp_savepath, os.path.basename(lblpath))}")

                if timestamp_save_mode:
                    timestamp = str(int(dt.datetime.now().timestamp()))
                    label_file_name = f"{timestamp}_{lblpath.split('_')[-1]}"
                    cv2.imwrite(os.path.join(label_savepath, os.path.basename(label_file_name)), label)
                    cv2.imwrite(os.path.join(insp_savepath, os.path.basename(label_file_name)), img)
                    break

                cv2.imwrite(os.path.join(label_savepath, os.path.basename(lblpath)), label)
                cv2.imwrite(os.path.join(insp_savepath, os.path.basename(lblpath)), img)
            break

        elif key == 114:  # r
            cropping = False
            break

        elif key == 113:  # q
            curr_idx = 999999999
            break

        elif key == 109:  # m (move)
            print(f"current index : {curr_idx}")
            move_index = input("move index :")
            curr_idx = int(move_index)  # curr_idx # setting move index
            break

        elif key >= 49 and key <= 57:
            filter_size = key - 48
            print("filter_size : ", filter_size)
    cv2.destroyAllWindows()


rootdir = r"V:\ADI\DATA\EHWA_ADI2_Exp_split_Dataset\train_roi"  # "D:\public\Hee1\ADI\For_Check_Data\raw_data\crop_adi1s1"
test_label = os.path.join(rootdir, 'insp_label')
test_img = os.path.join(rootdir, 'insp')
imgs = [os.path.join(test_img, f) for f in os.listdir(test_img) if f.endswith((".jpeg", ".jpg", ".bmp", ".png"))]
labels = [os.path.join(test_label, os.path.basename(f)) for f in imgs]
while curr_idx < len(imgs):
    extractImg((imgs[curr_idx], labels[curr_idx]))
