import numpy as np

def get_bigger_palette_to_show(palette):
    c = 50
    palette2 = np.ones((1 * c, len(palette) * c, 3))
    for i in range(len(palette)):
        palette2[:, i * c:i * c + c, :] = palette[i, :].reshape((1, 1, -1))
    return palette2

def get_bigger_palette_to_show_One(palette):
    c = 50
    palette2 = np.ones((1 * c, 1 * c, 3))
    for i in range(1):
        palette2[:, i * c:i * c + c, :] = palette.reshape((1, 1, -1))
    return palette2
def Get_Color(palette,h):
    c = 50
    palette2 = np.ones((1 * c, h, 3))
    palette2[:,  0:h, :] = palette.reshape((1, 1, -1))
    return palette2;