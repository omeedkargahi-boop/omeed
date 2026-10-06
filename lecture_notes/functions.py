# # # name = "Omeed"

# # # # print("Hello", name)

# # # def say_hello(name):
# # #     print("Hello", name)

# # # say_hello(name)

# # # def add(a,b):
# # #     print(a+b)

# # # add(7,8)

# # # def check_num(num):
# # #     if num > 0:
# # #         return "Positive"
# # #     elif num < 0:
# # #         return "Negative"
# # #     elif num == 0:
# # #         return "Zero"

# # # print(check_num)

# # # print(False or False)

# # # def can_vote(age, is_citizen):
# # #     if age >= 18 and is_citizen:
# # #         print("You can vote!")
# # #     else:
# # #         print("You cannot vote")
# # # can_vote(18, True)

# # def is_weekend(day):
# #     if day=="Saturday" or day=="Sunday":
# #         return "It is the weekend!"
# #     else:
# #         return "It is not the weekend :("
# # print(is_weekend("Monday"))

# for i in range(10):
#     print(i)

def in_range(n):
    if n > 100 or n < 10:
        return "True"
    else:
        return "False"

print(in_range(99))