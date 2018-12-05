import tensorflow as tf
from tensorflow.keras import layers

"""Testing some Keras"""

def main():
    print(tf.VERSION)
    print(tf.keras.__version__)


    model = tf.keras.Sequential()
    # Adds a densely-connected layer with 64 units to the model:
    b = model.add(layers.Dense(64, activation='relu'))
    # Add another:
    model.add(layers.Dense(64, activation='relu'))
    # Add a softmax layer with 10 output units:
    model.add(layers.Dense(10, activation='softmax'))

    print(type(model))
    print(type(b))
    
    

if __name__ == '__main__':
    main()

#fashion_mnist = keras.datasets.fashion_mnist
#(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
