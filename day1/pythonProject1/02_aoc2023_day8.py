import io
import typing
import re
from collections import namedtuple
from dataclasses import dataclass
Node = namedtuple("Node", ["left", "right"])

# Same thing - data class
# @dataclass
# class Node:
#     left: str
#     right: str
#
#
node = Node(left="AAA", right="BBB")
# print(node.left)

input = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

"""
Your Turn:
1. Write a new function that takes a map and an instruction line
   and walks the path of the instruction line,
   returning the IDs of the nodes on the way

2. Modify parse() to return also "path"   

3. Handle maps that look like this (that is iterate the path until you reach the end):
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""




def parse(input: typing.IO) -> dict[str, Node]:
    path = input.readline().strip()
    map = {}
    input.readline()

    for line in input:
        node, left, right = re.findall('\w+', line)
        map[node] = Node(left=left, right=right)

    return map

map = parse(io.StringIO(input))
print(map)



