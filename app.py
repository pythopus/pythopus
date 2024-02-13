from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Pytopus!'

@app.route('/')
def html_endpoint():
    return render_template('index.html')

@app.route('/api')
def json_endpoint():
    data = {'message': 'Hello, Pytopus!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run()