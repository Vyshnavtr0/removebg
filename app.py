from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_background():
    # Check if the request contains a file
    if 'file' not in request.files:
        return {"error": "No file provided"}, 400
    
    file = request.files['file']

    if file.filename == '':
        return {"error": "No file selected"}, 400

    # Read the image file
    input_image = Image.open(file.stream)
    
    # Remove the background
    output_image = remove(input_image)

    # Create a BytesIO object to save the image in memory
    img_byte_arr = io.BytesIO()
    output_image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    # Send the processed image back to the client
    return send_file(img_byte_arr, mimetype='image/png', as_attachment=True, download_name='output.png')

if __name__ == '__main__':
    app.run(debug=True)