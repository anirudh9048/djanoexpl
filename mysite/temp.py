import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


def machine_learning():
    input = [[0.1, 0.2, 0.05, 0.6], [0.3, -0.3, 0.4, -0.2]] # first half of the song
    output = [[0.2,0.4,0.2,0.445], [0.1, -0.56, 0.5, -0.1]] # second half of the song

    model = tf.keras.models.Sequential([
        layers.Dense(15, input_dim=len(input), activation="relu", name="layer1"),
    ])


    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    model.fit(input, output, epochs=5)

    print("-------")
    print(model.predict([1,-1,1,-1,1,0]))



machine_learning()
