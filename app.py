
import cv2

import numpy as np
from flask import Flask, request, jsonify
from tensorflow import keras
from keras import models


app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def index():
    return jsonify({'prediction': "ya raaaaaaaab"})



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)