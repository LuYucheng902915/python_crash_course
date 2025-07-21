# 8-4. Large Shirts:
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.


def make_shirt(size="large", message="I love Python"):
    info = f"\nThe size of the shirt is {size},"
    info += f"\nThe message: {message}, need to be printed on the shirt."
    print(info)


make_shirt()
make_shirt("medium")
make_shirt("small", "Hello world")
