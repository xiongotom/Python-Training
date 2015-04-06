#!/usr /bin/env python
# -*- coding: utf-8 -*-

"""
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
Pillow：Python Imaging Library
PIL.ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None)
"""

import Image, ImageDraw, ImageFont
import sys,os

original_avatar = 'weChat_avatar.png'
saved_avatar = 'new_avatar.png'
windows_font = '微软雅黑'
color = (255, 0, 0)

def __init__(self):
    curtPath = cur_file_dir()
    original_avatar = curtPath+"\\"+original_avatar
    print original_avatar
    saved_avatar = curtPath+"\\"+saved_avatar
    print saved_avatar


def draw_text(text, fill_color, windows_font):
    #try:
        path = cur_file_dir()+"\\"+original_avatar
        im = Image.open(path)
        x, y =  im.size
        print "The size of the Image is: "
        print(im.format, im.size, im.mode)
        im.show()
        
        draw = ImageDraw.Draw(im)
        #font = ImageFont.truetype(windows_font, 35)
        draw.text((x-30, 7), text, fill_color)
        
        svpath=cur_file_dir()+"\\"+saved_avatar;
        im.save(svpath)
        im.show()

    #except:
     #   print "Unable to load image"

def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

if __name__ == "__main__":
    #number = str(raw_input('please input number: '))
    number = str(4)
    draw_text(number, color, windows_font)
