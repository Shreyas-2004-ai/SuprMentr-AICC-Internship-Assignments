# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"

    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great 😄"

    elif "your name" in user_input:
        return "I am a simple NLP chatbot."

    elif "bye" in user_input:
        return "Goodbye! Have a nice day 👋"

    elif "help" in user_input:
        return "You can ask me basic questions like greetings, name, etc."

    else:
        return "Sorry, I didn't understand that."

# Chat loop
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ")

    response = chatbot_response(user)
    print("Chatbot:", response)

    if "bye" in user.lower():
        break