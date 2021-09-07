from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return 'Blog Page'

@app.route('/greeting/<name>')
def greeting(name):
    return render_template('page.html', name='Orion')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')