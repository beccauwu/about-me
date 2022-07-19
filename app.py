from flask import Flask, render_template
from flask_fontawesome import FontAwesome
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')
fa = FontAwesome(app)

@app.route('/')
def index():
    driver.get('https://docs.google.com/document/d/1SmTpbQXWuH8WP5YeyxyPHx5i51952ffgvUU8ZuT30_I/export?format=pdf&embedded=true')
    driver.sleep(2)
    driver.get_screenshot_as_file('web/static/img/resume_screenshot.png')
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
