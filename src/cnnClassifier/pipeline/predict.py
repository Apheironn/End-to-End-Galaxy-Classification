import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras import backend as K
import os
import json

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model
        K.clear_session()
        model = load_model(os.path.join("artifacts", "training", "best_model.h5"))

        class_labels = ['Cigar-shaped smooth', 'In between smooth', 'completely round smooth', 'edge-on', 'spiral']

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        predictions = model.predict(test_image)
        predicted_class_index = np.argmax(predictions)
        predicted_class_label = class_labels[predicted_class_index]

        print("Predicted class:", predicted_class_label)

        # Create a dictionary containing the prediction information
        prediction_result = {
            "predicted_class": predicted_class_label
        }

        return [prediction_result]
