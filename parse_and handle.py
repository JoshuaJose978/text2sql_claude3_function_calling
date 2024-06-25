import re

# Define command handlers
def handle_help():
    return "Available commands: /help, /cc <country>, /weather <location>"

def handle_cc(country):
    # Dummy implementation, replace with actual logic to fetch country code
    country_codes = {"US": "1", "IN": "91", "FR": "33"}
    return f"Country code for {country} is {country_codes.get(country.upper(), 'Unknown')}"

def handle_weather(location):
    # Dummy implementation, replace with actual logic to fetch weather
    return f"Weather information for {location} is not available."

# Command parsing and handling function
def parse_and_handle_command(user_input):
    if user_input.startswith('/'):
        command_parts = user_input.split(' ', 1)
        command = command_parts[0].lower()
        arg = command_parts[1] if len(command_parts) > 1 else ''
        
        if command == '/help':
            return handle_help()
        elif command == '/cc':
            return handle_cc(arg)
        elif command == '/weather':
            return handle_weather(arg)
        else:
            return "Unknown command. Type /help for a list of commands."
    else:
        # Normal chatbot response handling
        return "I'm sorry, I don't understand. Type /help for a list of commands."

# Main chatbot loop
def chatbot():
    print("Welcome to the chatbot! Type /help for a list of commands.")
    while True:
        user_input = input("> ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        response = parse_and_handle_command(user_input)
        print(response)

# Start the chatbot
chatbot()
