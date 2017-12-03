import time

#import cv2
import numpy as np
import pandas as pd
from scipy import misc

def convert_images_to_arrays(file_path, df):
    

    lst_imgs = [l for l in df['Image_Index']]

    return np.array([np.array(misc.imread(file_path + img)) for img in lst_imgs])


def save_to_array(arr_name, arr_object):
   
    return np.save(arr_name, arr_object)


if __name__ == '__main__':
    start_time = time.time()

    labels = pd.read_csv("/home/chik/Downloads/images/newcsv.csv")

    print("Creating Training Array")
    X_train = convert_images_to_arrays('/home/chik/Downloads/images/newimages/', labels)

    print(X_train.shape)

    print("Saving Train Array")
    save_to_array('/home/chik/Downloads/images/X_sample.npy', X_train)

    print("Time taken(sec): ", round(time.time() - start_time), 2)