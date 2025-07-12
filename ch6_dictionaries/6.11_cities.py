# 6-11. Cities:
# Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city.
# The keys for each city’s dictionary should be something like country, population, and fact.
# Print the name of each city and all of the information you have stored about it.

cities = {
    "tokyo": {
        "country": "japan",
        "population": 14_000_000,
        "fact": "It is the largest metropolitan area in the world.",
    },
    "cairo": {
        "country": "egypt",
        "population": 9_800_000,
        "fact": "It is home to the Great Pyramids of Giza.",
    },
    "paris": {
        "country": "france",
        "population": 2_100_000,
        "fact": 'It is known as the "City of Light".',
    },
}

print("--- City Information ---")
for city, city_info in cities.items():
    print(f"\nHere's some information about {city.title()}:")
    country = city_info["country"]
    population = city_info["population"]
    fact = city_info["fact"]

    print(f"\tIt is located in {str(country).title()}.")
    print(f"\tIt has an approximate population of {population:,}.")
    print(f"\tAn interesting fact: {fact}")
