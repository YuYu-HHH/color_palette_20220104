import os
from os.path import join
import numpy as np


def judge():



    # filename = "F:\palette_period\images\c928a25f9b04b58fb8e75c52e8d523.jpg";
    # filename = "F:\palette_period\images\93cdfb146505802586be7e6b75c268.jpg";
    # filename = "F:\palette_period\images\gwu_youhua.png"
    # filename = "F:\palette_period\images\BLING.jpg";
    # filename = "E:\gwu-chahua.jpg"
    # filename1 = "gwu-chahua"
    # filename = "H:\denghuo_2.png"
    # filename1 = "denghuo_2"
    # save_Path1 = "H:\Save_Path"
    # filename = "H:\yishutu_biaozhun\enwu.png"
    # filename1 = "enwu.png"
    save_Path1 = "E:\Save_Path_"
    dir = "E:\ezdrawing"
    fileNames, img_filenames = get_filenames(dir);
    save_Paths = [];
    # 文件夹中图片的数量
    img_filename_shape = len(np.array(img_filenames));
    print("一共有{}张图片".format(img_filename_shape));
    if not os.path.exists(save_Path1):
        print("文件夹不存在,正在新建中");
        os.mkdir(save_Path1);

    for i in range(img_filename_shape):
        filename1 = fileNames[i];
        save_Path = os.path.join(save_Path1, filename1);
        if not os.path.exists(save_Path):
            print("文件夹不存在,正在新建中");
            os.mkdir(save_Path);

        save_Paths.append(save_Path);

    # save_Path = os.path.join(save_Path1, filename1)



    return img_filenames,save_Paths,img_filename_shape;

def isornot_image(filename):
    return any(filename.endswith(extension) for extension in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'])


def get_filenames(dir):
    img_filenames = [];
    fileNames = [];
    for x in os.listdir(dir):
        if isornot_image(x):
            img_filename = join(dir, x);
            img_filenames.append(img_filename);
            fileName = os.path.splitext(x)[0]
            fileNames.append(fileName)

    return fileNames,img_filenames;