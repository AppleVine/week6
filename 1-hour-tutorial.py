
# Lists
# [] means storing a bunch of values in a list. This list can contain strings, numbers & boolian values, python doesn't care. 
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# print(friends) -- prints out the entire list. 
# print(friends[0]) -- prints index 0 of the list. 
# print(friends[-1]) -- prints the last person on the list. -2 second last etc. 
# print(friends[1:]) -- prints all data after index 1. 
# print(friends[1:3]) -- prints all data from index 1 through to 2. [up to but NOT including]
# friends[1] = "Mike"
#Updated index 1 from Karen --> Mike. 
# print(friends[1])

# ----------------------------------------

#Functions with lists.

# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
# lucky_numbers = [4, 8, 15, 16, 23, 42]
# friends.extend(lucky_numbers) -- adds one list onto the other. 
# friends.append("Creed") -- adds another data point onto the end of the list. 
# friends.insert(1, "Kelly") -- inserts Kelly into index 1, 1 onwards get pushed 1 to the right. 
# friends.remove("Jim") -- Removes Jim from the list.
# friends.clear() -- removes all data from the list. 
# friends.pop() -- removes the last element off the list. 
# print(friends.index("Kevin")) -- tells you the index of Kevin. If it's not in the list, it'll give an error saying not in the list.
# print(friends.count("Jim")) -- counts the amount of entries of "Jim"
# friends.sort() -- sorts in alphabetical/ascending (numberically) order. 
# lucky_numbers.reverse() -- reverses order of list.
# friends2 = friends.copy -- makes a list of friends2 which copies friends
# print(friends)

# ----------------------------------------

# Tuples.
# Tuples is a data-structure/container that stores values. Tuples are immutable -- can't be changed or modified once created.

# coordinates = (4, 5)
# print(coordinates[0]) -- prints entry at index 0. 
# coordinates[1] = 10. -- Will tell you tuple does not support item assignment. 
# You can make a list of tuples.

# ----------------------------------------

#Functions. 
# def - defining a function. 

# def sayhi(name, age):
#     print("Hello " + name + ", you are " + str(age))

# sayhi("Mike", 38)

# ----------------------------------------

# Return Statement

# def cube(num):
#     return num*num*num

# You cannot put any more code after "return". 

# result = cube(4)

# print(result)

# ----------------------------------------

# If statements

# is_male = True
# is_tall = False

# if is_male and is_tall:
#     print("You are a tall male.")
# elif is_male or is_tall: 
#     print("You either a male or tall.")
# else:
#     print("You are neither male nor tall.")

# ----------------------------------------

# If statements & Comparisons. 

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: 
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(5, 15, 3))

# ----------------------------------------