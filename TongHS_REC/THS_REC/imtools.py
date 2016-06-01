#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from PIL import Image
import cv
import numpy
from pylab import *


def binarized(img):
    """ picture binarization
    Args:
        img:the image without binarization

    Returns:
        result: the binarized picture
    """
    picture = img.convert("RGB")
    pixels = picture.load()
    result = picture.copy()
    resultpixels = result.load()
    (width, height) = picture.size
    # 二值化 255表示白色
    for x in xrange(width):
        for y in xrange(height):
            if pixels[x, y][0] >= 200 and pixels[x, y][1] >= 200 and pixels[x, y][2] >= 200:  # 如果RGB的值都大于200则将其赋值为白色
                resultpixels[x, y] = (255, 255, 255)  # BACKCOLOR = (255, 255, 255)
            else:
                resultpixels[x, y] = (0, 0, 0)  # TEXTCOLOR = (0, 0, 0)

    return result


def enhance(img):
    """picture enhance, separating the useful and disturb information
    Args:
        img: The binarized picture
    Returns:
        result: The picture with the
    """

    picture = img.convert("RGB")
    pixels = picture.load()
    result = picture.copy()
    resultpixels = result.load()
    (width, height) = picture.size
    xx = [1, 0, -1, 0, 1, -1, 1, -1]
    yy = [0, 1, 0, -1, -1, 1, 1, -1]
    threshold = 10
    # Window = []
    for i in xrange(width):
        for j in xrange(height):
            window = [i, j]
            for k in xrange(8):  # 取3*3窗口中像素值存在Window中
                if 0 <= i + xx[k] < width and 0 <= j + yy[k] < height:
                    window.append((i + xx[k], j + yy[k]))
            window.sort()
            (x, y) = window[len(window) / 2]
            if abs(pixels[x, y][0] - pixels[i, j][0]) < threshold :    # 若差值小于阈值则进行“强化”
                if pixels[i, j][0] < 255 - pixels[i, j][0]:   # 若该点接近黑色则将其置为黑色（0），否则置为白色（255）
                    resultpixels[i, j] = (0, 0, 0)
                else:
                    resultpixels[i, j] = (255, 255, 255)
            else:
                resultpixels[i, j] = pixels[i, j]
    return result


def smooth(img):
    """平滑降噪
    Args:
        img: The binarized picture
    Returns:
        result: The picture with the
    """
    picture = img.convert("RGB")
    pixels = picture.load()
    (width, height) = picture.size
    xx = [1, 0, -1, 0]
    yy = [0, 1, 0, -1]
    for i in xrange(width):
        for j in xrange(height):
            if pixels[i, j] != (255, 255, 255):
                Count = 0
                for k in xrange(5):
                    try:
                        if pixels[i + xx[k], j + yy[k]] == (255, 255, 255):
                            Count += 1
                    except IndexError:    # 忽略访问越界的情况
                        pass
                if Count > 3:
                    pixels[i, j] = (255, 255, 255)
    return picture


def tiltlineremove(img):
    """ 去掉倾斜的直干扰线
    Args:
        img: The binarized picture
    Returns:
        result: The picture with the titLiner removed
    """
    block = img.convert("RGB")
    pixels = block.load()
    result = block.copy()
    resulpiexls = result.load()
    (width, height) = block.size
    xx = [0, -1, 0, 1]  # 4个单元点
    yy = [1, 0, -1, 0]
    xxx = [1, 0, -1, 0, 1, -1, 1, -1]  # 8个单元点
    yyy = [0, 1, 0, -1, -1, 1, 1, -1]
    xxxx = [-2, -2, -2, -2, -2, -1, -1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]  # 24个单元点
    yyyy = [-2, -1, 0, 1, 2, -2, -1, 0, 1, 2, -2, -1, 1, 2, -2, -1, 0, 1, 2, -2, -1, 0, 1, 2]
    # 循环迭代

    # 判断该点周围8个点包含的像素点的个数是否小于threshold4 = 2
    threshold4 = 2
    for i in range(width):
        for j in range(height):
            window = []
            for k in range(len(xx)):
                if 0 <= i + xx[k] < width and 0 <= j + yy[k] < height:
                    window.append((i + xx[k], j + yy[k]))  # 获取点(i,j)周围的4个单元点,上下左右
            count1 = 0
            for m in range(len(window)):
                (x, y) = window[m]
                if pixels[(x, y)][1] < 200:
                    count1 += 1
            if count1 < threshold4:
                resulpiexls[i, j] = (255, 255, 255)

    # 判断该点周围8个点包含的像素点的个数是否小于threshold8 = 5
    threshold8 = 2
    for i in range(width):
        for j in range(height):
            window = []
            for k in range(len(xxx)):
                if 0 <= i + xxx[k] < width and 0 <= j + yyy[k] < height:
                    window.append((i + xxx[k], j + yyy[k]))  # 获取点(i,j)周围的4个单元点,上下左右
            count1 = 0
            for m in range(len(window)):
                (x, y) = window[m]
                if pixels[(x, y)][1] < 200:
                    count1 += 1
            if count1 < threshold8:
                resulpiexls[i, j] = (255, 255, 255)

    # 判断该点周围8个点包含的像素点的个数是否小于threshold24 = 5
    threshold24 = 2
    for i in range(width):
        for j in range(height):
            window = []
            for k in range(len(xxxx)):
                if 0 <= i + xxxx[k] < width and 0 <= j + yyyy[k] < height:
                    window.append((i + xxxx[k], j + yyyy[k]))  # 获取点(i,j)周围的4个单元点,上下左右
            count1 = 0
            for m in range(len(window)):
                (x, y) = window[m]
                if pixels[(x, y)][1] < 200:
                    count1 += 1
            if count1 < threshold24:
                resulpiexls[i, j] = (255, 255, 255)
    return result


