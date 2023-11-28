from flask import Flask, request, jsonify
# from tensorflow import keras
# from keras import models
# import cv2

# import numpy as np


# classes = ["non-cancer","cancer"]

# my_model= models.load_model("model87.h5")



app = Flask(__name__)
# @app.route('/')
# def home ():
#     return jsonify({'prediction': "ya raaaaaaaab"})


@app.route('/', methods=['GET'])
def get_strings():
    # Replace this list with your actual list of strings
    Bcodes = ["6223001364986", "6223001362975", "6223001365785","6225000332928","62211550","6222020804848","-9599"]
    Patterns = ["622300671", "622114309", "50112","62211550997"]
    manufactures=[]

    return jsonify({
        'Bcodes': Bcodes,
        "Patterns":Patterns, 
        "manufactures":manufactures,
                   })


# @app.route('/',methods=["POST","GET"])
# def index():
#     if request.method=='POST':
#         image_file = request.files['image']
#         image_bytes = image_file.read()
#         image_np = np.frombuffer(image_bytes, np.uint8)
#         image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
#         # Check if the image was loaded successfully
#         if image is None:

#             return 'Failed to load image', 400

#         # Resize the image using cv2.resize()
#         resized_image = cv2.resize(image, (50, 50))
#         normalized_image = resized_image / 255.0
#         input_image = np.expand_dims(normalized_image, axis=0)
#         assert input_image.shape == (1, 50, 50, 3)
#         y = my_model.predict([input_image])
#         y=y.tolist()
#         ind= int(np.argmax(y))
#         pred=classes[ind]
#         if(pred=="cancer"):
#             percentage = (y[0][ind]/ 13) * 100
#             if(percentage>=100):
#                 percentage=float(98.1)
            
#         else:
#             percentage = (y[0][ind]/ 4) * 100
#             if(percentage>=100):
#                 percentage = percentage=float(98.1)
#         return jsonify({'prediction':pred,"percentage":str(round(percentage))})
#     else:
#         return jsonify({'prediction': "upload or use post method to get result"})



if __name__ == '__main__':
    app.run(port=4000, debug=True)