from transformers import pipeline

# Carga el modelo y el tokenizer entrenados
model_path = './results'
qa_pipeline = pipeline('question-answering', model=model_path, tokenizer=model_path)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = qa_pipeline({'question': user_input, 'context': 'Aquí puedes proporcionar un contexto si es necesario'})
    answer = response['answer']
    save_interaction(user_input, answer)
    return jsonify({'response': answer})
