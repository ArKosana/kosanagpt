from flask import Flask, request, jsonify, render_template
from models import query_model

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        prompt = data.get("prompt", "")
        if not prompt:
            return jsonify({"response": "Prompt is required."}), 400

        result = query_model(prompt, "mistralai/Mistral-7B-Instruct-v0.3")
        return jsonify({"response": result})

    except Exception as e:
        return jsonify({"response": f"Exception: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
