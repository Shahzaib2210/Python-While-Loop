'''
# Pseudo Code
1 - Declare a numbers_array.
2 - Add while statement while true.
3 - Take number input from user and store in user_input variable.
4 - check if answer number is -1 break the loop and print(sum(numbers_array)/len(numbers_array)).
5 - Else append number in numbers array.
'''
# Array of numbers.
numbers_array = []
# Starting While loop
while True:
    # Taking number input from user.
    user_input = input("Please enter number: ")
    # Checking if user enter -1, then break the loop.
    if user_input == "-1":
        break
    else:
        # Appending numbers in array.
        numbers_array.append(float(user_input))
# Printing sum of number divided by len of total numbers.
print(sum(numbers_array)/len(numbers_array))
