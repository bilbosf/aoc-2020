"""
Day 7

Input: List of rules on which color bags must contain how many of other color bags:

###
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
###

Output: How many bags are contained within a shiny gold bag
"""
import click
from pathlib import Path
from collections import deque


def parse_rule(rule, graph):
    container = rule.split("bags")[0][:-1]
    contained_list = rule.split("contain")[1][1:-1].split(", ")

    graph[container] = []
    for contained in contained_list:
        bag_with_number = contained.split(" bag")[0] # Remove " bags" or " bag" from the end

        if bag_with_number == "no other":
            break

        number, bag = bag_with_number.split(" ", 1)
        graph[container].append((int(number), bag))

    return graph

def inner_bags(graph, start):
    # Returns how many bags are contained in the <start> bag
    count = 0
    for number, bag in graph[start]:
        count += number*(1 + inner_bags(graph, bag))

    return count


@click.command()
@click.option("--filename", default="input/day7.txt")
def main(filename):
    filepath = Path(filename)
    with open(filepath) as f:
        rule_list = f.read()
        rule_list = rule_list[:-1].split("\n")

    graph = dict()
    for rule in rule_list:
        graph = parse_rule(rule, graph)

    print(inner_bags(graph, "shiny gold"))
    

if __name__ == "__main__":
    main(None)