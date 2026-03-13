import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import tensorflow as tf

img_size = 224

model = load_model("best_moodpet_model.h5")
class_indices = np.load("class_names.npy", allow_pickle=True).item()
CLASSES = list(class_indices.keys())

def getclass(image_path: str):
    try:
        img = Image.open(image_path).convert("RGB")
        img = img.resize((img_size, img_size))
        arr = np.asarray(img).astype("float32")
        arr = tf.keras.applications.mobilenet_v2.preprocess_input(arr)
        arr = np.expand_dims(arr, axis=0)

        if isinstance(model.input_shape, list) and len(model.input_shape) == 2:
            preds = model.predict([arr, arr], verbose=0)[0]
        else:
            preds = model.predict(arr, verbose=0)[0]

        idx = np.argmax(preds)
        clase = CLASSES[idx]
        conf = preds[idx]

        return clase, conf

    except Exception as e:
        return f"error en prediccion: {str(e)}"