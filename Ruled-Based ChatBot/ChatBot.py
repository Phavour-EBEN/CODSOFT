import datetime

class ReminderBot:
    def __init__(self):
        self.reminders = []
        self.welcome_message = "Hello, Welcome!\nI am your virtual assistant ChatBot. How can I help you."
        print(self.welcome_message)

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

# Main loop for chatbot interaction
if __name__ == "__main__":
    bot = ReminderBot()

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("Goodbye!")
            break

        elif user_input == "add reminder":
            title = input("Enter reminder title: ")
            description = input("Enter reminder description: ")
            date_time = input("Enter reminder date and time (YYYY-MM-DD HH:MM): ")
            print(bot.add_reminder(title, description, date_time))

        elif user_input == "delete reminder":
            title = input("Enter reminder title to delete: ")
            print(bot.delete_reminder(title))

        elif user_input == "list reminders":
            print(bot.list_reminders())

        elif user_input == "due reminders":
            print(bot.get_due_reminders())

        else:
            print("I didn't understand that. Try 'add reminder', 'delete reminder', 'list reminders', or 'due reminders'.")
