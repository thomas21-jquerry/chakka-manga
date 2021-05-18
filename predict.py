import tensorflow as tf
import numpy as np
from tensorflow import keras
import os
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Sequential, load_model
import matplotlib.pyplot as plt

model_path = './models/model.h5'
model = load_model(model_path)


def predictImage(filename):
    img1 = image.load_img(filename,target_size=(150,150))
    
    plt.imshow(img1)
 
    Y = image.img_to_array(img1)
    
    X = np.expand_dims(Y,axis=0)
    val = model.predict(X)
    print(val)
    if val == 1:
        
        print("mango")
        
    
    elif val == 0:
        
        print("jackfruit")

predictImage("./test-data/jackf.jpeg")