from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Configura tu API key de OpenAI
openai.api_key = 'tu-API-key'

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=150
    )
    answer = response.choices[0].text.strip()
    save_interaction(user_input, answer)
    return jsonify({'response': answer})

def save_interaction(question, answer):
    # Aquí es donde guardarás las interacciones en la base de datos
    # Por simplicidad, estamos imprimiendo las interacciones
    print(f"Pregunta: {question}\nRespuesta: {answer}")

if __name__ == '__main__':
    app.run(debug=True)

