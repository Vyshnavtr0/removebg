from flask import Flask, request, jsonify, send_file
from rembg import remove
from io import BytesIO
from PIL import Image
import os
app = Flask(__name__)

@app.route('/')
def index():
    return "Background Removal API is running"

# @app.route('/remove-bg', methods=['POST'])
# def remove_bg():
#     if 'image' not in request.files:
#         return jsonify({"error": "No image file provided"}), 400
    
#     image_file = request.files['image']
#     img = Image.open(image_file.stream)

#     # Remove background
#     img_no_bg = remove(img)

#     # Save output to BytesIO
#     img_io = BytesIO()
#     img_no_bg.save(img_io, 'PNG')
#     img_io.seek(0)

#     return send_file(img_io, mimetype='image/png')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))  # Use PORT from the environment, fallback to 5000
    app.run(host='0.0.0.0', port=port)