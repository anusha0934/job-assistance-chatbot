import json
import pickle
import random

# Load trained model and vectorizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Load intents
with open('data/intents.json') as file:
    intents = json.load(file)

def get_response(user_input):
    # Convert user input to vector
    X = vectorizer.transform([user_input])
    tag = model.predict(X)[0]

    # Find response
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

    return "Sorry, I didn't understand that."

# Test chatbot in terminal
if __name__ == "__main__":
    print("Job Assistance Chatbot is running! (type 'quit' to exit)")
    while True:
        msg = input("You: ")
        if msg.lower() == "quit":
            break
        print("Bot:", get_response(msg))