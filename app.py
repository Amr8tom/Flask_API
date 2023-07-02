from flask import Flask, request, jsonify
from tensorflow import keras
from keras import models



import cv2


import numpy as np

app = Flask(__name__)

# @app.route('/')
# def home ():
#     return jsonify({'prediction': "ya raaaaaaaab"})

classes = ["non-cancer","cancer"]
my_model= models.load_model("model87.h5")

@app.route('/',methods=["POST","GET"])
def index():
    if request.method=='POST':
        image_file = request.files['image']
        image_bytes = image_file.read()
        image_np = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        # Check if the image was loaded successfully
        if image is None:
            return 'Failed to load image', 400
        
        # Resize the image using cv2.resize()
        resized_image = cv2.resize(image, (50, 50))
        normalized_image = resized_image / 255.0
        input_image = np.expand_dims(normalized_image, axis=0)
        assert input_image.shape == (1, 50, 50, 3)
        y = my_model.predict([input_image])
        y=y.tolist()
        ind= np.argmax(y)
        y=classes[ind]
        return jsonify({'prediction':y})
    else:
        return jsonify({'prediction': "ya raaaaaaaab"})



if __name__ == '__main__':
    app.run(port=4000, debug=True)