"""
Part One:
Given a text file with passports separated by white lines, validate all passports based on containing the below fields:
-byr (Birth Year)
-iyr (Issue Year)
-eyr (Expiration Year)
-hgt (Height)
-hcl (Hair Color)
-ecl (Eye Color)
-pid (Passport ID)
-cid (Country ID) (optional)

Approach:
-Parse the file and create an array with each passport as its own array with each element representing one field
-For each passport, add all the fields that exist into a set and compare it to a global set containing required fields

"""
def create_input_array():
    filepath = 'input.txt'
    input_numbers = []
    with open(filepath) as fp:
        lines = fp.readlines()
        cnt = 1
        current_passport = []
        for line in lines:
            if line == "\n" and current_passport:
                input_numbers.append(current_passport)
                current_passport = []
                continue
            item = line.strip()
            current_passport += item.split()
        input_numbers.append(current_passport)
    return input_numbers

input_numbers = create_input_array()

all_mandatory_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
def validate_passport(passport):
    contained_fields = set()
    for field in passport:
        id_name = field[0:3]
        if id_name != 'cid':
            contained_fields.add(id_name)
    return contained_fields == all_mandatory_fields

def validate_passports(passports):
    count = 0
    for passport in passports:
        if (validate_passport(passport)):
            count += 1
    return count
    
# Part One answer
print(validate_passports(input_numbers))

"""
Part Two:
Do the same as part one except with additional validations:
-byr (Birth Year) - four digits; at least 1920 and at most 2002.
-iyr (Issue Year) - four digits; at least 2010 and at most 2020.
-eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
-hgt (Height) - a number followed by either cm or in:
-If cm, the number must be at least 150 and at most 193.
-If in, the number must be at least 59 and at most 76.
-hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
-ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
-pid (Passport ID) - a nine-digit number, including leading zeroes.
-cid (Country ID) - ignored, missing or not.

Approach:
-Same approach as part one except with a lot more if conditionals and additional helper functions for specific validations
"""
eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
def validate_passport_strict(passport):
    contained_fields = set()
    for field in passport:
        id_name = field[0:3]
        value = field[4:]
        if id_name == 'cid':
            continue
        elif id_name == 'byr':
            if 1920 <= int(value) <= 2002:
                contained_fields.add(id_name)
        elif id_name == 'iyr':
            if 2010 <= int(value) <= 2020:
                contained_fields.add(id_name)
        elif id_name == 'eyr':
            if 2020 <= int(value) <= 2030:
                contained_fields.add(id_name)
        elif id_name == 'hgt':
            metric = value[-2:]
            num_val = value[0:-2]
            if num_val and check_all_digits(num_val):
                num_val = int(num_val)
            else:
                continue
            if (metric == 'cm' and 150 <= num_val <= 193) or (metric == 'in' and 59 <= num_val <= 76):
                contained_fields.add(id_name)
        elif id_name == 'hcl':
            if value[0] == '#' and string_isdigit_isalpha(value[1:]) and len(value) == 7:
                contained_fields.add(id_name)
        elif id_name == 'ecl':
            if value in eye_colors:
                contained_fields.add(id_name)
        elif id_name == 'pid':
            if check_all_digits(value) and len(value) == 9:
                contained_fields.add(id_name)
    return contained_fields == all_mandatory_fields

def check_all_digits(nums):
    for char in nums:
        if not char.isdigit():
            return False
    return True
letters = {'a','b','c','d','e','f'}
letters_digits = {'a','b','c','d','e','f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
# def string_isdigit_isalpha(blob):
#     for letter in blob:
#         if letter not in letters_digits:
#             return False
#     return True
def string_isdigit_isalpha(blob):
    count = 0
    for letter in blob:
        if letter.isdigit():
            count += 1
        elif letter.isalpha() and letter in letters:
            count += 1
    return count == len(blob)

def validate_passports_strict(passports):
    count = 0
    for passport in passports:
        if (validate_passport_strict(passport)):
            count += 1
    return count
test_case = ['pid:087499704', 'hgt:74in', 'ecl:grn', 'iyr:2012', 'eyr:2030', 'byr:1980', 'hcl:#623a2f']

# Part Two answer
print(validate_passports_strict(input_numbers))