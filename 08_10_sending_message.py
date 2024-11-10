messages = ["Hello!", "How are you?", "Goodbye!"]
sent_messages = []

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

send_messages(messages, sent_messages)
print("\nFinal lists:")
print("Messages:", messages)
print("Sent Messages:", sent_messages)