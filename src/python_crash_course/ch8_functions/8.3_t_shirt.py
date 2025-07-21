# 8-3. T-Shirt:
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.


def make_shirt(size, message):
    info = f"\nThe size of the shirt is {size},"
    info += f"\nThe message: {message}, need to be printed on the shirt."
    print(info)


size = "large"
message = "Victory"
make_shirt(size, message)
make_shirt(message=message, size=size)
