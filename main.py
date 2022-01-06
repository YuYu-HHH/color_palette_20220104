


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
import time

import numpy as np

from Get_Palette_by_Two_center.Get_Palette_by_Two_center import Get_Palette_by_Two_center

if __name__ == '__main__':
    # filename_Path = "E:\gwu-chahua.jpg";
    # filename = "gwu-chahua"
    # filename_Path = "E:\BingWallpaper.jpg";
    # filename = "BingWallpaper";
    # filename_Path = "E:\out.png";
    # filename = "out";
    # filename_Path = "E:\DSC01270.jpg"
    # filename = "DSC01270"

    # filename_Path = "E:\DSC00904.JPG"
    # filename = "DSC00904"

    # filename_Path = "E:\DSC00907.JPG"
    # filename = "DSC00907"
    # filename_Path = os.path.join("E:\ezdrawing", "00c25473cfd79c9a425c62e606ec1828.jpg")
    # # filename_Path = "E:\ezdrawing"
    # filename = "00c25473cfd79c9a425c62e606ec1828"
    #
    # save_Path1 = "E:\Save_Path_"
    # save_Path = os.path.join(save_Path1, filename)
    #
    # if not os.path.exists(save_Path):
    #     print("文件夹不存在,正在新建中");
    #     os.mkdir(save_Path1);
    # if not os.path.exists(save_Path):
    #     print("文件夹不存在,正在新建中");
    #     os.mkdir(save_Path);
    #
    # Get_Palette_by_Two_center(filename_Path, save_Path);


    from utils.judge_file import judge

    fileNames, save_Paths, img_filename_shape = judge();

    t1 = time.time();
    for i in range(img_filename_shape):
        print("第 %d 张图片 " % (i + 1));
        print("图片名称为：",fileNames[i])
        filename = fileNames[i];
        save_Path = save_Paths[i];

        Get_Palette_by_Two_center(filename, save_Path);
    t2 = time.time();

# See PyCharm help at https://www.jetbrains.com/help/pycharm/