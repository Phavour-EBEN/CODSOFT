import datetime
import requests

import re

class BaseBotModule:
    """Base class for all bot functionality modules"""
    def can_handle(self, user_input):
        # Determine if this module can handle the user input To be implemented by child classes
        return False
    
    def process_input(self, user_input):
        # Process the user input To be implemented by child classes
        
        raise NotImplementedError("Each module must implement process_input method")


class ReminderBot(BaseBotModule):
    def __init__(self):
        self.reminders = []

    def can_handle(self, user_input):
        reminder_keywords = ['remind', 'reminder', 'schedule', 'todo', 'task', 'appointment']
        return any(keyword in user_input.lower() for keyword in reminder_keywords)

    def process_input(self, user_input):
        if "add reminder" in user_input:
            print("Alright! Let's set up a reminder.")
            title = input("What should I call the reminder? ")
            description = input("Can you give me a little detail about it? ")
            date_time = input("When should I remind you? (Please use YYYY-MM-DD HH:MM format): ")
            return self.add_reminder(title, description, date_time)
        elif "list reminders" in user_input:
            return "Here’s a list of your reminders:\n" + self.list_reminders()
        elif "delete reminder" in user_input:
            print("Sure, I can delete a reminder for you.")
            title = input("Which reminder should I delete? ")
            return self.delete_reminder(title)
        else:
            return "I'm here to help with your reminders. Try saying 'add reminder', 'list reminders', or 'delete reminder'."

    def add_reminder(self, title, description, date_time):
        try:
            date_time = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M")
            self.reminders.append({'title': title, 'description': description, 'date_time': date_time})
            return f"Reminder set for '{title}' at {date_time}.\n"
        except ValueError:
            return "Invalid date and time format. Please use 'YYYY-MM-DD HH:MM'.\n"

    def delete_reminder(self, title):
        for reminder in self.reminders:
            if reminder['title'].lower() == title.lower():
                self.reminders.remove(reminder)
                return f"Reminder '{title}' deleted.\n"
        return f"Reminder '{title}' not found.\n"

    def list_reminders(self):
        if not self.reminders:
            return "No reminders found.\n"
        response = "Your reminders:\n"
        for reminder in self.reminders:
            response += f"Title: {reminder['title']}, Description: {reminder['description']}, Time: {reminder['date_time']}\n"
        return response

    def get_due_reminders(self):
        now = datetime.datetime.now()
        due_reminders = [rem for rem in self.reminders if rem["date_time"] <= now]
        if due_reminders:
            response = "Due reminders:\n"
            for reminder in due_reminders:
                response += f"Title: {reminder['title']}, Description: {reminder['description']}, Time: {reminder['date_time']}\n"
            return response
        return "No reminders are due.\n"
    
import os
from dotenv import load_dotenv
load_dotenv()
class weatherBot(BaseBotModule):
    def __init__(self):
        self.open_weather_api =os.getenv('open_weather_api')
        self.base_url = os.getenv('base_url')

    def can_handle(self, user_input):
        """Check if input is related to weather"""
        weather_keywords = [
            'weather', 'temperature', 'forecast', 
            'degrees', 'climate', 'sunny', 'rainy'
        ]
        return any(keyword in user_input.lower() for keyword in weather_keywords)

    def process_input(self, user_input):
        city_name = input("Enter the city name: ")
        url = f"{self.base_url}?q={city_name}&appid={self.open_weather_api}"
        # print(url)
        response = requests.get(url)
        # print(response.json())

        if response.status_code == 200:
            data = response.json()
            weather_data = data['weather'][0]['main']
            temp_data = data['main']['temp']
            # print(f'The current weather is {weather_data}.')
            # print(f'The current temperature is {temp_data}°C (degrees).')
            return f"The current weather in {city_name} is {weather_data} with a temperature of {temp_data}°C."
        else:
            return "Sorry, I couldn't retrieve the weather information."
            

class ChatBot:
    def __init__(self):
        # List of bot modules
        self.modules = [
            weatherBot(),
            ReminderBot()
        ]
        
        # Default fallback module
        self.default_module = DefaultModule()
    
    def process_input(self, user_input):
        """
        Route user input to appropriate module
        """
        # Find the first module that can handle the input
        for module in self.modules:
            if module.can_handle(user_input):
                return module.process_input(user_input)
        
        # If no module can handle, use default
        return self.default_module.process_input(user_input)
    
    def start_chat(self):
        print("Hello there! 👋 I'm your friendly virtual assistant, ChatBot.")
        print("Need a reminder or want to know the weather? I’ve got you covered!")
        print("You can ask me things like 'What's the weather like?' or 'Set a reminder for me.'")
        print("And when you're done, just type 'exit' to end our chat. Let's get started! 😊")

        
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("ChatBot: It's been great talking with you. Have a wonderful day! 🌟")
                break
            
            
            # Add conversational flair
            if "weather" in user_input.lower():
                print("ChatBot: Let me grab the latest weather update for you. Hang tight! 🌤️.")
                
            elif "reminder" in user_input.lower():
                print("ChatBot: Sure! Let me assist you with reminders.")
                
            elif any(greeting in user_input.lower() for greeting in ["hi", "hello", "hey"]):
                print("ChatBot: Hi there! 😊 How can I assist you today?")
                continue
            elif any(farewell in user_input.lower() for farewell in ["bye", "goodbye", "see you"]):
                print("ChatBot: Goodbye! Take care and have a great day ahead! 🌟")
                continue
            elif "how are you" in user_input.lower():
                print("ChatBot: I'm just a bot, but I'm here to help! How can I assist you?")
            elif "thank you" in user_input.lower() or "thanks" in user_input.lower():
                print("ChatBot: You're welcome! 😊 I'm always here to help.")
                continue
            elif "help" in user_input.lower():
                print("ChatBot: Of course! I can assist with weather updates and reminders. What would you like to do?")
                continue
            else:
                print("ChatBot: Hmm, I didn't quite catch that. Could you rephrase? Maybe I can help with reminders or weather updates.")
                continue

             # Process the user input
            response = self.process_input(user_input)
            
            print("ChatBot:", response)
class DefaultModule(BaseBotModule):
    """
    Fallback module for unhandled inputs
    """
    def can_handle(self, user_input):
        """Always returns True as a last resort"""
        return True
    
    def process_input(self, user_input):
        """
        Provide a generic response for unhandled inputs
        """
        return (
            "I'm not sure how to help with that. "
            "I can assist with weather and reminders. "
            "Try asking about the weather or managing reminders."
        )

# Demonstration of usage
def main():
    # Create chatbot instance
    chatbot = ChatBot()   
    # Start the chat
    chatbot.start_chat()


# Main loop for chatbot interaction
if __name__ == "__main__":
    main()

    