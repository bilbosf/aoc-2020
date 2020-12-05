"""
Day 2

Input: password database with "<criterium>: <password>" pairs:
###
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
###

- The criterium "n1-n2 c:" Means the password must contain the letter c at least n1 times and 
  at most n2 times in order to be valid.
- Output: number of valid passwords
"""
import click
from pathlib import Path

def parse(entry):
    '''
    Function that parses an entry and returns a tuple (n1, n2, char, password) from that entry
    '''
    criteria = entry[:entry.index(':')]
    password = entry[entry.index(':')+2:]

    char = criteria[-1]
    n1 = int(criteria[:criteria.index('-')])
    n2 = int(criteria[criteria.index('-')+1:len(criteria)-2])

    return (n1, n2, char, password)

def is_valid(entry):
    n1, n2, char, password = parse(entry)
    ocurrences = password.count(char)
    return ocurrences >= n1 and ocurrences <= n2

@click.command()
@click.option("--filename", default="input/day2.txt")
def main(filename):
    filepath = Path(filename)
    with open(filepath) as f:
        password_list = f.read()
        password_list = password_list[:-1].split("\n")

    count = 0
    for entry in password_list:
        if is_valid(entry):
            count += 1
    
    print("Valid entries: {}".format(count))

    

if __name__ == "__main__":
    main(None)