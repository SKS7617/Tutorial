from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', section='home')

@app.route('/about')
def about():
    return render_template('index.html', section='about')

@app.route('/contact')
def contact():
    return render_template('index.html', section='contact')

@app.route('/image-perferation')
def image_perferation():
    return render_template('image_perferation.html')

@app.route('/image-enhancer')
def image_enhancer():
    return render_template('image_enhancer.html')

@app.route('/image-to-lines')
def image_to_lines():
    return render_template('image_to_lines.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

