# 8-8. User Albums:
# Start with your program from Exercise 8-7.
# Write a while loop that allows users to enter an album’s artist and title.
# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created.
# Be sure to include a quit value in the while loop.


def make_album(name, title):
    album = {"name": name.title(), "title": title.title()}
    return album


while True:
    name = input("Enter the album's artist, enter q to quit. ")
    if name == "q":
        break
    title = input("Enter the albums's title, enter q to quit. ")
    if title == "q":
        break
    album = make_album(name, title)
    print(album)
