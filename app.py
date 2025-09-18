from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    api_key = data.get("api_key")
    user_message = data.get("message")

    if not api_key:
        return jsonify({"error": "API key required"}), 400

    try:
        # Configure Gemini API with user’s key
        genai.configure(api_key=api_key)

        # Use the latest working model
        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
