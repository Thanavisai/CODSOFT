import re

def chatbot_response(user_input):
    # Convert input to lower case to make the bot case insensitive
    user_input = user_input.lower()
    
    # Define patterns and responses
    responses = [
        (r'hello|hi|hey', "Hello! How can I help you today?"),
        (r'how are you|how\'s it going', "I'm just a bot, but I'm doing great! How about you?"),
        (r'what is your name', "I'm a chatbot created by OpenAI. What's your name?"),
        (r'thank you|thanks', "You're welcome! Anything else I can help with?"),
        (r'bye|goodbye|see you', "Goodbye! Have a great day!"),
        (r'help', "I'm here to assist you. What do you need help with?"),
        (r'what can you do', "I can chat with you and provide information based on predefined rules. Ask me something!"),
        (r'weather', "I can't provide real-time weather updates, but you can check a weather website or app for that information."),
        (r'(\d+)\s*\+\s*(\d+)', lambda match: f"The result is {int(match.group(1)) + int(match.group(2))}."),
        (r'(\d+)\s*-\s*(\d+)', lambda match: f"The result is {int(match.group(1)) - int(match.group(2))}."),
        (r'(\d+)\s*\*\s*(\d+)', lambda match: f"The result is {int(match.group(1)) * int(match.group(2))}."),
        (r'(\d+)\s*\/\s*(\d+)', lambda match: f"The result is {int(match.group(1)) / int(match.group(2))}."),
    ]
    
    # Check each pattern
    for pattern, response in responses:
        match = re.search(pattern, user_input)
        if match:
            if callable(response):
                return response(match)
            return response
    
    # Default response if no pattern matches
    return "I'm sorry, I don't understand that. Can you rephrase?"

# Chat loop to test the chatbot
if __name__ == "__main__":
    print("Welcome to the chatbot! Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye", "see you"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        print("Chatbot:", chatbot_response(user_input))
