#from flask import Flask , request , render_template ,url_for,jsonify
import cv2
#import base64
#from PIL import Image
# import io
import numpy as np
from flask import Flask, request, jsonify
from tensorflow import keras
from keras import models


app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def index():
    classes = ["non-cancer","cancer"]
    my_model= models.load_model("model87.h5")
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
        # y = my_model.predict([input_image])
        y=[0.4,3.5]
        #y=y.tolist()
        ind= np.argmax(y)
        y=classes[ind]
        return jsonify({'prediction': "cancer"})
    else:
        return jsonify({'prediction': "ya raaaaaaaab"})



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)