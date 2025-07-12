# -5. Rivers:
# Make a dictionary containing three major rivers and the country each river runs through.
# One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers = {
    "nile": "Egypt",
    "Amazon": "Brazil",
    "Mississippi": "US",
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country}")
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)
