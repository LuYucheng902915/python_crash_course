# 8-6. City Names:
# Write a function called city_country() that takes in the name of a city and its country.
# The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values that are returned.


def city_country(city, country):
    str = f"{city.title()}, {country.title()}"
    return str


str1 = city_country("Beijing", "China")
str2 = city_country("Hangzhou", "China")
str3 = city_country("New York", "US")
print(str1)
print(str2)
print(str3)
