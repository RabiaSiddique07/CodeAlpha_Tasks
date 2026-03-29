def get_response(user_input):
    """This function takes user input and returns a reply."""
    
    user_input = user_input.lower()

    if user_input == "hello" or user_input == "hi" or user_input == "hye":
        return "Hi there! How can I help you?"

    elif user_input == "how are you":
        return "I'm doing great, thanks for asking!"

    elif user_input == "what is your name":
        return "I'm ChatBot, your simple Python assistant!"

    elif user_input == "what can you do":
        return "I can chat with you! Try: hello, how are you, bye"

    elif user_input == "bye" or user_input == "goodbye":
        return "Goodbye! Have a great day!"

    elif user_input == "thanks" or user_input == "thank you":
        return "You're welcome!"

    else:
        return "Hmm, I didn't understand that. Try: hello, how are you, bye"


# -------------------------------------------------------
print("ChatBot is ready! Type 'bye' to exit.\n")

while True:
    user_message = input("You: ") 

    response = get_response(user_message)
    print("Bot:", response, "\n") 

    if user_message.lower() == "bye" or user_message.lower() == "goodbye":
        break
