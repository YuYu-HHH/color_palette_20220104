import numpy as np
from colormath.color_conversions import convert_color
from colormath.color_objects import sRGBColor, HSVColor, LabColor


# def rgbs_2_hss(rgbs):
#     hsvs = np.zeros([len(rgbs),2]);
#     for i in range(len(rgbs)):
#         rgb = rgbs[i];
#         hsv = rgb_2_hs(rgb);
#         hsvs[i] = hsv;
#     return hsvs;
#
# def rgbs_2_hsvs(rgbs):
#     hsvs = np.zeros([len(rgbs),3]);
#     for i in range(len(rgbs)):
#         rgb = rgbs[i];
#         hsv = rgb_2_hsv(rgb);
#         hsvs[i] = hsv;
#     return hsvs;
# def rgb_2_hs(rgb):
#     print(rgb)
#     RGB = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True);
#     HSV = convert_color(RGB, HSVColor);
#
#     h = HSV.hsv_h;
#     s = HSV.hsv_s;
#     hs = [];
#     hs.append(np.array([h,s]));
#     return np.array(hs);
# def rgb_2_hsv(rgb):
#     RGB = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True);
#     HSV = convert_color(RGB, HSVColor);
#
#     h = HSV.hsv_h;
#     s = HSV.hsv_s;
#     v = HSV.hsv_v;
#
#     hs = [];
#     hs.append(np.array([h,s,v]));
#     return np.array(hs);
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# def rgb_2_ab(rgb):
#
#     RGB = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True);
#     LAB = convert_color(RGB, LabColor);
#
#     a = LAB.lab_a;
#     b = LAB.lab_b;
#
#     return np.array([a,b]);
#
# def rgb_2_lab(rgb):
#     RGB = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True);
#     LAB = convert_color(RGB, LabColor);
#
#     l = LAB.lab_l;
#     a = LAB.lab_a;
#     b = LAB.lab_b;
#
#     return np.array([l,a,b]);
#
# def rgb_2_lab_l(rgb):
#     RGB = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True);
#     LAB = convert_color(RGB, LabColor);
#
#     l = LAB.lab_l;
#     a = LAB.lab_a;
#     b = LAB.lab_b;
#
#     return l
#
# def lab_2_rgb(lab):
#
#
#     LAB = LabColor(lab[0],lab[1],lab[2]);
#     RGB = convert_color(LAB, sRGBColor);
#
#     r = RGB.rgb_r;
#     g = RGB.rgb_g;
#     b = RGB.rgb_b;
#
#     return np.array([r,g,b]);
#
#
# def rgbs_2_abs(rgbs):
#     labs = np.zeros([len(rgbs),2]);
#     for i in range(len(rgbs)):
#         rgb = rgbs[i];
#         RGB1 = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True)
#         lab1 = convert_color(RGB1, LabColor)
#         # print(hsv1)
#
#         A1 = lab1.lab_a;
#         B1 = lab1.lab_b;
#
#         labs[i] = np.array([A1,B1]);
#
#     return labs;
# def rgbs_2_labs(rgbs):
#     labs = np.zeros([len(rgbs),2]);
#     for i in range(len(rgbs)):
#         rgb = rgbs[i];
#         RGB1 = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True)
#         lab1 = convert_color(RGB1, LabColor)
#         # print(hsv1)
#
#         L1 = lab1.lab_l;
#         A1 = lab1.lab_a;
#         B1 = lab1.lab_b;
#
#         labs[i] = np.array([L1,A1,B1]);
#
#     return labs;



import numpy as np
from colormath.color_conversions import convert_color
from colormath.color_objects import sRGBColor, HSVColor, LabColor
import colour
from get_the_picture_about_color.rgblab import *

def rgbs_2_hss_colormath(rgbs):
    hsvs = np.zeros([len(rgbs),2]);
    for i in range(len(rgbs)):
        rgb = rgbs[i];
        hsv = rgb_2_hs_colormath(rgb);
        hsvs[i] = hsv;
    return hsvs;

def rgbs_2_hsvs_colormath(rgbs):
    hsvs = np.zeros([len(rgbs),3]);
    for i in range(len(rgbs)):
        rgb = rgbs[i];
        hsv = rgb_2_hsv_colormath(rgb);
        hsvs[i] = hsv;
    return hsvs;
