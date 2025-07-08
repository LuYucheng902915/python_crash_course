# 8-11.
#  Messages: Start with your work from Exercise 8-10.
#  the function send_messages() with a copy of the list of messages.
# After calling the function, print both of your lists to show that the original list has retained its messages.


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
send_messages(messages[:], sent_messages)

print("\nFinal lists")
print(messages)
print(sent_messages)
