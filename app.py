from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set OpenAI API key
openai.api_key = 'open_api_key'


# Route to serve the HTML file
@app.route('/')
def index():
    return render_template('index.html')


# Route to handle the chatbot interaction
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']  # Get the message from the request

    # Use the OpenAI API to get a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the updated model, e.g., gpt-4 if needed
        messages=[{"role": "user", "content": user_input}],  # Set the role and content
        max_tokens=150
    )

    # Extract the chatbot response
    chatbot_response = response['choices'][0]['message']['content'].strip()

    return jsonify({'message': chatbot_response})  # Return response as JSON


if __name__ == '__main__':
    app.run(debug=True)