def rgb_2_hs_colormath(rgb):
    print(rgb)
    RGB = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True);
    HSV = convert_color(RGB, HSVColor);

    h = HSV.hsv_h;
    s = HSV.hsv_s;
    hs = [];
    hs.append(np.array([h,s]));
    return np.array(hs);
def rgb_2_hsv_colormath(rgb):
    RGB = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True);
    HSV = convert_color(RGB, HSVColor);

    h = HSV.hsv_h;
    s = HSV.hsv_s;
    v = HSV.hsv_v;

    hs = [];
    hs.append(np.array([h,s,v]));
    return np.array(hs);
def rgb_2_hsv_v_colormath(rgb):
    RGB = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True);
    HSV = convert_color(RGB, HSVColor);

    v = HSV.hsv_v;
    return v














def rgb_2_ab_colormath(rgb):

    RGB = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True);
    LAB = convert_color(RGB, LabColor);

    a = LAB.lab_a;
    b = LAB.lab_b;

    return np.array([a,b]);
def rgb_2_ab(rgb):
    lab = rgb2lab(rgb);
    ab = lab[1:3];
    return ab;

def rgb_2_lab_colormath(rgb):
    RGB = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True);
    LAB = convert_color(RGB, LabColor);

    l = LAB.lab_l;
    a = LAB.lab_a;
    b = LAB.lab_b;

    return np.array([l,a,b]);

def rgb_2_lab(rgb):
    return rgb2lab(rgb);

def rgb_2_lab_l_colormath(rgb):
    RGB = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True);
    LAB = convert_color(RGB, LabColor);

    l = LAB.lab_l;
    a = LAB.lab_a;
    b = LAB.lab_b;

    return l;

def rgb_2_lab_l(rgb):
    lab = rgb2lab(rgb);
    l = lab[0];
    return l;

def lab_2_rgb_colormath(lab):


    LAB = LabColor(lab[0],lab[1],lab[2]);
    RGB = convert_color(LAB, sRGBColor);

    r = RGB.rgb_r;
    g = RGB.rgb_g;
    b = RGB.rgb_b;

    return np.array([r,g,b]);

def lab_2_rgb(lab):
    return lab2rgb(lab);

def rgbs_2_abs_colormath(rgbs):
    labs = np.zeros([len(rgbs),2]);
    for i in range(len(rgbs)):
        rgb = rgbs[i];
        RGB1 = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True)
        lab1 = convert_color(RGB1, LabColor)
        # print(hsv1)

        A1 = lab1.lab_a;
        B1 = lab1.lab_b;

        labs[i] = np.array([A1,B1]);

    return labs;

def rgbs_2_abs(rgbs):
    labs = np.zeros([len(rgbs), 2]);
    for i in range(len(rgbs)):
        rgb = rgbs[i];
        lab = rgb2lab(rgb);
        labs[i] = np.array(lab[1:3]);
    return labs;

def rgbs_2_labs_colormath(rgbs):
    labs = np.zeros([len(rgbs),2]);
    for i in range(len(rgbs)):
        rgb = rgbs[i];
        RGB1 = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True)
        lab1 = convert_color(RGB1, LabColor)
        # print(hsv1)

        L1 = lab1.lab_l;
        A1 = lab1.lab_a;
        B1 = lab1.lab_b;

        labs[i] = np.array([L1,A1,B1]);

    return labs;
def rgbs_2_labs(rgbs):
    labs = np.zeros([len(rgbs), 3]);
    for i in range(len(rgbs)):
        rgb = rgbs[i];
        lab = rgb2lab(rgb);
        labs[i] = np.array(lab);
    return labs;


def sRGB_2_RGB_colour(rgb):
    lab = colour.RGB_to_LAB(rgb);

    return lab;


def rgbs_2_abs(rgbs):
    abs = np.zeros([len(rgbs),2]);
    for i in range(len(rgbs)):
        rgb = rgbs[i];
        ab = rgb2lab(rgb);
        abs[i] = ab[1:];

    return abs;

def lab_2_rgb_colormath(lab):


    LAB = LabColor(lab[0],lab[1],lab[2]);
    RGB = convert_color(LAB, sRGBColor);

    r = RGB.rgb_r;
    g = RGB.rgb_g;
    b = RGB.rgb_b;

    return np.array([r,g,b]);
