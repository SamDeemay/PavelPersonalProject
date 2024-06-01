import openai
from flask import Flask, Response, request
from flask_cors import CORS

# Configuration for OpenAI API
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "not-needed"

# Function to create a chat completion with a dynamic user prompt and handle streaming
def create_chat_completion(user_input, system_message):
    response = openai.ChatCompletion.create(
        model="local-model",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        stream=True  # Enable streaming
    )
    return response

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    user_input = data.get('prompt', '')
    system_message = (
        "The following is a conversation with Pavel, an AI mental health assistant. "
        "Pavel is designed to provide compassionate support to individuals struggling with mental health issues."
        "Pavel listens attentively and responds with empathy and understanding. "
        "Pavel respects user privacy and maintains confidentiality in all interactions."
        "Pavel offers personalized recommendations and resources tailored to users' unique needs."
        "Pavel encourages users to engage in self-care practices and seek professional help when needed. "
    )

    # Create chat completion with streaming
    response = create_chat_completion(user_input, system_message)

    def stream_response():
        for chunk in response:
            if 'choices' in chunk and len(chunk['choices']) > 0:
                content = chunk['choices'][0]['delta'].get('content', '')
                yield f"data: {content}\n\n"

    return Response(stream_response(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)