def picture_cut(img):
    """ image segmentation
    Args:
        img: picture
    Returns:
        blocks: the segmented pictures
    """
    global BACKCOLOR
    global TEXTCOLOR
    block = img.convert("RGB")
    pixels = block.load()
    (width, height) = block.size

    # 统计水平方向像素的个数
    pixels_count = []
    for i in xrange(height):
        count1 = 0
        for j in xrange(width):
            if pixels[j, i] == (0, 0, 0):
                count1 += 1
        pixels_count.append(count1)
    # 统计水平方向上不为零个数
    count2 = 0
    for j in xrange(height-1):
        if pixels_count[j] != 0:
            count2 += 1
    # 统计水平方向第一个非零数的位置
    count3 = 0
    for k in xrange(height-1):
        count3 += 1
        if pixels_count[k] != 0:
            break

    # 统计竖直方向像素个数
    pixels_count = []
    for i in xrange(width):
        count4 = 0
        for j in xrange(height):
            if pixels[i, j] == (0, 0, 0):
                count4 += 1
        pixels_count.append(count4)
    # 统计竖直方向非零的个数
    count5 = 0
    for i in xrange(width-1):
        if pixels_count[i] != 0:
            count5 += 1
    # 统计竖直方向第一个不为零的数
    count6 = 0
    for i in xrange(width-1):
        count6 += 1
        if pixels_count[i] != 0:
            break
    # 切割
    j = 1
    blocks = []
    for i in range(4):
        x = count6 + i*(count5/4)   # 这里的数字参数需要自己   4表示有四个参数
        y = 0           # 根据验证码图片的像素进行
        box = (x-1, y, x+(count5/4)+1, height)  # 保持上下结构不变进行左右切割
        blocks.append(img.crop(box))
        # k = (j-1)*4+i
        # a.save("test/%d.gif" % k)   # 适当的修改
        # print "j=", j
        # j += 1
    return blocks


# 对左右切割好的图片进行上下切割
def updowncut(img):
    """ image segmentation by up and down
    Args:
        img
    Returns:
        blocks
    """
    block = img.convert("RGB")
    pixels = block.load()
    (width, height) = block.size
    # 统计水平方向像素的个数
    pixelscount = []
    for i in xrange(height):
        count1 = 0
        for j in xrange(width):
            if pixels[j, i] == (0, 0, 0):
                count1 += 1
        pixelscount.append(count1)
    # 统计水平方向上不为零个数
    count2 = 0
    for j in xrange(height-1):
        if pixelscount[j] != 0:
            count2 += 1
    # print count2
    # 统计水平方向第一个非零数的位置
    count3 = 0
    for k in xrange(height-1):
        count3 += 1
        if pixelscount[k] != 0:
            break
    # print count3
    box = (0, count3-1, width, count3+count2-1)
    blocks = img.crop(box)
    return blocks


def normalize(img, m, n):
    """ 图片归一化,调整尺寸,生成相同规格的图片
    Args:
        img: the picture
        m: width
        n: height
    Returns:
        image
    """
    image = img.resize((m, n))
    return image


def rotated(img, angle):
    """ # 图片旋转,倾斜矫正
    Args:
        img
        angle
    Returns:
        image
    """
    image = img.rotate(angle)
    return image


def im2matrix(img):
    """ 将图片转化成01矩阵的形式
    Args:
        img
    Returns:
        matrix
    """
    (cols, rows) = img.size
    matrix = [[0 for col in range(cols)] for row in range(rows)]
    im = array(img)
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if im[i, j, 0] == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    return matrix


def im2txt(img, name):
    """ 将转化的矩阵保存为txt文件
    Args:
        img
    Returns:
        matrix
    """
    savetxt('%s.txt' % name, img, fmt='%d', delimiter='')  # delimiter='' represents there's nothing between two numbers


def type_rename(path, str1):
    """ 图片的格式改成指定格式的图片
    Args:
        path
        str1
    Returns:
    """
    training_file_list = os.listdir(path)
    num_samples = len(training_file_list)
    for i in xrange(num_samples):
        filename = training_file_list[i]
        [name, type] = filename.split(".")
        if filename.endswith(str1):
            a = Image.open(path+filename)
            a.save("./testDigits/%s.jpg" % name)


# knn训练
#
# if __name__ == '__main__':
#     if len(sys.argv) == 1:
#         exit('Usage: recognition.py filename.png')
#     if len(sys.argv) == 2:
#         if sys.argv[1].startswith('train'):
#             trainfiles = os.listdir(sys.argv[1])
#             #trainfiles.sort()
#             for trainfile in trainfiles:
#                 trainfile = sys.argv[1]+'/'+trainfile
#                 print trainfile
#                 im = getframe(trainfile)
#                 train(im)
#                 os.remove(trainfile)
#         else:
#             filename=sys.argv[1]
#             extension=os.path.splitext(filename)[1]
#             #print extension
#             if MODE == 'sample':
#                 samples = loadsamples()
#             else:
#                 samples = loadttf()
#             results = {}
#             im = getframe(filename)
#             #im.show()
#             #printframe(im)
#             ans = crackcode(im)
#             #print ans
#             if 'failed' in ans:
#                 im = getframe(filename,1)
#                 ans = crackcode(im)
#             for result in ans:
#                 print result
