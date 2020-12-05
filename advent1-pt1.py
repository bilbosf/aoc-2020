"""
Day 1

Input: List of numbers, one per line
###
1721
979
366
299
675
1456
###

Output: product of the 2 numbers in the list that add up to 2020
"""
import click

def search(number_list):
    for n in number_list:
        if 2020-n in number_list:
            return [n, 2020-n]
    return None

@click.command()
@click.option("--filename", default="input/day1.txt")
def main(filename):
    with open(filename) as f:
        number_list = f.read()
        number_list = number_list[:-1].split("\n")
        number_list = [int(x) for x in number_list]

    if number_list:
        result = search(number_list)
        print(result[0] * result[1])


if __name__ == "__main__":
    main(None)
