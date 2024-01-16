import io
import typing
import re
from collections import namedtuple
from dataclasses import dataclass
import itertools
# Node = namedtuple("Node", ["left", "right"])

# Same thing - data class
@dataclass(frozen=True)
class Node:
    left: str
    right: str


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




def parse(input: typing.IO) -> tuple[str, dict[str, Node]]:
    path = input.readline().strip()
    map = {}
    input.readline()

    for line in input:
        node, left, right = re.findall(r'\w+', line)
        map[node] = Node(left=left, right=right)

    return (path, map)

def walk(map: dict[str, Node], path: typing.Iterable) -> list[str]:
    """
    walks the given desert using a provided path
    :param map: map of the desert
    :param path: the LRLL path to walk
    :return: list of nodes visited
    """
    location = 'AAA'
    result = []
    for turn in itertools.takewhile(lambda p: location != 'ZZZ', path):
        result.append(location)
        if turn == 'L':
            location = map[location].left
        elif turn == 'R':
            location = map[location].right
        else:
            raise Exception(f"Invalid turn {turn}")

    result.append(location)
    return result


def walk_v2(map: dict[str, Node], path: typing.Iterable) -> list[str]:
    """
    walk_v2 is a generator version of walk
    it makes sense because now we don't need to create the list
    and we can let external code decide when to stop wondering in
    the desert
    """
    location = 'AAA'
    for turn in path:
        yield location
        if turn == 'L':
            location = map[location].left
        elif turn == 'R':
            location = map[location].right
        else:
            raise Exception(f"Invalid turn {turn}")



# path, map = parse(io.StringIO(input))
# print(walk(map, path))

with open('map.txt', encoding='utf8') as f:
    path, map = parse(f)
    print(walk(map, itertools.cycle(path)))
    print(list(itertools.takewhile(lambda location: location != 'ZZZ',
                                  walk_v2(map, itertools.cycle(path)))))


