from flask import Flask, render_template, request
from PIL import Image
import io

app = Flask(__name__)

def extract_colors(image, num_colors):
    # Resize image for faster processing if needed
    max_size = (100, 100)
    image.thumbnail(max_size)

    # Convert image to RGB mode (in case it's not in RGB)
    image = image.convert('RGB')

    # Get colors using the Pillow library
    color_palette = image.getcolors(num_colors)
    if color_palette is None:
        return []
    
    # Extract RGB values from the palette
    extracted_colors = [color[1] for color in color_palette]

    return extracted_colors

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    image = Image.open(io.BytesIO(file.read()))

    # Extract 6 dominant colors from the image
    num_colors = 6
    palette = extract_colors(image, num_colors)

    return render_template('result.html', palette=palette)


if __name__ == '__main__':
    app.run(debug=True)
