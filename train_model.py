#importing essential modules for the project
import numpy as np
import tensorflow as tf
from tensorflow import keras

#loading data from the mnist dataset using keras into defined variables using tuple unpacking 

(x_train,y_train),(x_test,y_test) = keras.datasets.mnist.load_data()

#normalizing given input data for training the model as well as for testing the model
#dividing each of the pixel value with 255, to cast the value within the range [0,1]
#this makes the learning process for the neural network easier
#we use array broadcasting as a shorthand way to do normalization
x_train = x_train/255
x_test = x_test/255

model = keras.Sequential([keras.layers.Flatten(input_shape=(28,28)), keras.layers.Dense(128, activation='relu'), keras.layers.Dropout(0.2),keras.layers.Dense(10, activation = 'softmax')])
#This creates a sequence of layers that the data corresponding to a training image would go through
#The first layer flats the given array of shape (28,28) into a 784 element list or 1D array, which is processed by the model 
#Then the dense layer sends all of the 784 pixels data to each of the 128 neurons in the layer
#Each neuron acts as a computational unit which computes weights corresponding to pixel data by which it learns
#The activation set up as relu implies rectified linear unit, giving output as relu(x) = max(0,x), that is it gives x if it is positive, and 0 otherwise, used for pattern recognition, like curves, edges, etc.
#Then the image's data passes through the dropout layer with value 0.2, implying during each time an image is given as input for training, 20% of the nerons will be switched off or deactivated
#this is done in order to make sure over-fitting is not occuring, where one of the neurons or a select group learn the image too well, not providing other neurons to learn general patterns
#this results in the model not being able to predict accurately when provided with a different test image.
#Finally comes the dense layer which has 10 neurons as there are 10 possible digits as output.
#the raw values are converted into probabilities for each of the 10 digits and they all add up to 1.0, this is done by softmax
#the higher the probability value the higher the confidence the model shows for that particular output.

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#using the optimizer adam, the optimizer would change the value of weights in the neurons corresponding the pixel data after comparing the prediction with the actual answer, upon measuring loss using crossentropy -log(probability value given by the model for the correct answer)
#then using back propogation the optimizer would change the weights little by little with the aim being to reduce loss as much as possible.
#we use sparse since our labels are just integers and not hot-encoded using arrays, and we categorical since our ouputs can be between 0-9 hence categorical.


print("\n Training the model!")

#training the model
model.fit(x_train,y_train,epochs = 5, validation_data=(x_test, y_test))

#testing the model
test_loss, test_accuracy = model.evaluate(x_test,y_test,verbose = 2)
print(f"\n Final test accuracy: {test_accuracy * 100:.2f}%")

#saving the model
model.save('digit_recognizer_model.keras')
print("\n Model saved as digit_recognizer_model.keras")


