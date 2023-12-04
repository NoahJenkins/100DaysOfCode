from flask import Flask, render_template, request, send_file
import pyttsx3
import tempfile
import os
import PyPDF2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    # Get the uploaded PDF file
    pdf_file = request.files['pdf']

    # Save the PDF file to a temporary location
    temp_dir = tempfile.mkdtemp()
    pdf_path = os.path.join(temp_dir, 'input.pdf')
    pdf_file.save(pdf_path)

    # Read text content from the PDF file
    text_content = ""
    with open(pdf_path, 'rb') as pdf:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text_content += page.extract_text()

    # Convert the text to audio
    engine = pyttsx3.init()
    output_path = os.path.join(temp_dir, 'output.mp3')
    engine.save_to_file(text_content, output_path)
    engine.runAndWait()

    # Return the converted audio file
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

