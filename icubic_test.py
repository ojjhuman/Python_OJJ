import numpy as np
from PIL import Image


def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

empty = 0
px_w = 16
px_h = 20
im_to_color = np.zeros((px_h,px_w,3))
num_array = np.zeros((px_h,px_w))
color_array = np.zeros((px_h,px_w))
color_tuple = [0,0,0]

im = Image.open("01.jpg")
sizew_1pixel = im.size[0]//px_w
sizeh_1pixel = im.size[1]//px_h
print(im.format,im.size,im.mode)
im_to_color = im_to_color.astype(int)
color_array = color_array.astype(str)
for i in range(px_h):
    for j in range(px_w):
        empty = 1
        im_to_color[i][j] = im.getpixel((sizew_1pixel//2 + sizew_1pixel*j ,sizeh_1pixel//2 + sizeh_1pixel*i))

        #(type(color_tuple[0]))
        color_array[i][j] = rgb2hex(im_to_color[i][j][0],im_to_color[i][j][1],im_to_color[i][j][2])
        #num_array[i][j] = rgb_to_hex(color_tuple)
        #print(im_to_color[i][j])
    #print("\n")
#im_to_color = im_to_color.astype(int)
#num_array = num_array.astype(int)
print(num_array[3][5])
print(type(im_to_color[1][1][0]))
for i in range(px_h):
    temp_num = 1
    jth = px_w -1
    for j in reversed(range(px_w)):

        if j != 0:
            if im_to_color[i][j][0] == im_to_color[i][j-1][0] and im_to_color[i][j][1] == im_to_color[i][j-1][1] and im_to_color[i][j][2] == im_to_color[i][j-1][2]:
                temp_num += 1
            else:
                num_array[i][jth] = temp_num
                jth += -1
                temp_num = 1
        else:
            num_array[i][jth] = temp_num

print(num_array)
print(color_array)
print(im_to_color[12][11][0])
im.show()
#for test11111222
