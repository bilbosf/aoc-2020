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

Output: product of the 3 numbers in the list that add up to 2020
"""
import click
from pathlib import Path

def search(number_list):
    for idx, n in enumerate(number_list):
        for m in number_list[idx:]:
            if 2020-n-m in number_list:
                return [n, m, 2020-n-m]
    return None

@click.command()
@click.option("--filename", default="input/day1.txt")
def main(filename):
    filepath = Path(filename)
    with open(filepath) as f:
        number_list = f.read()
        number_list = number_list[:-1].split("\n")
        number_list = [int(x) for x in number_list]

    if number_list:
        result = search(number_list)
        print(result[0] * result[1] * result[2])


if __name__ == "__main__":
    main(None)
