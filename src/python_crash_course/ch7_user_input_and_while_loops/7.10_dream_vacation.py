# 7-10. Dream Vacation:
# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where would you go?
# Include a block of code that prints the results of the poll.

"""
poll_results = {}
active = True

while active:
    prompt = "Enter your name before poll: "
    name = input(prompt)
    prompt = "Enter your dream vacation: "
    vacation = input(prompt)
    poll_results[name] = vacation
    prompt = "Continue the poll? Enter yes or no: "
    flag = input(prompt)
    if flag == "no":
        active = False

for name, vacation in poll_results.items():
    print(f"The dream vaction of {name.title()} is {vacation}")
"""

# prompt是不变的，应该定义在循环外
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = input(name_prompt)
    place = input(place_prompt)

    # Store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != "yes":
        break

# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
