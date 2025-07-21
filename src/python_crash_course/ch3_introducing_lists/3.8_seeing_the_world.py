# 3-8. Seeing the World:
# Think of at least five places in the world you’d like  to visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its order has changed.
# • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.

travel_places = ["Japan", "Italy", "Canada", "Australia", "Brazil"]
print(travel_places)
print(sorted(travel_places))  # Sorted list, original list remains unchanged
print(travel_places)  # Original list remains unchanged
print(sorted(travel_places, reverse=True))  # Sorted in reverse order
print(travel_places)  # Original list remains unchanged
travel_places.reverse()  # Reverse the original list
print(travel_places)  # Display the reversed list
travel_places.reverse()  # Reverse it back to original order
print(travel_places)  # Display the original order again
travel_places.sort()  # Sort the original list permanently
print(travel_places)  # Display the sorted list
travel_places.sort(reverse=True)  # Sort the original list in reverse order permanently
print(travel_places)  # Display the list sorted in reverse order
