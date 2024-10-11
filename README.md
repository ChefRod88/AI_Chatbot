AI Chatbot Web Application
Overview
This project is a simple AI chatbot web application built using Flask for the backend and HTML/CSS/JavaScript for the frontend. The chatbot interacts with users and generates responses using the OpenAI API. This application allows users to ask questions and receive answers in real-time, making it a valuable tool for exploring the capabilities of AI in natural language processing.

Features
User Interaction: Users can type messages into a text area and receive responses from the chatbot.
Dynamic Chat Interface: The chat interface updates dynamically, displaying both user and bot messages.
Typing Indicator: A visual typing indicator shows when the bot is generating a response.
Responsive Design: The application is designed to be user-friendly and responsive on various devices.
Technologies Used
Flask: A lightweight Python web framework used for building the web server and handling HTTP requests.
OpenAI API: Provides AI capabilities to generate responses to user queries.
HTML/CSS: Used for structuring and styling the web application.
JavaScript: Handles user input, sends requests to the server, and updates the chat interface.
Setup Instructions
To run this project locally, follow these steps:

Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Install Dependencies: Make sure you have Python and pip installed. Then install the required packages.

bash
Copy code
pip install flask openai
Set Up OpenAI API Key: Replace 'open_api_key' in the app.py file with your actual OpenAI API key.

Run the Application: Start the Flask server by running:

bash
Copy code
python app.py
Access the Application: Open your web browser and go to http://127.0.0.1:5000 to access the chatbot.

Code Explanation
app.py: This file contains the main Flask application. It sets up routes for serving the HTML page and handling chatbot interactions.

The / route serves the index.html file.
The /chat route handles POST requests to interact with the OpenAI API, sending user messages and returning AI-generated responses.
index.html: The HTML file that defines the structure of the chatbot interface, including styles and JavaScript functionality for sending messages and displaying responses.

Contribution
Contributions are welcome! If you have suggestions for improvements or new features, feel free to submit a pull request or open an issue.
