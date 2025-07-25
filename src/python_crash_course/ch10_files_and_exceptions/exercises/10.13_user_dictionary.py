# 10-13. User Dictionary:
# The remember_me.py example only stores one piece of information, the username.
# Expand this example by asking for two more pieces of information about the user, then store all the information you collect in a dictionary.
# Write this dictionary to a file using json.dumps(), and read it back in using json.loads().
# Print a summary showing exactly what your program remembers about the user.

import json
from pathlib import Path


def get_stored_user_info(path):
    """Get stored user info if avaliable."""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None


def get_new_user_info(path):
    """Get information from a new user."""
    username = input("What is your name? ")
    game = input("What's your favorite game? ")
    animal = input("What's your favorite animal? ")

    user_dict = {
        "username": username,
        "game": game,
        "animal": animal,
    }

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict


def greet_user():
    """Greet the user by name, and state what we know about them."""
    path = Path("user_info.json")
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome back, {user_dict['username']}")
        print(f"Hope you've been playing some {user_dict['game']}")
        print(f"Have you seen a {user_dict['animal']} recently")
    else:
        user_dict = get_new_user_info(path)
        msg = f"We'll remember you when you return, {user_dict['username']}"
        print(msg)


greet_user()
