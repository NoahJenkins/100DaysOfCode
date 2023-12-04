from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

# Function to add watermark to the image
def add_watermark(input_image_path, output_image_path, watermark_text):
    original_image = Image.open(input_image_path)
    width, height = original_image.size

    # Creating a drawing context
    drawing = ImageDraw.Draw(original_image)

    # Define font and position for watermark
    font = ImageFont.load_default()
    text_width, text_height = drawing.textsize(watermark_text, font)
    text_position = ((width - text_width) // 2, (height - text_height) // 2)

    # Adding the watermark text to the image
    drawing.text(text_position, watermark_text, fill="white", font=font)

    # Save the image with watermark
    original_image.save(output_image_path)

# Route to handle file upload and display the form
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file:
            # Save the uploaded file
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)

            # Watermark text
            watermark_text = "Your Watermark Text"

            # Create a unique filename for the watermarked image
            output_file_path = os.path.join('uploads', 'watermarked_' + file.filename)

            # Add watermark to the uploaded image
            add_watermark(file_path, output_file_path, watermark_text)

            return render_template('result.html', original_image=file.filename, watermarked_image='watermarked_' + file.filename)

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)

