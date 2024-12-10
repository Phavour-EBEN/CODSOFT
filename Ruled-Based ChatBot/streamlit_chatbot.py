# import streamlit as st
# from ChatBot import ChatBot

# chatbot = ChatBot()

# st.set_page_config(page_title='chatbot', page_icon="🤖")

# st.title("🤖 Rule-Based ChatBot")
# st.write("Hi there! I'm your virtual assistant. I can help you with reminders, provide weather updates and the least news headlines. Type your message below!")

# # Chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # User input
# user_input = st.text_input("You:", placeholder="Ask me something...")

# # Process user input
# if user_input:
#     # Append user input to chat history
#     st.session_state.messages.append(("You", user_input))

#     # Get chatbot response
#     response = chatbot.process_input(user_input)

#     # Append chatbot response to chat history
#     st.session_state.messages.append(("ChatBot", response))

# # Display chat history
# for sender, message in st.session_state.messages:
#     if sender == "You":
#         st.markdown(f"**You:** {message}")
#     else:
#         st.markdown(f"**ChatBot:** {message}")

import streamlit as st
from ChatBot import ChatBot  # Import the ChatBot class from your original file

def main():
    st.title("ChatBot 🤖")
    st.write("Need a reminder or want to know the weather? I've got you covered!")

    # Initialize the chatbot
    chatbot = ChatBot()

    # Text input for user message
    user_input = st.text_input("Enter your message:")

    # Button to send message
    if st.button("Send"):
        if user_input:
            # Process the input through the chatbot
            response = chatbot.process_input(user_input)
            
            # Display the response
            st.text_area("ChatBot Response:", value=response, height=200)

if __name__ == "__main__":
    main()