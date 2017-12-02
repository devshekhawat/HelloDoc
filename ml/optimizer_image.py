


import os
import time
import numpy as np
from PIL import Image
from scipy import misc


def create_directory(directory):
    
    if not os.path.exists(directory):
        os.makedirs(directory)


def crop_and_resize_images(path, new_path, img_size):
 
    create_directory(new_path)
    dirs = [l for l in os.listdir(path) if l != '.DS_Store']

    for item in dirs:
        img = Image.open(path+item).convert('L')
        #img = img.convert('L')
        img = img.resize((img_size, img_size))
        misc.imsave(str(new_path + item), img)


if __name__ == '__main__':
    start_time = time.time()
    crop_and_resize_images(path='/home/chik/Downloads/images/images/', new_path='/home/chik/Downloads/images/newimages/', img_size=255)
    print("Time taken(sec): ", time.time() - start_time)