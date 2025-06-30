travel_places = ["Japan", "Italy", "Canada", "Australia", "Brazil"]
print(travel_places)
print(sorted(travel_places))  # Sorted list, original list remains unchanged
print(travel_places)  # Original list remains unchanged
print(sorted(travel_places, reverse=True))  # Sorted in reverse order,
# original list remains
print(travel_places)  # Original list remains unchanged
travel_places.reverse()  # Reverse the original list
print(travel_places)  # Display the reversed list
travel_places.reverse()  # Reverse it back to original order
print(travel_places)  # Display the original order again
travel_places.sort()  # Sort the original list permanently
print(travel_places)  # Display the sorted list
travel_places.sort(reverse=True)  # Sort the original list in reverse order permanently
print(travel_places)  # Display the list sorted in reverse order
