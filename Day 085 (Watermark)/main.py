from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from tkinter import Tk, filedialog
from PIL import Image, ImageTk
import io
import base64

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'

def add_watermark(input_image, watermark_text):
    # Open the image using PIL
    image = Image.open(input_image)

    # Add a text watermark using PIL
    watermark = Image.new('RGBA', image.size, (255, 255, 255, 0))
    watermark_text_draw = ImageDraw.Draw(watermark)
    watermark_text_draw.text((10, 10), watermark_text, fill=(255, 255, 255, 128))

    # Combine the image with the watermark
    watermarked_image = Image.alpha_composite(image.convert('RGBA'), watermark)

    return watermarked_image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            filename = secure_filename(file.filename)
            file.save(app.config['UPLOAD_FOLDER'] + filename)
            return redirect(url_for('process', filename=filename))

@app.route('/process/<filename>')
def process(filename):
    root = Tk()
    root.withdraw()
    filepath = app.config['UPLOAD_FOLDER'] + filename

    watermark_text = filedialog.askstring("Watermark", "Enter watermark text:")

    watermarked_image = add_watermark(filepath, watermark_text)

    buffered = io.BytesIO()
    watermarked_image.save(buffered, format='PNG')
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return render_template('result.html', image=img_str)

if __name__ == '__main__':
    app.run(debug=True)
