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
- The cid field is optional
- Output: number of valid passports
"""
import click


def is_valid(passport):
    keys_in_passport = set()

    for field in passport.split():
        key = field.split(":")[0]
        keys_in_passport.add(key)

    required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    if keys_in_passport.issuperset(required_keys):
        return True
    else:
        return False




@click.command()
@click.option("--filename", default="input/day4.txt")
def main(filename):
    with open(filename) as f:
        passport_list = f.read()
        passport_list = passport_list[:-1].split("\n\n")

    count = 0
    for passport in passport_list:
        print(passport)
        valid = is_valid(passport)
        if valid:
            count += 1
        print("Is valid: {}".format(valid))
        print("----------------------")

    print("Valid count: {}".format(count))



if __name__ == "__main__":
    main(None)