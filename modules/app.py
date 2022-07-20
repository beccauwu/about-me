from flask import Flask, render_template
from flask_fontawesome import FontAwesome
app = Flask(__name__,
            static_url_path='',
            static_folder='../web/static',
            template_folder='../web/templates')
fa = FontAwesome(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact-form/')
def about():
    return render_template('about.html')

@app.route('/contact-me/')
def contact():
    return render_template('contact.html')

@app.route('/resume/')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(port=5000)
