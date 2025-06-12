from flask import Flask, request, jsonify
from models import query_model

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get("prompt")
    # Use fixed model for now
    model = "mistralai/Mistral-7B-Instruct-v0.3"

    response = query_model(prompt, model)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
