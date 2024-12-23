import streamlit as st
from ChatBot import ChatBot, ReminderBot, weatherBot, newsletterBot

def initialize_session_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = ChatBot()
    if 'current_module' not in st.session_state:
        st.session_state.current_module = None
    if 'awaiting_input' not in st.session_state:
        st.session_state.awaiting_input = None
    # Initialize with welcome message
    if not st.session_state.messages:
        welcome_message = (
            "Hello there! 👋 I'm your friendly virtual assistant, ChatBot.\n\n"
            "Need a reminder or want to know the weather? I've got you covered!\n"
            "You can ask me things like:\n"
            "- 'What's the weather like?'\n"
            "- 'Set a reminder for me'\n"
            "- 'Show me the latest news'\n\n"
            "How can I help you today? 😊"
        )
        st.session_state.messages.append({"role": "assistant", "content": welcome_message})

def handle_pleasantries(user_input):
    # Dictionary of response patterns
    pleasantry_responses = {
        "greeting": {
            "triggers": ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"],
            "response": "Hi there! 😊 How can I assist you today?"
        },
        "farewell": {
            "triggers": ["bye", "goodbye", "see you", "cya"],
            "response": "Goodbye! Take care and have a great day ahead! 🌟"
        },
        "thanks": {
            "triggers": ["thank", "thanks", "appreciate"],
            "response": "You're welcome! 😊 I'm always here to help."
        },
        "how_are_you": {
            "triggers": ["how are you", "how're you", "how you doing"],
            "response": "I'm doing great, thanks for asking! I'm ready to help you with whatever you need. 😊"
        },
        "help": {
            "triggers": ["help", "what can you do", "what do you do"],
            "response": "I can help you with several things:\n- Check the weather\n- Set reminders\n- Get the latest news\nWhat would you like to try? 🤔"
        }
    }

    user_input_lower = user_input.lower()
    
    # Check for matches and return appropriate response
    for category in pleasantry_responses.values():
        if any(trigger in user_input_lower for trigger in category["triggers"]):
            return category["response"]
    
    return None

def display_chat_history():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_reminder_inputs():
    with st.form(key='reminder_form'):
        title = st.text_input("What should I call the reminder?")
        description = st.text_input("Can you give me a little detail about it?")
        date_time = st.text_input("When should I remind you? (Please use YYYY-MM-DD HH:MM format)")
        submit_button = st.form_submit_button(label='Set Reminder')
        
        if submit_button:
            for module in st.session_state.chatbot.modules:
                if isinstance(module, ReminderBot):
                    response = module.add_reminder(title, description, date_time)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    st.session_state.awaiting_input = None
                    st.rerun()

def handle_weather_inputs():
    with st.form(key='weather_form'):
        city = st.text_input("Enter the city name:")
        submit_button = st.form_submit_button(label='Get Weather')
        
        if submit_button:
            for module in st.session_state.chatbot.modules:
                if isinstance(module, weatherBot):
                    response = module.process_input(f"weather in {city}")
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    st.session_state.awaiting_input = None
                    st.rerun()

def handle_newsletter_inputs():
    with st.form(key='news_form'):
        headline = st.text_input("Enter your headline:")
        submit_button = st.form_submit_button(label='Get News')
        
        if submit_button:
            for module in st.session_state.chatbot.modules:
                if isinstance(module, newsletterBot):
                    response = module.process_input(f"news about {headline}")
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    st.session_state.awaiting_input = None
                    st.rerun()

def main():
    st.title("ChatBot 🤖")
    initialize_session_state()

    # Display chat history
    display_chat_history()

    # Handle different input forms based on the current state
    if st.session_state.awaiting_input == 'reminder':
        handle_reminder_inputs()
    elif st.session_state.awaiting_input == 'weather':
        handle_weather_inputs()
    elif st.session_state.awaiting_input == 'newsletter':
        handle_newsletter_inputs()

    # Main chat input
    if prompt := st.chat_input("What can I help you with?"):
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # First check for pleasantries
        pleasantry_response = handle_pleasantries(prompt)
        if pleasantry_response:
            st.session_state.messages.append({"role": "assistant", "content": pleasantry_response})
            st.rerun()
            return

        # If not a pleasantry, proceed with module handling
        for module in st.session_state.chatbot.modules:
            if module.can_handle(prompt):
                st.session_state.current_module = type(module).__name__
                
                if isinstance(module, ReminderBot):
                    if "add reminder" in prompt.lower():
                        st.session_state.awaiting_input = 'reminder'
                        st.session_state.messages.append({
                            "role": "assistant", 
                            "content": "I'll help you set up a reminder. Please fill in the details below. ⏰"
                        })
                    elif "list reminders" in prompt.lower():
                        response = module.list_reminders()
                        st.session_state.messages.append({"role": "assistant", "content": response})
                    elif "delete reminder" in prompt.lower():
                        st.session_state.awaiting_input = 'delete_reminder'
                        st.session_state.messages.append({
                            "role": "assistant", 
                            "content": "Which reminder would you like to delete?"
                        })
                    else:
                        response = module.process_input(prompt)
                        st.session_state.messages.append({"role": "assistant", "content": response})
                
                elif isinstance(module, weatherBot):
                    st.session_state.awaiting_input = 'weather'
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": "I'll help you check the weather. Please enter a city name below. 🌤️"
                    })
                
                elif isinstance(module, newsletterBot):
                    st.session_state.awaiting_input = 'newsletter'
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": "I'll help you find news. Please enter your headline search below. 📰"
                    })
                
                st.rerun()
                break
        else:
            # If no module can handle the input
            response = (
                "I'm not quite sure how to help with that. 🤔\n\n"
                "I can help you with:\n"
                "- Checking the weather\n"
                "- Setting reminders\n"
                "- Getting the latest news\n\n"
                "Would you like to try one of these?"
            )
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()