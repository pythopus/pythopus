from flask import Flask, jsonify, render_template

app = Flask(__name__)
CORS(app) # Enable CORS for all domains on all routes

@app.route('/')
def index():
    return 'Pythopus Backend API!'

@app.route('/')
def html_endpoint():
    return render_template('index.html')

@app.route('/api')
def json_endpoint():
    data = {'message': 'Pythopus Backend API!'}
    return jsonify(data)

@app.route('/api/command', methods=['POST'])
def command():
    # Extract data from the request
    data = request.get_json()
    commands = data.get('commands')

    if not commands:
        for command in commands:
            print(command['name'])
    return jsonify({'error': 'No prompt provided'}), 400

    response = {
        'response': 'This is a dummy response. Commands: ' + ', '.join(commands),
    }

    return jsonify(response)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK'}), 200

if __name__ == '__main__':
    app.run(debug=True)