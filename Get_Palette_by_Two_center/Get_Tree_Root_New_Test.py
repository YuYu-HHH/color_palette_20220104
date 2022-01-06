from PIL import Image

from Get_Palette_by_Two_center.distance_util import distance_ab, distance_num
from Get_palettes.Get_Split_further import Broken_down_further_Get_Two_center, Broken_down_further_by_Color_Depth
from Get_palettes.Get_Tree_root import Get_Tree_root
from Get_palettes.Save_ import get_bigger_palette_to_show
from Get_Palette_by_Two_center.space_2_space import rgbs_2_hsvs_colormath, rgb_2_hsv_colormath, rgb_2_ab, rgbs_2_abs, \
    rgbs_2_labs
from get_the_picture_about_color.rgblab import lab2rgb
from palette_sorter.color_palette import ColorPalette
from palette_sorter.comprehensive_single_palette_sorter import ComprehensiveSinglePaletteSorter
import numpy as np
import cv2



def Get_Tree_Roots(result_palettes, result_weights, palette_rgb_five,k):
    colors = [];
    weights_new = [];
    for i in range(len(result_palettes)):

        result_palette = result_palettes[i];


        result_weight = result_weights[i];

        # vertices_image = get_bigger_palette_to_show(result_palette);
        # Image.fromarray((vertices_image).round().astype(np.uint8)).save(
        #     str(k) + "result_palette" + str(i) + "-vertices.png");

        if i == 0:
            color, weight_new_ = Get_Tree_root(result_palette, result_weight);
            colors.append(color);
            weights_new.append(weight_new_);
        else:
            palettes_new_one, palettes_new_two, weight_new_one, weight_new_two, return_base = Broken_down_further_Get_Two_center(
                result_palette, result_weight);
            palettes1_one, palettes1_two, weights1_one, weights1_two, return1_num = Broken_down_further_by_Color_Depth(
                palettes_new_one,weight_new_one);
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
                colors1, weights_new1 = Get_Root_about_Tree(palettes_new_one, weight_new_one, palette_rgb_five);
                for i in range(len(colors1)):
                    colors.append(colors1[i]);
                    weights_new.append(weights_new1[i]);
            if len(palettes_new_two) > 0:
                palettes2_one, palettes2_two, weights2_one, weights2_two, return2_num = Broken_down_further_by_Color_Depth(
                    palettes_new_two, weight_new_two);
                if return2_num == 1:
                    palettes2_one = np.array(palettes2_one);
                    palettes2_two = np.array(palettes2_two);
                    weights2_one = np.array(weights2_one);
                    weights2_two = np.array(weights2_two);
                    colors1, weights_new1 = Get_Root_about_Tree(palettes2_one, weights2_one, palette_rgb_five);
                    for i in range(len(colors1)):
                        colors.append(colors1[i]);
                        weights_new.append(weights_new1[i]);
                    if len(palettes2_two) > 0:
                        colors2, weights_new2 = Get_Root_about_Tree(palettes2_two, weights2_two, palette_rgb_five);
                        for j in range(len(colors2)):
                            colors.append(colors2[j]);
                            weights_new.append(weights_new2[j]);
                else:
                    if len(palettes_new_two) > 0:
                        colors2, weights_new2 = Get_Root_about_Tree(palettes_new_two, weight_new_two, palette_rgb_five);
                        for j in range(len(colors2)):
                            colors.append(colors2[j]);
                            weights_new.append(weights_new2[j]);

            # vertices_image = get_bigger_palette_to_show(palettes_new_one);
            # Image.fromarray((vertices_image).round().astype(np.uint8)).save(
            #     "palettes_new_one" + str(i) + "_one-Split_Sorted-vertices.png");
            # if len(palettes_new_two) > 0:
            #     vertices_image_ = get_bigger_palette_to_show(palettes_new_two);
            #     Image.fromarray((vertices_image_).round().astype(np.uint8)).save(
            #         "palettes_new_two" + str(i) + "_two-Split_Sorted-vertices.png");


            # 排序
            # colors1, weights_new1 = Get_Root_about_Tree(palettes_new_one,weight_new_one,palette_rgb_five);
            # for i in range(len(colors1)):
            #     colors.append(colors1[i]);
            #     weights_new.append(weights_new1[i]);
            # if len(palettes_new_two) > 0:
            #     colors2, weights_new2 = Get_Root_about_Tree(palettes_new_two,weight_new_two,palette_rgb_five);
            #     for j in range(len(colors2)):
            #         colors.append(colors2[j]);
            #         weights_new.append(weights_new2[j])




    return colors, weights_new;




