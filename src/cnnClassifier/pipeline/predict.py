import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts","training", "best_model.h5"))


        class_labels = ['Cigar-shaped smooth',   'In between smooth','completely round smooth','edge-on', 'spiral']

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        predictions = model.predict(test_image)
        predicted_class_index = np.argmax(predictions)
        predicted_class_label = class_labels[predicted_class_index]

        print("Predicted class:", predicted_class_label)
        print("Prediction probabilities:", predictions)

        return "Predicted class:", predicted_class_label, "\nPrediction probabilities:", predictions