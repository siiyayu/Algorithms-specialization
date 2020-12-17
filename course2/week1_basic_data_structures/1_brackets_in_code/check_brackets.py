# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


# Bracket = namedtuple("Bracket", "char position") # same


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    closing_brackets_stack = []
    n1 = 0
    n2 = 0
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i + 1))
            # n1 = len(opening_brackets_stack)

        if next in ")]}":
            closing_brackets_stack.append(Bracket(next, i))
            # n2 = len(closing_brackets_stack)
            if len(opening_brackets_stack) == 0 or \
                    not are_matching(opening_brackets_stack[-1][0], closing_brackets_stack[-1][0]): #checking if brackets are not match
                return i + 1
            else:
                opening_brackets_stack.pop()
                closing_brackets_stack.pop()
    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[0][1]
    return "Success"


def test():
    assert find_mismatch('[]') == 'Success', print(find_mismatch('[]'))
    assert find_mismatch('{}[]') == 'Success', print(find_mismatch('[]'))
    assert find_mismatch('[()]') == 'Success', print(find_mismatch('[]'))
    assert find_mismatch('(())') == 'Success', print(find_mismatch('[]'))
    assert find_mismatch('{[]}[]') == 'Success', print(find_mismatch('[]'))
    assert find_mismatch('[]') == 'Success', print(find_mismatch('[]'))
    assert find_mismatch('{[}') == 3, print(find_mismatch('{[}'))
    assert find_mismatch('foo(bar)') == 'Success', print(find_mismatch('foo(bar)'))
    assert find_mismatch('{') == 1, print(find_mismatch('{'))




def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # test()


if __name__ == "__main__":
    main()
