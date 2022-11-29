import GeneratorForTask1 as tsk1

import time
import random

def get_listofedges(stredges, weighted = False):
    stredges = stredges[stredges.find("#") + 2:]
    stredges = stredges.split()
    if not weighted:
        del stredges[2::3]
    stredges = [int(i) for i in stredges]
    return stredges

def get_matrix(edges):
    """Без веса"""
    matrix = [[0 for i in range(100)] for j in range(100)]
    for index in range(len(edges) // 2):
        weight = random.randint(0, 1001)
        matrix[int(edges[index + 1]) - 1][int(edges[index]) - 1] = weight
        matrix[int(edges[index]) - 1][int(edges[index + 1]) - 1] = weight
    return matrix

def convert_tomatrix(adjencylist, countofvertex):
    """Без веса"""
    matrix = [[0 for i in range(countofvertex)] for j in range(countofvertex)]
    for vertex in range(countofvertex):
        for neighbor in adjencylist[vertex]:
            weight = random.randint(1, 1000)
            if not matrix[vertex][neighbor]:
                matrix[vertex][neighbor] = weight
            if not matrix[neighbor][vertex]:
                matrix[neighbor][vertex] = weight
    return matrix

def get_adjacencylist(edges, count_vertex):
    """Без веса"""
    result = [[] for i in range(count_vertex)]
    for index in range(len(edges) // 2):
        result[edges[index + 1] - 1].append(edges[index] - 1)
        # result[edges[index ] - 1].append(edges[index + 1] - 1)
    return result

def get_graph_without_cycle(graph, count_vertex):
    """Обход простым дфс. Если обнаружится цикл просто не добавляем в итоговый граф ребро, которое привело к циклу"""
    start = 0
    used = [False for i in range(count_vertex)]
    result = [[] for i in range(count_vertex)]
    dfs_adj = []
    dfs_adj.append(start)
    while len(dfs_adj) > 0:
        cur = dfs_adj.pop()
        for neighbor in graph[cur]:
            if not used[neighbor]:
                used[neighbor] = True
                dfs_adj.append(neighbor)
                if neighbor not in result[cur]:
                    result[cur].append(neighbor)
                if cur not in result[neighbor]:
                    result[neighbor].append(cur)

    return result

def print_test(infile):
    result = ""
    for i in range(len(infile)):
        result += infile[i]
        if(i % 2):
            result+="\n"
        else:
            result+=' '

def print_matrix(matrix):
    output = open("D:/AVM/test_place/result/matrix_" + res_num, 'w')
    for line in matrix:
        output.write(','.join([str(i) for i in line]) + '\n')

def print_list(adjencylist, matrix, weighted = False):
    output = open("D:/AVM/test_place/result/input" + res_num, 'w')
    output.write(str(len(adjencylist)) + " " + str(len(adjencylist) * 2) + "\n")
    for i in range(len(adjencylist)):
        #output.write(str(i) + ": ")
        length = len(adjencylist[i])
        output.write(str(length) + ' ')
        for j in range(length - 1):
            output.write(str(adjencylist[i][j]))
            output.write(' ')
            if weighted:
                output.write(str(matrix[i][j]))
                output.write(' ')
        output.write(str(adjencylist[i][-1]))
        if weighted:
            output.write(' ')
            output.write(str(matrix[i][adjencylist[i][-1]]))
        output.write('\n')

    queries = tsk1.get_input(len(adjencylist), random.randint(0, len(adjencylist)-1))
    output.write(queries)

if __name__ == "__main__":
    count_files = int(input("Enter a count of files: "))
    first_num = int(input("Enter a first number of file index: "))
    for file_i in range(first_num, first_num + count_files):
        file = open("D:/AVM/test_place/test_" + str(file_i) + ".tgf")
        infile = file.read()

        countofvertex = len(infile[:infile.find('#')].split())
        if (file_i <= 9):
            res_num = "0" + str(file_i)
        else:
            res_num = str(file_i)

        listofedges = get_listofedges(infile)
        list = get_adjacencylist(listofedges, countofvertex)
        list = get_graph_without_cycle(list, countofvertex)
        matrix = convert_tomatrix(list, countofvertex)

        countofedges = 0
        for l in list:
            countofedges += len(l)

        print(countofvertex - 1)

        print_matrix(matrix)
        print_list(list, matrix,  True)
        # output = open("D:/AVM/test_place/result/" + res_num, 'w')
        # output.write(result)

        # time.sleep(3)

