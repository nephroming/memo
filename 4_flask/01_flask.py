from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test')
def test():
    return '같은 화면'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
