from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/image_perferation')
def image_perferation():
    return render_template('image_perferation.html')

@app.route('/image_enhancer')
def image_enhancer():
    return render_template('image_enhancer.html')

@app.route('/image_to_lines')
def image_to_lines():
    return render_template('image_to_lines.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

