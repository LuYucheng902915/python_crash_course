# 6-12. Extensions:
# We’re now working with examples that are complex enough that they can be extended in any number of ways.
# Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.

cities_extended = {
    "tokyo": {
        "country": "japan",
        "population": 14_000_000,
        "fact": "It is the largest metropolitan area in the world.",
        "major_landmark": "Tokyo Tower",
    },
    "cairo": {
        "country": "egypt",
        "population": 9_800_000,
        "fact": "It is home to the Great Pyramids of Giza.",
        "major_landmark": "Khan el-Khalili bazaar",
    },
    "paris": {
        "country": "france",
        "population": 2_100_000,
        "fact": 'It is known as the "City of Light".',
        "major_landmark": "Eiffel Tower",
    },
    "new york city": {
        "country": "united states",
        "population": 8_400_000,
        "fact": "It was originally named New Amsterdam.",
        "major_landmark": "Statue of Liberty",
    },
}

print("--- Extended City Information (Improved Formatting) ---")
for city, city_info in cities_extended.items():
    print(f"\n--- {city.title()} ---")
    print(f"Location: {str(city_info['country']).title()}")
    print(f"Population: {city_info['population']:,}")
    # f" { value : format_spec } "。
    # value: 就是 city_info['population']，代表要显示的原始数字（例如 1100000）。
    #:: 这是一个标记，告诉 Python “后面是我对这个值进行格式化的要求”。
    # ,: 这就是格式说明符本身。逗号 , 的特定功能就是用作千位分隔符。
    # 当 Python 的 f-string 解释器看到 :, 这个组合时，它会理解用户的意图是：“请将这个数字以带千位分隔符（逗号）的形式显示出来。”
    print(f"Major Landmark: {city_info['major_landmark']}")
    print(f"Did you know? {city_info['fact']}")
