from flask import Flask, render_template, request
import base64
import os
from datetime import datetime
from recognize_barcode_api import a
import recognize_barcode_api
app = Flask(__name__)

SAVE_DIR = 'captured_images'
os.makedirs(SAVE_DIR, exist_ok=True)

# print(os.path.abspath("captured_images"))
print(a)
@app.route('/')
def index():
    print(print(os.getcwd()))
    #my_number=353553534534535
    return render_template('index2.html',my_number=a.raw_text)

@app.route('/capture', methods=['POST'])
def capture():
    image_data = request.form['image']
    header, encoded = image_data.split(",", 1)
    binary_data = base64.b64decode(encoded)

    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
    filepath = os.path.join(SAVE_DIR, filename)

    with open(filepath, "wb") as f:
        f.write(binary_data)
    return "Image saved as " + filename








if __name__ == '__main__':
    app.run(debug=True)
