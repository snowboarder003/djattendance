""" BADGES util.py 
Utility functions for badges module
"""

from PIL import Image

def _image_upload_path(instance, filename):
  # To customise the path which the image saves to.
  return instance.get_upload_path(filename)

def _image_upload_avatar_path(instance, filename):
  # To customise the path which the image saves to.
  return instance.get_upload_avatar_path(filename)

def resize_image(avatar, size=(200,200)):
    image = Image.open(avatar.path)
    image.resize(size, Image.ANTIALIAS).save(avatar.path, 'JPEG', quality=75)
