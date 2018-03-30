#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# pip install Pillow
from PIL import Image
import io

img = Image.open("input.jpg")
bytes_io = io.BytesIO()
img.save(bytes_io, format='JPEG')
img_data = bytes_io.getvalue()
print(len(img_data), img_data)
