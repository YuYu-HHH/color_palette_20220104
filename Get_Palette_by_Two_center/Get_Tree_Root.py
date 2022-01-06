import os

from Get_Palette_by_Two_center.Get_Tree_Root_New_Test import Get_Root_about_Tree
from Get_palettes.Get_Split_further import Broken_down_further_by_Color_Depth, Broken_down_further_Get_Two_center
import numpy as np
import cv2

from show import get_bigger_palette_to_show,Get_Color


def Get_Tree_Root(result_palettes, result_weights, palette_rgb_five,t):
    colors = [];
    weights_new = [];

    for i in range(len(result_palettes)):
        result_palette = result_palettes[i];
        result_weight = result_weights[i];

        palettes1_one, palettes1_two, weights1_one, weights1_two, return1_num = Broken_down_further_by_Color_Depth(
            result_palette,result_weight);
        if return1_num == 1:
            colors1, weights_new1 = Get_Root_about_Tree(palettes1_one, weights1_one, palette_rgb_five);
            for i in range(len(colors1)):
                colors.append(colors1[i]);
                weights_new.append(weights_new1[i]);

            if len(palettes1_two) > 0:
                palettes1_two = np.array(palettes1_two);
                weights1_two = np.array(weights1_two);
                colors2, weights_new2 = Get_Root_about_Tree(palettes1_two, weights1_two, palette_rgb_five);
                for j in range(len(colors2)):
                    colors.append(colors2[j]);
                    weights_new.append(weights_new2[j]);
        else:
            if len(result_palette) > 0:
                result_palette = np.array(result_palette)
                print(result_palette.shape)
                save_Path = os.path.join("E:\Save_Path_", "00c25473cfd79c9a425c62e606ec1828");
                palette_img = get_bigger_palette_to_show(result_palette);
                save_Filename = os.path.join(save_Path, str(t) + "result_palette" + str(0) + "-vertices.png")
                cv2.imwrite(save_Filename, palette_img);

            colors1, weights_new1 = Get_Root_about_Tree(result_palette, result_weight, palette_rgb_five);
            for i in range(len(colors1)):
                colors.append(colors1[i]);
                weights_new.append(weights_new1[i]);

    return colors,weights_new;