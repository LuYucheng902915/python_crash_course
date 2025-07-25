# 10-7. Addition Calculator:
# Wrap your code from Exercise 10-5 in a while loop so the user can continue entering numbers, even if they make a mistake and enter text instead of a number.

print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nGive me a number: ")
        if x == "q":
            break

        x = int(x)

        y = input("\nGive me another number: ")
        if y == "q":
            break

        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}")

'''
def get_number(prompt):
    """循环提示用户输入一个数字，直到成功或用户输入'q'退出。"""
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'q':
            # 返回一个特殊值（比如None）来表示用户希望退出
            return None 
        
        try:
            # 只把真正可能出错的代码放在 try 块中
            return int(user_input)
        except ValueError:
            print("Sorry, I really needed a number. Please try again or enter 'q' to quit.")

print("Enter 'q' at any time to quit.\n")

while True:
    x = get_number("\nGive me the first number: ")
    # 如果用户在第一次输入时就想退出
    if x is None:
        break

    y = get_number("Give me the second number: ")
    # 如果用户在第二次输入时想退出
    if y is None:
        break
    
    # 到这里，x 和 y 一定是有效的整数了
    total = x + y
    print(f"The sum of {x} and {y} is {total}\n")
    # 让我们可以开始新一轮的计算
'''
