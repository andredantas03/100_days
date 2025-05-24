from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
@make_bold
def hello():
    return 'Hello, World'

@app.route('/bye')
def bye():
    return 'Bye!'

if __name__ == '__main__':
    app.run(debug=True)