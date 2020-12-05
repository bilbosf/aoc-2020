"""
Day 4

Input: Text file containing passports, separated by blank lines, each passport formed by key:value pairs:

####
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
####

- Every passport must have all of the following fields: byr, iyr, eyr, hgt, hcl, ecl, pid
- Criteria for each field:
    - byr (Birth Year) - four digits; at least 1920 and at most 2002.
    - iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    - eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    - hgt (Height) - a number followed by either cm or in:
        - If cm, the number must be at least 150 and at most 193.
        - If in, the number must be at least 59 and at most 76.
    - hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    - ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    - pid (Passport ID) - a nine-digit number, including leading zeroes.
    - cid (Country ID) - ignored, missing or not.
- The cid field is optional
- Output: number of valid passports
"""

import click
from pathlib import Path

def is_valid_byr(byr):
    if not byr.isdigit():
        return False

    n = int(byr)
    if n < 1920 or n > 2002:
        return False

    return True

def is_valid_iyr(iyr):
    if not iyr.isdigit():
        return False

    n = int(iyr)
    if n < 2010 or n > 2020:
        return False

    return True

def is_valid_eyr(eyr):
    if not eyr.isdigit():
        return False

    n = int(eyr)
    if n < 2020 or n > 2030:
        return False

    return True

def is_valid_hgt(hgt):
    unit = hgt[-2:]
    n = hgt[:-2]

    if not n.isdigit():
        return False
    n = int(n)

    if unit == "cm":
        if n < 150 or n > 193:
            return False
    elif unit == "in":
        if n < 59 or n > 76:
            return False
    else:
        return False

    return True

def is_valid_hcl(hcl):
    if hcl[0] != "#" or len(hcl) != 7:
       return False

    try:
        hexadecimal = int(hcl[1:], 16)
    except:
        return False

    return True
    
def is_valid_ecl(ecl):
    return ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def is_valid_pid(pid):
    return len(pid) == 9 and pid.isdigit()

def is_valid_cid(cid):
    return True

def is_valid(passport):
    '''
    Returns wether a passport is valid or not
    '''

    keys_in_passport = set()

    for field in passport.split():
        key, value = field.split(":")
        keys_in_passport.add(key)
        if not globals()["is_valid_" + key](value): #Checks validity of field by calling appropriate function
            return False

    required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    if keys_in_passport.issuperset(required_keys): #Checks if passport has all required fields
        return True
    else:
        return False


@click.command()
@click.option("--filename", default="input/day4.txt")
def main(filename):
    filepath = Path(filename)
    with open(filepath) as f:
        passport_list = f.read()
        passport_list = passport_list[:-1].split("\n\n")


    count = 0
    for passport in passport_list:
        valid = is_valid(passport)
        if valid:
            count += 1

    print("Valid count: {}".format(count))




if __name__ == "__main__":
    main(None)