# (if you have any helper functions – e.g., file listing, metrics logging etc.)
import os

def list_images(directory, extensions=('png','jpg','jpeg','bmp')):
    return [os.path.join(directory, f)
            for f in os.listdir(directory)
            if f.lower().endswith(extensions)]

