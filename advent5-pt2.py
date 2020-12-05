"""
Day 5

Input: Text file containing boarding passes, one per line, in the "binary space partitioning" system:

###
FBBBFFBLRR
FFBFFBBRLL
BFFFFFBLRL
FBFBFBFRRR
BBFFBBBLLL
BFBFBFBRRR
FBBBFFBLRL
BBBFFBFLRR
###

- The plane has 128 rows and 8 columns
- The first 7 characters are either F or B, and refer to the row of the seat.
    - Each F character means "divide by 2 the remaining rows and take the lower half"
    - Each B character means "divide by 2 the remaining rows and take the upper half"
- The last 3 characters are  either L or R, and refer to the column of the seat.
    - Each L character means "divide by 2 the remaining columns and take the lower half"
    - Each R character means "divide by 2 the remaining columns and take the upper half"
- Each 10-character sequence completely specifies a seat in the plane
- The seat ID can be calculated by: ID = 8*row + column

Output: The seat ID that is NOT in the input file, but both its neighbors (ID-1 and ID+1) are
"""
import click


def get_ID(seat):
    '''
    Converts a seat's character sequence in the string form to binary, and returns the ID as an integer
    '''
    seat = list(seat)
    for idx, char in enumerate(seat):
        if char == "F" or char == "L":
            seat[idx] = "0"
        else:
            seat[idx] = "1"
    
    binary_str = ""
    for char in seat:
        binary_str += char

    return int(binary_str, 2)
    

@click.command()
@click.option("--filename", default="input/day5.txt")
def main(filename):
    with open(filename) as f:
        seat_list = f.read()
        seat_list = seat_list[:-1].split("\n")

    possible_IDs = [x for x in range(1024)]

    for seat in seat_list:
        seat_ID = get_ID(seat)
        possible_IDs.remove(seat_ID)

    for n in possible_IDs:
        if n+1 in possible_IDs or n-1 in possible_IDs:
            continue
        else:
            print(f"My ID: {n}")


if __name__ == "__main__":
    main(None)