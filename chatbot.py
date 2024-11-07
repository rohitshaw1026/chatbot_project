from flask import Flask, render_template, request
import random

app = Flask(__name__)

def greet():
    greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!", "Howdy!"]
    return random.choice(greetings)

def small_talk(query):
    responses = {
        "how are you": "I'm doing great, thanks for asking!",
        "what is your name": "My name is ChatBot 3000.",
        "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    }
    return responses.get(query.lower(), "Sorry, I didn't understand that.")

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input.lower() == "exit":
            return "Goodbye! It was nice chatting with you."
        response = small_talk(user_input)
        return response
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(debug=True)
