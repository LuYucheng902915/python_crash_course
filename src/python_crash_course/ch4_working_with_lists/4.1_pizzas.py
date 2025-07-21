# 4-1. Pizzas:
# Think of at least three kinds of your favorite pizza.
# Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza.
# For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, that states how much you like pizza.
# The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

pizzas = ["Neapolitan Pizza", "Margherita Pizza", "Chicago Pizza"]

for pizza in pizzas:
    print(pizza)

print("\n")  # 单独的print( "\n") 会空两行
# print() 函数本身要打印的内容是 "\n"，\n 是一个换行符。所以程序会先执行这个换行操作。
# print() 函数执行完毕后，会默认在末尾再追加一个换行符。
# 因此，整个过程是“换行” -> “再换行”，这就造成了两个换行的效果，在视觉上就是隔开了两个完整的空行。

for pizza in pizzas:
    message = f"I like {pizza}"
    print(message)

print("\nI really love pizza!")
