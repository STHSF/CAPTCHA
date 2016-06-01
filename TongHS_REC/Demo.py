#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import THS_REC.kNN

"""验证码图像批处理流程"""

back_color = (255, 255, 255)
text_color = (0, 0, 0)

# # 图片二值化,降噪,平滑,干扰线去除处理
# str = ".jpg"
# dir = "./pics/"
# path = "./enhance/"
# for f in os.listdir(dir):
#     if f.endswith(str):
#         img = Image.open(dir+f)
#         # 图片二值化
#         res = imtools.binarized(img)
#         # 图片降噪增强处理
#         res1 = imtools.enhance(res)
#         # 图片平滑处理
#         res2 = imtools.smooth(res1).save(path+f, "PNG")
#         # 干扰线去除
#         # imtools.tiltlineremove(res).save(path+f, "PNG")


# # 保存分割的图片
# dir = "./enhance/"
# count = 0
# for f in os.listdir(dir):
#     if f.endswith(str):
#         img = Image.open(dir+f)
#         block = imtools.picturecut(img)
#         for i in xrange(len(block)):
#             k = i+len(block)*count
#             block[i].save("./fonts/%d.png" % k)
#         count += 1


# # 手动分割图片
# count = 0
# img = Image.open("./enhance/267.jpg")
# block = imtools.picturecut(img)
# print len(block)
# for i in xrange(len(block)):
#     # k = i+len(block)*count
#     block[i].save("./tests/%d.bmp" % i)
#     count += 1

# # 切割后的图片上下空白重新切割
# dir = "/Users/li/Desktop/Captcha/recognition/recogtest/train/"
# path = "/Users/li/Desktop/Captcha/recognition/recogtest/trainingDigit/"
# count = 0
# for f in os.listdir(dir):
#     if f.endswith(".bmp"):
#         img = Image.open(dir+f)
#         imtools.updowncut(img).save(path+f)


# # 对分割的图片进行归一化处理
# dir = "/Users/li/Desktop/Captcha/recognition/recogtest/trainingDigit/"
# path = "/Users/li/Desktop/Captcha/recognition/recogtest/training/"
# count = 0
# for f in os.listdir(dir):
#     if f.endswith(".bmp"):
#         img = Image.open(dir+f)
#         imtools.normalize(img, 32, 32).save(path+f)


# # 图片转化成矩阵
# dir = "/Users/li/Desktop/Captcha/recognition/recogtest/training/"
# path = "/Users/li/Desktop/Captcha/recognition/recogtest/trainingDigits/"
# count = 0
# for f in os.listdir(dir):
#     if f.endswith(".bmp"):
#         [name, type] = f.split(".")
#         img = Image.open(dir+f)
#         # 将图片转化为0,1矩阵
#         a = imtools.im2matrix(img)
#         # 将转化的矩阵保存为txt文件
#         imtools.im2txt(a, path+name)


# # 图片格式转换
# path = "/Users/li/Desktop/Captcha/recognition/recogtest/trainingDigits/"
# str1 = ".bmp"
# imtools.type_rename(path, str1)


# # knn训练
data_set_dir = "/Users/li/Desktop/Captcha/recognition/recogtest/"   # 训练集和预测集所在的目录
pra = THS_REC.kNN.captcha_test(data_set_dir)  # predict data label
print pra
res = []
for i in range(len(pra)):
    res.append(THS_REC.kNN.match(pra[i]))  # predict letter
print res

