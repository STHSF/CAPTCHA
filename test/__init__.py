#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from captchaRecognition import *
from PIL import Image


image_name = "21.jpg"
a = captcharecognition()
txt = a.recognition(image_name)
print txt