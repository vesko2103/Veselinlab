from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = {
        'response': f'You said: {user_input}'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
