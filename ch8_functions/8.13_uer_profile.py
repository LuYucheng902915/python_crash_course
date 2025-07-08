# 8-13. User Profile:
# Start with a copy of user_profile.py from page 148.
# Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile("Lu", "Yucheng", height="170", location="Hangzhou")
# 在语法层面，关键字参数只能是标识符（也就是符合变量命名规则的名字），不能写成 "height"="170"。
# 在函数内部，所有用 **user_info 收集到的关键字都会被放到一个字典里，字典的键都是 str 类型。
print(user_profile)
