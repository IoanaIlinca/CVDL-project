import tensorflow as tf
import numpy as np

from tensorflow.keras import layers, models

def create_model(height: int = 8, width: int = 8) -> models:
	main_input_layer = layers.Input(shape = (height, width, 10))
	secondary_input_layer = layers.Input(shape = (height, width, 1))

	first_convolutional_layer = layers.Conv2D(64, (3,3), padding = "same", activation = "relu")(main_input_layer)
	second_convolutional_layer = layers.Conv2D(64, (3,3), padding = "same", activation = "relu")(first_convolutional_layer)
	third_convolutional_layer = layers.Conv2D(64, (3,3), padding = "same", activation = "relu")(second_convolutional_layer)
	fourth_convolutional_layer = layers.Conv2D(64, (3,3), padding = "same", activation = "relu")(third_convolutional_layer)
	fifth_convolutional_layer = layers.Conv2D(64, (3,3), padding = "same", activation = "relu")(fourth_convolutional_layer)
	sixth_convolutional_layer = layers.Conv2D(1, (1,1), padding = "same", activation = "sigmoid")(fifth_convolutional_layer)

	output_layer = layers.multiply([sixth_convolutional_layer, secondary_input_layer])
	model = models.Model(inputs = [main_input_layer, secondary_input_layer], outputs = output_layer)
	model.compile(optimizer = "adam", loss = "binary_crossentropy", metrics = ["accuracy"])

	model.summary()
	return model