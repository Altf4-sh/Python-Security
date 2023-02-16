#!/usr/bin/env python

from PIL import Image
from PIL.ExifTags import TAGS

print(Image.open('images/image.jpg')._getexif())

for (key,value) in Image.open('images/image.jpg')._getexif().items():
        print('%s = %s' % (TAGS.get(key), value))
