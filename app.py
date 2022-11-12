from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
@app.route('/index')
def index():
    return 'index'


@app.route('/contact/')
def contact():
    return 'contact information'


@app.route('/calculate/7/9/')
def calculate():
    return str(7 ** 9)


@app.route('/albums/1')
def hello_world():
    return 'Hello, Flask'


@app.route('/albums/<album_number>')
def albums(album_number):
    return 'The {} album.'.format(album_number)

# if __name__ == "__main__":
#     app.run(host='127..0.0.1', port=5000)
