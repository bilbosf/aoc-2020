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

Output: How many colors of bags could potentially hold a shiny gold bag, directly or indirectly

- In the example, a muted yellow bag holds a shiny gold bag directly
- A dark orange bag holds a muted yellow bag, which holds a shiny gold bag. So a dark orange
  bag holds shiny gold indirectly
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

def bfs(graph, start, target):
    '''
    Runs a breadth-first search on the graph, starting on <start>. Returns True if was able to find the target, False otherwise.
    '''

    found_target = False

    marked = graph.copy()
    for key in marked.keys():
        marked[key] = False

    q = deque()

    marked[start] = True
    q.append(start)

    while len(q) != 0:
        v = q.popleft()
        contained_list = [x[1] for x in graph[v]]
        for w in contained_list:
            if not marked[w]:
                if(w == target):
                    return True
                q.append(w)
                marked[w] = True

    return False



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

    count = 0
    for bag in graph.keys():
        if bfs(graph, bag, "shiny gold"):
            count += 1

    print(count)
    

if __name__ == "__main__":
    main(None)