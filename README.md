# chakka-manga
Tinkerhub project

## Team Id: BFH/recNQ9o2hmUaS6MeB/2021

## Team Members
+ Fayaz Azeem P
+ Nandhagopal  C S
+ Thomas Jose

website: https://chakka-manga-classifier.herokuapp.com/

# Binary image Classification as mango or jackfruit

## Overview
This is a simple image classification web application, using both Streamlit and Tensorflow keras to classify images as either mango or jackfruit

## Dataset
The dataset used to create the model: www.kaggle.com/d()ataset/2a36453721a41dc1d7030ad9bf70a938644844ed65346ffd5cd03c9a0a352b70
  
## Model
#### Contains the whole process of building the CNN Model 
- import libraries
- Preprocess the images using OpenCV.
- Use ImageDataGenerator for image augmentation and help the model generalise it's results.
- keras.sequential() is used with 7 layers
- We now create a model checkpoint and then fit the model and run it for 10 epochs.
- Now Load the model's weights and biases and evaluate it on our test dataset.
- Save our model in Keras HDF5 format.
- Use the saved model to test on random images.
  
## Installation
- Clone the repository
```bash
git clone https://github.com/Fayazazeemp/chakka-manga-classifier.git
```
- Install the requirements
```bash
pip install -r requirements.txt
```
- Run the app
```bash
streamlit run app.py
```

