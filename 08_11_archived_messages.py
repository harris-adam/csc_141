messages = ["Hello!", "How are you?", "Goodbye!"]
sent_messages = []

def send_messages(messages, sent_messages):
    while messages:
        sent_messages.append(messages.pop())

send_messages(messages[:], sent_messages)  # Passing a copy of the list
print("Messages:", messages)  # Original list remains unchanged
print("Sent Messages:", sent_messages)