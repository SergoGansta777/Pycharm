import random

def isAll(result, countofvertex, start):
    for i in range(countofvertex):
        count = result.count(str(i))
        if count != countofvertex:
            if not( i == start and count == countofvertex + 1):
                print("fail" + str(i))
                return False

        #print(str(i) + " - " + str(count))
    return True

def get_input(countofvertex, cur):
    allpairs = [[j for j in range(countofvertex)] for i in range(countofvertex)]
    counter = countofvertex ** 2

    result_str = str(cur) + '\n'

    while counter:
        while len(allpairs[cur]) == 0:
            cur = random.randint(0, len(allpairs) - 1)

        choice = random.randint(0, len(allpairs[cur]) - 1)
        counter -= 1
        result_str += (str(allpairs[cur][choice]) + '\n')
        allpairs[cur].pop(choice)
        cur = choice

    return result_str

def maybe():
    test = get_input(10, 4)
    print(test)
    print()
    print(len(test.split()))
    print(isAll(test, 10, 4))
    print()