def Get_Tree_Roots1(result_palettes, result_weights, palette_rgb_five, len_index,k):
    colors = [];
    weights_new = [];
    for i in range(len_index):
        result_palette = result_palettes[i];
        result_weight = result_weights[i];
        result_palette_hsv = rgbs_2_hsvs_colormath(result_palette);

        vertices_image = get_bigger_palette_to_show(result_palette);
        Image.fromarray((vertices_image).round().astype(np.uint8)).save(
            str(k) + "result_palette" + str(i) + "-vertices.png");
        if i == 0:
            color, weight_new_ = Get_Tree_root(result_palette, result_weight);
            colors.append(color);
            weights_new.append(weight_new_);
        else:
            # palettes_new_one, palettes_new_two, weight_new_one, weight_new_two, return_base = Broken_down_further_Get_Two_center(
            #     result_palette, result_weight);
            palettes1_one, palettes1_two, weights1_one, weights1_two, return1_num = Broken_down_further_by_Color_Depth(
                result_palette,result_weight);
            palettes1_one = np.array(palettes1_one);
            palettes1_two = np.array(palettes1_two);
            weights1_one = np.array(weights1_one);
            weights1_two = np.array(weights1_two);
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
                colors1, weights_new1 = Get_Root_about_Tree(result_palette, result_weight, palette_rgb_five);
                for i in range(len(colors1)):
                    colors.append(colors1[i]);
                    weights_new.append(weights_new1[i]);

            # vertices_image = get_bigger_palette_to_show(palettes_new_one);
            # Image.fromarray((vertices_image).round().astype(np.uint8)).save(
            #     "palettes_new_one" + str(i) + "_one-Split_Sorted-vertices.png");
            # if len(palettes_new_two) > 0:
            #     vertices_image_ = get_bigger_palette_to_show(palettes_new_two);
            #     Image.fromarray((vertices_image_).round().astype(np.uint8)).save(
            #         "palettes_new_two" + str(i) + "_two-Split_Sorted-vertices.png");


            # 排序
            # colors1, weights_new1 = Get_Root_about_Tree(palettes_new_one,weight_new_one,palette_rgb_five);
            # for i in range(len(colors1)):
            #     colors.append(colors1[i]);
            #     weights_new.append(weights_new1[i]);
            # if len(palettes_new_two) > 0:
            #     colors2, weights_new2 = Get_Root_about_Tree(palettes_new_two,weight_new_two,palette_rgb_five);
            #     for j in range(len(colors2)):
            #         colors.append(colors2[j]);
            #         weights_new.append(weights_new2[j])




    return colors, weights_new;













def Get_Tree_Roots_1(result_palettes, result_weights, palette_rgb_five, len_index, k):
    colors = [];
    weights_new = [];
    for i in range(len_index):
        result_palette = result_palettes[i];
        result_weight = result_weights[i];
        base_ = 0
        for j in range(len(result_palette)):

            if result_palette[j] in palette_rgb_five:
                base_ = 1;
                colors.append(result_palette[j]);
                weights_new.append(result_weight[j]);
        if base_ == 0:
            max_index = np.argmax(result_weight);
            colors.append(result_palette[max_index]);
            weights_new.append(np.sum(result_weight));
    return colors,weights_new




