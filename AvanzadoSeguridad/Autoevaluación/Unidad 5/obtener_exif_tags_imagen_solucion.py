#!/usr/bin/env python

from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_tags(path_image):
    resultado = {}
    image = Image.open(path_image)
    if hasattr(image, '_getexif'):
        info = image._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag,tag)
            resultado[decoded] = value
    return resultado

tags = get_exif_tags('image.jpg')

for (key,value) in tags.items():
        print('%s = %s' % (key,value))

