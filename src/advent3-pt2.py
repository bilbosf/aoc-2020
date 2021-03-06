"""
Day 3 - Part 1

Input: Map with open spaces '.' and trees '#":
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#

Map infinitely repeats itself horizontally:
..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

- Starting from the upper left free space
- Use a slope of right 3, down 1
- Check how many trees you hit by going down that slope until the bottom

Locations that should be checked in the example ('O' for open spaces and 'X' for trees):
..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

In this example, you would encounter 7 trees.
"""

import click
from inf_list import InfList
from pathlib import Path

def get_trees(map_list, slope):
    '''
    Counts the trees hit using the given slope on the given map
    Slope must be passed as a tuple (X, Y) in which for each iteration you will go right X, down Y
    '''

    map_list = [InfList(line) for line in map_list]
    counter = 0
    x_pos = 0
    for i in range(0, len(map_list), slope[1]):
        if map_list[i][x_pos] == "#":
            counter += 1
        x_pos += slope[0]

    return counter


@click.command()
@click.option("--filename", default="input/day3.txt")
def main(filename):
    filepath = Path(filename)
    with open(filepath) as f:
        map_list = f.read()
        map_list = map_list[:-1].split("\n")

    slopes_list = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    accumulator = 1
    for slope in slopes_list:
        n = get_trees(map_list, slope)
        print("For slope = {}, hit {} trees".format(slope, n))
        accumulator *= n

    print("Product = {}".format(accumulator))



if __name__ == "__main__":
    main(None)