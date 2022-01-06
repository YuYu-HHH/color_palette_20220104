# import numpy as np
# from get_the_picture_about_color.rgblab import rgb2lab
# from Get_Palette_by_Two_center.space_2_space import rgb_2_hsv_colormath
# a = np.array([ 26  ,22,  36]);
# b = np.array( [ 47  ,45 , 43]);
# c = np.array( [107 ,102 , 88]);
# # b = rgb2lab(a)
# # a1 = rgb_2_hsv_colormath(a)
# # b1 = rgb_2_hsv_colormath(b);
# # c1 = rgb_2_hsv_colormath(c);
# # print(a1)
# # print(b1)
# # print(c1)
# d = np.array([a,b,c]);
# e = np.sum(d,axis=0) / len(d)
# print(e)
import numpy as np


def delete_similar_color(colors):
    def dis_RGB(rgb1, rgb2):
        rgb3 = rgb1 - rgb2;
        if abs(rgb3[0]) < 10 and abs(rgb3[1]) < 10:
            if abs(rgb3[2]) < 50:
                return 1;
            else:
                return 0;
        elif abs(rgb3[0]) < 10 and abs(rgb3[2]) < 10:
            if abs(rgb3[1]) < 50:
                return 1;
            else:
                return 0;
        elif abs(rgb3[1]) < 10 and abs(rgb3[2]) < 10:
            if abs(rgb3[0]) < 50:
                return 1;
            else:
                return 0;
        elif abs(rgb3[0]) < 5 and abs(rgb3[1]) < 20:
            if abs(rgb3[2]) < 30:
                return 1;
            else:
                return 0;
        elif abs(rgb3[0]) < 20 and abs(rgb3[1]) < 5:
            if abs(rgb3[2]) < 30:
                return 1;
            else:
                return 0;
        elif abs(rgb3[0]) < 5 and abs(rgb3[2]) < 20:
            if abs(rgb3[1]) < 30:
                return 1;
            else:
                return 0;
        elif abs(rgb3[0]) < 20 and abs(rgb3[2]) < 5:
            if abs(rgb3[1]) < 30:
                return 1;
            else:
                return 0;
        elif abs(rgb3[1]) < 5 and abs(rgb3[2]) < 20:
            if abs(rgb3[0]) < 30:
                return 1;
            else:
                return 0;
        elif abs(rgb3[1]) < 20 and abs(rgb3[2]) < 5:
            if abs(rgb3[0]) < 30:
                return 1;
            else:
                return 0;
    colors_new = []
    index_delete = [];
    print(colors)

    for i in range(len(colors)):
        index = 0;
        for j in range(i + 1, len(colors)):
            if i != j:
                if dis_RGB(colors[i], colors[j]) == 1:
                    index = j;
                    index_delete.append([i,j]);
            print("----------------")
            print(colors[i]);
            print(colors[j]);
            print(index);
        print("=================")
        print(colors[i])
        print(index);
        if index == 0:
            colors_new.append(colors[i]);

    colors = colors_new;

    print("colorscolorscolorscolorscolorscolorscolorscolors")
    print(colors)
    return colors;
colors = [[  5  ,60 ,162],
 [ 11 ,112 ,204],
 [  2 ,226 ,220],
 [ 46 ,206, 244],
 [114 , 80 , 78],
 [168 ,122 ,135],
 [103 , 26 ,  1],
 [117 , 41 ,  5],
 [168 , 69 , 11],
 [169 , 80 , 45],
 [168 , 91 , 72]]
colors = np.array(colors);
delete_similar_color(colors);
