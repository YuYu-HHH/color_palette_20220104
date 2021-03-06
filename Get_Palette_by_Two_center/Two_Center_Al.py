import cv2
from Get_Palette_by_Two_center.distance_util import distance_num
import numpy as np

from Get_Palette_by_Two_center.draw_figure import draw_figure
from Get_Palette_by_Two_center.space_2_space import rgb_2_ab, rgbs_2_abs

class Colors:
    def __init__(self):
        self.colors = [];

    def two_center(self,palettes,ok):
        yes = 0;
        self.two_center_one(palettes, yes,ok);
        return self.colors;

    def two_center_one(self ,palettes,yes,ok):
        if len(palettes) > 8:
            yes = 0;
        if yes == 1:
            self.colors.append(palettes);
        elif yes == 0:
            # print("=====================================")
            # print(palettes)
            pixels_one, pixels_two, pixels_one_ab, pixels_two_ab = self.Get_Two_Center(palettes);
            xy1, xy2, yes = self.Verify_color_group_by_distance_LAB(pixels_one_ab, pixels_two_ab);

            if ok == 1:
                pixels_one_ab = np.array(pixels_one_ab, np.float32);
                # print(palettes_ab1)
                (x1, y1), radius1 = cv2.minEnclosingCircle(pixels_one_ab);
                if radius1 < 5:
                    self.two_center_one(pixels_one, 1, ok);
                else:
                    self.two_center_one(pixels_one, 0, ok);
                pixels_two_ab = np.array(pixels_two_ab, np.float32);
                # print(palettes_ab1)
                (x1, y1), radius1 = cv2.minEnclosingCircle(pixels_two_ab);
                if radius1 < 5:
                    self.two_center_one(pixels_two, 1, ok);
                else:
                    self.two_center_one(pixels_two, 0, ok);
                if len(pixels_one) == 1:
                    self.two_center_one(pixels_one, 1,ok);
                    self.two_center_one(pixels_two, yes,ok);
                if len(pixels_two) == 1:
                    self.two_center_one(pixels_one, yes,ok);
                    self.two_center_one(pixels_two, 1,ok);
                if len(pixels_one) != 1 and len(pixels_two) != 1:
                    self.two_center_one(pixels_one, yes,ok);
                    self.two_center_one(pixels_two, yes,ok);
            else:
                if len(pixels_one) == 1:
                    self.two_center_one(pixels_one, 1,ok);
                    self.two_center_one(pixels_two, yes,ok);
                if len(pixels_two) == 1:
                    self.two_center_one(pixels_one, yes,ok);
                    self.two_center_one(pixels_two, 1,ok);
                if len(pixels_one) != 1 and len(pixels_two) != 1:
                    self.two_center_one(pixels_one, yes,ok);
                    self.two_center_one(pixels_two, yes,ok);

                # print(yes)




    def Get_info(self,pixel):
        pixels_one, pixels_two, pixels_one_ab, pixels_two_ab = self.Get_Two_Center(pixel);
        return pixels_one, pixels_two;

    def Get_Two_Center(self,palettes):
        # print(palettes)
        dis_base = 0;
        index_base = np.zeros(2);
        # 1.????????????????????????????????????
        # print("---------------------------------------")
        for i in range(len(palettes)):
            for j in range(len(palettes)):

                dis = distance_num(rgb_2_ab(palettes[i]), rgb_2_ab(palettes[j]));
                # print(dis)
                # print(dis_base)
                if dis > dis_base:
                    index_base = [i, j];
                    dis_base = dis;

        # 2.??????????????????
        # print(index_base)
        # print(palettes)
        center_two_one = palettes[int(index_base[0])];
        center_two_two = palettes[int(index_base[1])];
        center_two_one_ab = rgb_2_ab(center_two_one);
        center_two_two_ab = rgb_2_ab(center_two_two);

        labels = np.zeros([len(palettes)]);

        pixels_one_ab = [];
        pixels_two_ab = [];
        pixels_one = [];
        pixels_two = [];
        for i in range(len(palettes)):
            palette = palettes[i];
            palette_ab = rgb_2_ab(palette);

            dis_one = distance_num(palette_ab, center_two_one_ab);
            dis_two = distance_num(palette_ab, center_two_two_ab);

            if dis_one < dis_two:
                labels[i] = 0;
                pixels_one_ab.append(palette_ab);
                pixels_one.append(palette);


                # ????????????????????????
                palettes_ab1 = np.array(pixels_one_ab, np.float32);
                (x1, y1), radius1 = cv2.minEnclosingCircle(palettes_ab1);
                center_two_one_ab = np.array([x1, y1]);


            elif dis_one > dis_two:
                labels[i] = 1;
                pixels_two_ab.append(palette_ab);
                pixels_two.append(palette)

                palettes_ab2 = np.array(pixels_two_ab, np.float32);
                (x2, y2), radius2 = cv2.minEnclosingCircle(palettes_ab2);
                center_two_two_ab = np.array([x2, y2]);
            # elif dis_one == dis_two:
            #     pixels_one_ab.append(palette_ab);
            #     pixels_one.append(palette);
            #     pixels_two_ab.append(palette_ab);
            #     pixels_two.append(palette);

        return pixels_one,pixels_two,pixels_one_ab,pixels_two_ab;

    def Verify_color_group_by_distance_LAB(self,palettes_ab1,palettes_ab2):
        yes = 1;

        # xy1 = np.zeros([len(palettes_ab1),2]);
        # xs1 = np.zeros([len(palettes_ab1)]);
        # ys1 = np.zeros([len(palettes_ab1)]);
        # radiuss1 = np.zeros(len(palettes_ab1));

        palettes_ab1 = np.array(palettes_ab1, np.float32);
        # print(palettes_ab1)
        (x1, y1), radius1 = cv2.minEnclosingCircle(palettes_ab1);
        xy1 = np.array([x1,y1])
        # ??????????????????
        # draw_figure(palettes_ab1, x1, y1, radius1);

        # xy2 = np.zeros([len(palettes_ab2), 2]);
        # xs2 = np.zeros([len(palettes_ab2)]);
        # ys2 = np.zeros([len(palettes_ab2)]);
        # radiuss2 = np.zeros(len(palettes_ab2));

        palettes_ab2 = np.array(palettes_ab2, np.float32);
        (x2, y2), radius2 = cv2.minEnclosingCircle(palettes_ab2);
        xy2 = np.array([x2, y2])

        # ??????????????????
        # draw_figure(palettes_ab2, x2, y2, radius2);


        if distance_num(xy1,xy2) < (radius1 + radius2 ):

            # print("???????????????????????????????????????");
            yes = 0;
        else:
            # print("?????????????????????????????????")
            yes = 1;

        #??????????????????
        # draw_entire_figure(palettes_not_sorted_hsv,xs,ys,radiuss);
        # print(xy);
        # print(radiuss);
        return xy1,xy2,yes;
