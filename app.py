from flask import Flask , request , render_template ,url_for,jsonify
import base64
from PIL import Image
import io
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
from flask import Flask, request, jsonify
from tensorflow import keras
import numpy as np
from PIL import Image
import cv2
import numpy as np
#print("ya raaaaaaaaab")
#print(tf.__version__)
# app=Flask(__name__)


classes = ["non-cancer","cancer"]
# @app.route('/predict', methods=["POST"])
# def predict():
#      #imagefile key in flutter json map
#      if 'imagefile' in request.files:
#         imagefile = request.files['imagefile']
#         # Further processing of the uploaded image
#         # ...

#         print ("Image file received and processed successfully.")
#      else:
#         return "No image file found in the request." 
#      print("GsdGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
#      print(imagefile)
#      print("GsdGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
#      #image_path = "D:/opaodp" + imagefile.filename
#      #imagefile.save(image_path)
#      # image_bytes = base64.b64decode(imagefile)
#      # image = Image.open(io.BytesIO(image_bytes))
#      image_bytes = imagefile.read()
#      image  = base64.b64encode(image_bytes).decode('utf-8')
#      image = preprossing(image)
#      y = my_model.predict([image])
#      return jsonify({'prediction': y})




# @app.route('/', methods=["POST"])
# def gogo():
    # my_model= load_model("model87.h5")
    # image_file = request.files['image']
    # image_bytes = image_file.read()
    # image_np = np.frombuffer(image_bytes, np.uint8)
    # image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    # # Check if the image was loaded successfully
    # if image is None:
    #     return 'Failed to load image', 400
    
    # # Resize the image using cv2.resize()
    # resized_image = cv2.resize(image, (50, 50))
    # normalized_image = resized_image / 255.0
    # input_image = np.expand_dims(normalized_image, axis=0)
    # assert input_image.shape == (1, 50, 50, 3)
    # y = my_model.predict([input_image])
    # y=y.tolist()
    # ind= np.argmax(y)
    # y=classes[ind]
    # return jsonify({'prediction': y})
    # return "Ya raaaaaaaaaaaaaaaaab"



# def predict():
#      print("run cooode")
#      if request.method=="GET":
#           print ("Trying load image correctly")
#           image = request.files["fileup"]
#           print ("loaded image correctly")
#           image = preprossing(image)
#           print("image is preprossed correctly")
#           result=[my_model.predict(image)]
#           ind = np.argmax(result)
#           final_output_prediction= classes[ind]
#           print("the model worked well ")
     
#      return "dsadasdas"
# if __name__=='__main__':
#     app.run(host="0.0.0.0",port=5000)
    #app.run(debug=True)


# @app.route('/',methods=['get','post'])
# def home():
#      if request.method=='post':
#           img=request.files['upimage']
#           img.save('D:/DMC Project/github/flask/IMG/upimage.jpg')
#           image_url = '/static/upimage.jpg'

#      return render_template("index.html",imagee=image_url)

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def index():
     
     if request.method=='post':
        my_model= load_model("model87.h5")
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
        return jsonify({'prediction': y})
     else:
         return "ya raaaaaaab"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)