import numpy as np
from get_the_picture_about_color.rgblab import rgb2lab
from Get_Palette_by_Two_center.space_2_space import rgb_2_hsv_colormath
a = np.array([ 26  ,22,  36]);
b = np.array( [ 47  ,45 , 43]);
c = np.array( [107 ,102 , 88]);
# b = rgb2lab(a)
a1 = rgb_2_hsv_colormath(a)
b1 = rgb_2_hsv_colormath(b);
c1 = rgb_2_hsv_colormath(c);
print(a1)
print(b1)
print(c1)