def Get_Root_about_Tree(palettes_new_one,weight_new_one,palette_rgb_five):
    colors = [];
    weights_new = [];
    yes = 0;
    for i in range(len(palettes_new_one)):
        if palettes_new_one[i]  in palette_rgb_five:
            yes = 1;
    if len(palettes_new_one) > 1:
        palettes_new_one_Color = ColorPalette(palettes_new_one);
        target_spaces = ['rgb', 'hsv', 'vhs', 'lab'];
        palettes_new_one_sorted = ComprehensiveSinglePaletteSorter(palettes_new_one_Color, target_spaces)
        standard_sorted_indices = palettes_new_one_sorted.standard_sort();
        print(palettes_new_one);
        palettes_new_one = np.array(palettes_new_one);
        weight_new_one = np.array(weight_new_one);
        palettes_sorted_one = palettes_new_one[standard_sorted_indices];
        weights_sorted_one = weight_new_one[standard_sorted_indices];
        base_ = 0;
        colors_new1 = [];
        weights_new1 = [];
        for i in range(len(palettes_sorted_one)):
            palette_one = palettes_sorted_one[i];
            weight_one = weights_sorted_one[i];
            if palette_one in palette_rgb_five:
                colors.append(palette_one);
                weights_new.append(weight_one);
                base_ = 1;
            elif weight_one > 10000:
                colors.append(palette_one);
                weights_new.append(weight_one);
                base_ = 1;
        if base_ == 1:
            palette_ab = rgbs_2_abs(colors);
            palette_lab = rgbs_2_labs(colors);
            print(palette_ab)
            print(colors)
            palette_ab = np.array(palette_ab)
            if len(colors) > 1:
                palette_ab = np.array(palette_ab, np.float32);
                (x2, y2), radius2 = cv2.minEnclosingCircle(palette_ab);
                if radius2 < 8:
                    colors_new1.append(lab2rgb(np.sum(palette_lab,axis=0) / len(palette_lab)));
                    weights_new1.append(np.sum(weights_new));

                else:
                    pixels_one,pixels_two,pixels_one_ab,pixels_two_ab,weights_one,weights_two = Get_Two_Center(colors,weights_new);
                    if len(pixels_one_ab) > 1:
                        pixels_one_ab = np.array(pixels_one_ab, np.float32);
                        (x2, y2), radius2 = cv2.minEnclosingCircle(pixels_one_ab);
                        palette_one_lab = rgbs_2_labs(pixels_one);
                        if radius2 < 8:
                            colors_new1.append(lab2rgb(np.sum(palette_one_lab, axis=0) / len(palette_one_lab)));
                            weights_new1.append(np.sum(weights_one));
                    elif len(pixels_one_ab) == 1:
                        colors_new1.append(pixels_one);
                        weights_new1.append(weights_one);

                    if len(pixels_two_ab) > 1:
                        pixels_two_ab = np.array(pixels_two_ab, np.float32);
                        (x2, y2), radius2 = cv2.minEnclosingCircle(pixels_two_ab);
                        palette_one_lab = rgbs_2_labs(pixels_two);
                        if radius2 < 8:
                            colors_new1.append(lab2rgb(np.sum(palette_one_lab, axis=0) / len(palette_one_lab)));
                            weights_new1.append(np.sum(weights_two));
                    elif len(pixels_two_ab) == 1:
                        colors_new1.append(pixels_two);
                        weights_new1.append(weights_two);
        if base_ == 0:
            arg = np.argmax(weights_sorted_one);
            colors.append(palettes_sorted_one[arg]);
            weights_new.append(weights_sorted_one[arg]);
    else:
        colors.append(palettes_new_one[0]);
        weights_new.append(weight_new_one[0]);
    return colors, weights_new;



def Get_Two_Center(palettes,weights):
    # print(palettes)
    dis_base = 0;
    index_base = np.zeros(2);
    # 1.先找出来两个距离最远的点
    #
    # print("---------------------------------------")
    for i in range(len(palettes)):
        for j in range(len(palettes)):
            dis = distance_num(rgb_2_ab(palettes[i]), rgb_2_ab(palettes[j]));
            # print(dis)
            # print(dis_base)
            if dis > dis_base:
                index_base = [i, j];
                dis_base = dis;

        # 2.分成两个中心
        # print(index_base)
        # print(palettes)
    center_two_one = palettes[int(index_base[0])];
    center_two_two = palettes[int(index_base[1])];
    # weights_one = weights[int(index_base[0])];
    # weights_two = weights[int(index_base[1])];
    center_two_one_ab = rgb_2_ab(center_two_one);
    center_two_two_ab = rgb_2_ab(center_two_two);

    labels = np.zeros([len(palettes)]);

    pixels_one_ab = [];
    pixels_two_ab = [];
    pixels_one = [];
    pixels_two = [];
    weights_one = [];
    weights_two = [];
    for i in range(len(palettes)):
        palette = palettes[i];
        weight = weights[i]
        palette_ab = rgb_2_ab(palette);

        dis_one = distance_num(palette_ab, center_two_one_ab);
        dis_two = distance_num(palette_ab, center_two_two_ab);

        if dis_one < dis_two:
            labels[i] = 0;
            pixels_one_ab.append(palette_ab);
            pixels_one.append(palette);
            weights_one.append(weight)

            # 将中心更换为圆心
            palettes_ab1 = np.array(pixels_one_ab, np.float32);
            (x1, y1), radius1 = cv2.minEnclosingCircle(palettes_ab1);
            center_two_one_ab = np.array([x1, y1]);


        elif dis_one > dis_two:
            labels[i] = 1;
            pixels_two_ab.append(palette_ab);
            pixels_two.append(palette)
            weights_two.append(weight)
            palettes_ab2 = np.array(pixels_two_ab, np.float32);
            (x2, y2), radius2 = cv2.minEnclosingCircle(palettes_ab2);
            center_two_two_ab = np.array([x2, y2]);
        # elif dis_one == dis_two:
        #     pixels_one_ab.append(palette_ab);
        #     pixels_one.append(palette);
        #     pixels_two_ab.append(palette_ab);
        #     pixels_two.append(palette);

    return pixels_one,pixels_two,pixels_one_ab,pixels_two_ab,weights_one,weights_two;