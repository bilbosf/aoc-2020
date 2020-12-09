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

- There is an error in the program: either one of the "jmp" operations was supposed to be "nop" or vice-versa.
- Fix the program in such a way that it does not loop infinitely, but terminates by trying to execute the instruction right after the last one.

Output: The accumulator value at the end of the fixed program

"""
import click
from pathlib import Path
from copy import deepcopy


def run(inst_list):
    # Runs the instructions in inst_list and returns the accumulator right before infinite loop

    accumulator = 0
    counter = 0
    visited = [False for x in inst_list]

    while (counter < len(inst_list)) and (not visited[counter]):
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

    return accumulator, (counter >= len(inst_list))


def bruteforce_fix(inst_list):
    # For each "nop" or "jmp" operation in the program, switches it and runs the program to see if it
    # terminates. If it does, return the accumulator value.
    for idx, inst in enumerate(inst_list):
        op, arg = inst
        if op == "nop":
            fix_attempt = deepcopy(inst_list)
            fix_attempt[idx] = ["jmp", arg]
            accumulator, terminated = run(fix_attempt)
            if terminated:
                return accumulator
        elif op == "jmp":
            fix_attempt = deepcopy(inst_list)
            fix_attempt[idx] = ["nop", arg]
            accumulator, terminated = run(fix_attempt)
            if terminated:
                return accumulator
    return -1



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

    print(bruteforce_fix(inst_list))



if __name__ == "__main__":
    main(None)