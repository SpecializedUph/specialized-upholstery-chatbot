from flask import Flask, request, jsonify
import os
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from Wix site

# Load API Key from Environment Variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("ERROR: OPENAI_API_KEY is not being read from environment variables!")

client = openai.OpenAI(api_key=OPENAI_API_KEY)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        user_message = request.json.get("message", "")
        
        if not user_message:
            return jsonify({"error": "No message provided"}), 400
        
        # Send user input to OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful chatbot for Specialized Upholstery."},
                {"role": "user", "content": user_message}
            ]
        )
        
        bot_response = response.choices[0].message.content.strip()
        return jsonify({"response": bot_response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
