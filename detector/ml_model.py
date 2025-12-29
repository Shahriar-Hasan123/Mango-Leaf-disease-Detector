import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

MODEL_PATH = "mango_leaf_disease_model.h5"
IMG_SIZE = (224, 224)

CLASS_NAMES = [
    "Anthracnose",
    "Bacterial_Canker",
    "Cutting_Weevil",
    "Die_Back",
    "Gall_Midge",
    "Healthy",
    "Powdery_Mildew",
    "Sooty_Mould"
]

model = tf.keras.models.load_model(MODEL_PATH)

def predict_image(img_path):
    img = image.load_img(img_path, target_size=IMG_SIZE)
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)
    index = np.argmax(preds)
    confidence = float(preds[0][index])

    return CLASS_NAMES[index], confidence
