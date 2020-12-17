# python3
from itertools import chain

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


class Entry:
    def __init__(self, query):
        self.number = query.number
        self.name = query.name

def h(x):
    p = 10 ** 7 + 19
    m = 1000
    a = 10 ** 6 + 484
    b = 10 ** 5 + 123
    return ((a * x + b) % p) % m


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    A = [[]]*1000
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            index = h(cur_query.number)
            for p in A[index]:
                if p.number == cur_query.number:
                    p.name = cur_query.name
                    break
            A[index] = list(chain(A[index], [Entry(cur_query)]))
            # for contact in contacts:
            #     if contact.number == cur_query.number:
            #         contact.name = cur_query.name
            #         break
            # else:  # otherwise, just add it
            #     contacts.append(cur_query)
        elif cur_query.type == 'del':
            index = h(cur_query.number)
            for j in range(len(A[index])):
                if A[index][j].number == cur_query.number:
                    A[index].pop(j)
                    break
            # for j in range(len(contacts)):
            #     if contacts[j].number == cur_query.number:
            #         contacts.pop(j)
            #         break
        else:
            response = 'not found'
            L = A[h(cur_query.number)]
            for p in L:
                if p.number == cur_query.number:
                    response = p.name
                    break
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
    # a = [[]]*3
    # a[0].append(9)
    # print(a)