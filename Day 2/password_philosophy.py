"""
Given an input.txt file in the following example format: 1-3 a: abcde
Print how many passwords are valid
A password is valid if it contains letters between and including the range given for the specified letter

Approach:
    -Download the input text
    -Parse the text and create an array in the following format: [beginning range, end range, letter, password]
    -Loop through the array and increment a counter 
    -Print the counter
"""

filepath = 'input.txt'
input_numbers = []
with open(filepath) as fp:
   lines = fp.readlines()
   cnt = 1
   for line in lines:
       item = line.strip().split(" ")
       num_range = item[0].split("-")
       num_range = [int(num_range[0]), int(num_range[1])]
       item = num_range + [item[1][0]] + [item[2]]
       input_numbers.append(item)

def contains_letters(lowest, highest, letter, password):
    counter = password.count(letter)
    return lowest <= counter <= highest

valid_passwords = 0
for item in input_numbers:
    if contains_letters(item[0], item[1], item[2], item[3]):
        valid_passwords += 1
print(valid_passwords)

"""
Part Two: The first number and the second number now represent indices - 1 (ex. first position at index 0 is represented as 1 in the input_array)
           At each index for the password, there must only be 1 occurence of the letter within the password to be valid

Approach:
    -Use the same input_array
    -If the first two numbers are valid indices in the password then check it
    -Increment a counter
    -If counter is 1 then return True else return False
"""

def valid_password(first_pos, second_pos, letter, password):
    count = 0
    password_length = len(password)
    if first_pos - 1 < password_length and password[first_pos - 1] == letter:
        count += 1
    if second_pos - 1 < password_length and password[second_pos - 1] == letter:
        count += 1
    if count == 1:
        return True
    return False

valid_password_count_2 = 0
for item in input_numbers:
    if valid_password(item[0], item[1], item[2], item[3]):
        valid_password_count_2 += 1
print(valid_password_count_2)
