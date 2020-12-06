"""
Template based on fbidu's template on https://github.com/fbidu/aoc-2020
Day 0

Input:

###
Input file model
###


"""
import click
from pathlib import Path

@click.command()
@click.option("--filename", default="input/day0.txt")
def main(filename):
    filepath = Path(filename)
    with open(filepath) as f:
        input_list = f.read()
        input_list = input_list[:-1].split("\n")



if __name__ == "__main__":
    main(None)