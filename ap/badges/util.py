""" BADGES util.py 

Utility functions for badges module
"""

def _image_upload_path(instance, filename):
  # To customise the path which the image saves to.
  return instance.get_upload_path(filename)

# def assign_trainee_badges():