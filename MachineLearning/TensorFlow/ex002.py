from tensorflow import keras
model = keras.models.load_model('./')

model.summary()