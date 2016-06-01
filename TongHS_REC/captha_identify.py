#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PIL import Image
from THS_REC import imtools
from THS_REC import kNN

data_set_dir = "/Users/li/Desktop/Captcha/TongHS_REC/THS_REC/"   # 训练集所在的目录
path = "./pics/1.jpg"  # 待识别的图片
dir = "/Users/li/Desktop/Captcha/TongHS_REC/THS_REC/testDigit/"  # 存放待识别图像处理过后的txt文件
im = Image.open(path)
#  二值化
res = imtools.binarized(im)

# 图片降噪增强处理
res1 = imtools.enhance(res)

# 图片平滑处理
res2 = imtools.smooth(res1)

# 干扰线去除
res3 = imtools.tiltlineremove(res2)

# 图片切割,对字符识别影响很大
block = imtools.picture_cut(res3)
for i in xrange(len(block)):
    res4 = imtools.updowncut(block[i])
    # blocks.show()
    res5 = imtools.normalize(res4, 32, 32)
    res6 = imtools.im2matrix(res5)
    # 将转化的矩阵保存为txt文件
    imtools.im2txt(res6, dir + "1_%d" % i)

# kNN 预测
pra = kNN.captcha_test(data_set_dir)  # predict data label
print "Predict label: %s" % pra
result = []
for i in range(len(pra)):
    result.append(kNN.match(pra[i]))  # predict letter
print "Predict letter: %s" % result