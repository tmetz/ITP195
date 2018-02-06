# sum = 0
# earlyquit = 0
# while sum < 100:
#     user_num = int(input("Please enter a positive integer:"))
#     if user_num < 0:
#         print("Oops!  You got early quit for entering a negative integer ", user_num)
#         earlyquit = 1
#         break
#     else:
#         sum += user_num
# if (earlyquit == 0):
#     print("The sum of entered integers: ",sum)

sum = 0
earlyquit = 0
while sum < 100:
    user_num = int(input("Please enter a positive integer:"))
    if user_num > 0:
        sum+=user_num
    else:
        print("Oops!  You got early quit for entering a negative integer ", user_num)
        break
else:
    print("The sum of entered integers: ",sum)
