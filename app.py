from flask import Flask, render_template, request, send_file
from model import run_style_transfer
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.files['content_image']
        style = request.files['style_image']
        
        content_path = os.path.join(app.config['UPLOAD_FOLDER'], 'content.png')
        style_path = os.path.join(app.config['UPLOAD_FOLDER'], 'style.png')
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.png')

        content.save(content_path)
        style.save(style_path)

        run_style_transfer(content_path, style_path, output_path)

        return render_template('index.html', output_image='output.png')

    return render_template('index.html', output_image=None)

if __name__ == '__main__':
    app.run(debug=True, port=5050)