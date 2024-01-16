def longer_than(n: int, words: list[str]) -> list[str]:
    """
    takes a value and a list of words
    :param n: threshold value
    :param words: list of texts
    :return: a new list with all the texts longer than n
    """
    return [w for w in words if len(w) > n]


def lastword(sentence: str) -> str:
    """ returns the last word from a sentence """
    return sentence.split().pop()

print(lastword("famous last words"))
print(longer_than(3, ["one", "two", "three"]))
print(longer_than(3, [range(10), "a", [1, 2, 3, 4, 5]]))

