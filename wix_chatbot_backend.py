from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from Wix site

# Set your OpenAI API key here
OPENAI_API_KEY = "your_openai_api_key"
openai.api_key = OPENAI_API_KEY

@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        user_message = request.json.get("message", "")

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Send user input to OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a helpful chatbot for Specialized Upholstery."},
                      {"role": "user", "content": user_message}]
        )

        bot_response = response["choices"][0]["message"]["content"].strip()
        return jsonify({"response": bot_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
