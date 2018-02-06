# first_name = input("Please enter your first name: ")
# last_name = input("Please enter your last name: ")
# print(first_name)
# print(last_name)
# print(first_name, last_name)
#
# full_name = first_name + last_name
# if (full_name == full_name[::-1]):
#     print ("Your name is a palindrome!")
# --------------------------------------------
# first_num = int(input("Enter first number: "))
# sec_num = int(input("Enter second number: "))
# print ("num1 + num2 = ",first_num + sec_num)
# print ("num1 - num2 = ",first_num - sec_num)
# print ("num1 * num2 = ",first_num * sec_num)
# print ("num1 / num2 = ",format(first_num / sec_num,'.2f')) # format to 2 decimal places
# print ("num1 // num2 = ",first_num // sec_num)
# print ("num1 % num2 = ",first_num % sec_num)
# print ("num1 ** num2 = ",first_num ** sec_num)
# --------------------------------------------

user_grade = int(input("What is your percentage? "))
if 0 <= user_grade <= 100:
    print ("For your percentage of {}, you received a".format(user_grade), end='')

if 0 <= user_grade <= 59:
    print ("n F")
    print ("You will need to retake the course")
elif 60 <= user_grade <= 69:
    print(" D")
    print ("You will need to retake the course")
elif 70 <= user_grade <= 79:
    print(" C")
elif 80 <= user_grade <= 89:
    print(" B")
elif 90 <= user_grade <= 100:
    print("n A")
    print("Congratulations!")
else:
    print ("Invalid entry")
