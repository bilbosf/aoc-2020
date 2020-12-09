"""
Day 8

Input: List of instructions "<operation> <argument>":

###
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
###

- nop = No Operation. Does nothing, instruction immediately below is executed
- acc = Adds the argument to a global value called the accumulator
- jmp = Jumps to a new instruction relative to itself, offset by the argument. "jmp +3" means jump 3 instructions below.

Output: The value on the accumulator right before the program tries to run any instruction for the second time (infinite loop)
"""
import click
from pathlib import Path


def run(inst_list):
    # Runs the instructions in inst_list and returns the accumulator right before infinite loop
    
    accumulator = 0
    counter = 0
    visited = [False for inst in inst_list]

    while not visited[counter]:
        inst, arg = inst_list[counter]
        visited[counter] = True
        if inst == "nop":
            counter += 1
            continue
        elif inst == "acc":
            accumulator += arg
            counter += 1
            continue
        elif inst == "jmp":
            counter += arg
            continue

    return accumulator




@click.command()
@click.option("--filename", default="input/day8.txt")
def main(filename):
    filepath = Path(filename)
    with open(filepath) as f:
        inst_list = f.read()
        inst_list = inst_list[:-1].split("\n")

    for idx, inst in enumerate(inst_list):
        inst_list[idx] = inst.split()
        inst_list[idx][1] = int(inst_list[idx][1])

    print(run(inst_list))



if __name__ == "__main__":
    main(None)