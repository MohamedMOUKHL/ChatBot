from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple rule-based responses
responses = {
    "hello": "Hi there!",
    "how are you": "I'm doing well, thank you!",
    "bye": "Goodbye! Have a great day!",
    # Add more keywords and responses as needed
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.form["user_message"].lower()  # Convert to lowercase for case-insensitive matching

    # Check if any keyword is present in the user's message
    for keyword, response in responses.items():
        if keyword in user_message:
            bot_response = response
            break
    else:
        # If no keyword is found, provide a default response
        bot_response = "I'm sorry, I didn't understand that."

    return jsonify({"bot_response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
