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
    X = vectorizer.transform([user_input])
    proba = model.predict_proba(X)
    confidence = max(proba[0])
    tag = model.classes_[proba.argmax()]

    #  ADD THIS BLOCK HERE
    if confidence < 0.4:
        return (
            "I'm not fully confident about this. Could you rephrase or be more specific?",
            confidence
        )

    # Find response
    for intent in intents['intents']:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response, confidence

    return "Sorry, I didn't understand that.", 0.0

# Test chatbot in terminal
if __name__ == "__main__":
    print("Job Assistance Chatbot is running! (type 'quit' to exit)")
    while True:
        msg = input("You: ")
        if msg.lower() == "quit":
            break
        print("Bot:", get_response(msg))
