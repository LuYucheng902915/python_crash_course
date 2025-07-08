# 8-10.
# Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed.
# After calling the function, print both of your lists to make sure the messages were moved correctly.


def show_messages(messages):
    """Print all messages in the list."""
    print("Showing all messages:")
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_message."""
    print("\nSending all messages:")
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)


messages = ["Hello!", "Hi!", "Wonderful!"]
show_messages(messages)

sent_messages: list[str] = []
send_messages(messages, sent_messages)

print("\nFinal lists")
print(messages)
print(sent_messages)
