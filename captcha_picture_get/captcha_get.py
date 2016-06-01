#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib2


def captcha_get(url_path, name, target_path):
    """
    Args:
        url_path: captcha address
        name: captcha name saved
        target_path: captcha path saved
    """
    content = urllib2.urlopen(url_path).read()
    try:
        with open(target_path+r"%s.bmp" % name, "wb") as file:
            file.write(content)
    except Exception, e:
        print "The Exception: ", Exception, ":", e


if __name__ == '__main__':

    #  同花顺验证码地址
    TongHuaShun_captcha_url = "http://captcha.10jqka.com.cn/build?token=21cfd9bcd4f65a74980d37b7f1f08fae&appid=" \
                  "login&sessionid=nasjatgjct7v4dj41ugo7m3p41&14631216628401"

    #  微博验证码地址
    WeiBo_captcha_get = "http://login.sina.com.cn/cgi/pin.php?r=76634618&s=0&p=gz-f14e3d626443a2c6add10cc8f438852dd5b1"

    # 同花顺验证码保存地址
    target_path_THS = "/Users/li/Desktop/Captcha/recognition/captcha_picture_get/tonghuashun/"

    # 微博验证码保存地址
    target_path_WB = "/Users/li/Desktop/Captcha/recognition/captcha_picture_get/weibo/"

    for i in range(50000):
        captcha_get(TongHuaShun_captcha_url, i, target_path_THS)
        captcha_get(WeiBo_captcha_get, i, target_path_WB)