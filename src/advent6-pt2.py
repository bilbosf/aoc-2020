"""
Day 6

Input: List of groups of people, separated by a blank line. For each group, each line represents a person's answers to a form. Each of the letters is a question they answered yes to:
###
abc

a
b
c

ab
ac

a
a
a
a

b
###

In the example, the third group has 2 people. The only question to which everyone in the group answered
"yes" is a. So, this group's count is 1.

Output: The sum of the counts for each group in the input
"""
import click
from pathlib import Path

def get_question_set(group):
    '''
    Given a group as a list of strings, each representing a person's answers, returns a set with
    all the questions to each everyone in the group answered yes
    '''
    question_set = set()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in alphabet:
        is_valid = True
        for line in group:
            if not char in line:
                is_valid = False
                break
        if is_valid:
            question_set.add(char)

    return question_set


@click.command()
@click.option("--filename", default="input/day6.txt")
def main(filename):
    filepath = Path(filename)
    with open(filepath) as f:
        groups_list = f.read()
        groups_list = groups_list[:-1].split("\n\n")
    
    for idx, group in enumerate(groups_list):
        groups_list[idx] = group.split("\n")
    
    counter = 0
    for group in groups_list:
        counter += len(get_question_set(group))

    print(counter)


if __name__ == "__main__":
    main(None)