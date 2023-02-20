#Question 1
# def hello_name(username):
#     print(f"hello_{user_name.title()}!")
# user_name=input("What is your name? ")

# hello_name(user_name)


# #Question 2
# def first_odds():
#     x = 1
#     while x <= 100:
#         if (x % 2) == 1:
#             print(x)
#         x += 1

# first_odds()


# #Question 3
# def inputnumber(message):
#   while True:
#     try:
#        userInput = int(input(message))
#     except ValueError:
#        print("Not an integer! Try again.")
#        continue
#     else:
#        return userInput 

# def max_num_in_list(a_list):
#     n = inputnumber("How many numbers do you want to input? ")

#     for i in range (0,n):
#         number = inputnumber("What is the number? ")
#         a_list.append(number)
#     a_list.sort()
#     print(f"The highest number you've entered is {a_list[-1]}")

# a_list = []
# max_num_in_list(a_list)


# #Question 4
# def inputnumber(message):
#   while True:
#     try:
#        userInput = int(input(message))
#     except ValueError:
#        print("Not an integer! Try again.")
#        continue
#     else:
#        return userInput 

# def is_leap_year(a_year):
#     year = inputnumber("Please type in a year: ")
#     if (year % 4 == 0 and year % 100 != 0):
#         year = 1
#         print(bool(year))
#     elif (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
#         year = 1
#         print(bool(year))
#     else:
#         year = 0
#         print(bool(year))
            
# a_year = 1
# is_leap_year(a_year)

#Question 5
def inputnumber(message):
  while True:
    try:
       userInput = int(input(message))
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 

def max_num_in_list(b_list):
    n = inputnumber("How many numbers do you want to input? ")

    for i in range (0,n):
        number = inputnumber("What is the number? ")
        b_list.append(number)
        b_list.sort()
    return()

def is_consecutive(b_list):
    max_num_in_list(b_list)
    range_list=list(range(min(b_list), max(b_list)+1))
    if b_list == range_list:
        return True
    else:
        return False


b_list = []
n = 0

is_consecutive(b_list)
