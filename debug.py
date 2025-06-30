def process_positive_number(number):
    """一个简单的函数，处理正数。"""
    print(f"  Processing positive number: {number}")
    return number * 2


def analyze_numbers(numbers_list):
    """分析一个数字列表，计算总和与正数处理后的和。"""
    total_sum = 0
    positive_sum = 0
    print("Starting analysis...")

    for num in numbers_list:
        total_sum += num
        if num > 0:
            processed_num = process_positive_number(num)
            positive_sum += processed_num

    print(f"Total sum: {total_sum}")
    print(f"Processed positive sum: {positive_sum}")
    return positive_sum


# --- 主程序 ---
my_numbers = [1, -2, 5, -8, 10]
final_result = analyze_numbers(my_numbers)
print(f"Final result is: {final_result}")
