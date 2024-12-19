from collections import deque

def build_matrix(a):
    n = len(a)
    a = {a[i] - 1: n - i for i in range(len(a))}
    print({a[i]: n - i for i in range(len(a))})
    A = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if a[i] >= a[j]:
                A[i][j] = 1
            else:
                A[i][j] = 0

    return A

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def bitwise_and(matrix1, matrix2):
    return [[matrix1[i][j] & matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def matrix_add(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def main():
    a = [3, 1, 2]
    A = build_matrix(a)
    b = [1, 3, 2]
    B = build_matrix(b)

    A_T = transpose(A)
    B_T = transpose(B)

    Y_AB = bitwise_and(A, B)

    Y_AB_T = bitwise_and(A_T, B_T)

    K = matrix_add(Y_AB, Y_AB_T)

    print("Матрица A:")
    for row in A:
        print(row)

    print("\nМатрица B:")
    for row in B:
        print(row)

    print("\nМатрица Y_AB (A & B):")
    for row in Y_AB:
        print(row)

    print("\nТранспонированная матрица A_T:")
    for row in A_T:
        print(row)

    print("\nТранспонированная матрица B_T:")
    for row in B_T:
        print(row)

    print("\nМатрица Y_AB_T (A_T & B_T):")
    for row in Y_AB_T:
        print(row)

    print("\nИтоговая матрица K (Y_AB + Y_AB_T):")
    for row in K:
        print(row)


    def find_ordering(pairs, n):
        graph = {i: [] for i in range(1, n + 1)}
        in_degree = {i: 0 for i in range(1, n + 1)}

        for i, j in pairs:
            graph[i].append(j)
            in_degree[j] += 1

        queue = deque([node for node in in_degree if in_degree[node] == 0])
        result = []
        visited = 0

        while queue:
            node = queue.popleft()
            result.append(node)
            visited += 1

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if visited != n:
            print("Граф имеет цикл, невозможно построить правильную аранжировку")
            return None

        return result

    zero_pairs = []
    for i in range(len(K)):
        for j in range(i, len(K[0])):
            if K[i][j] == 0:
                zero_pairs.append((i + 1, j + 1))

    print("Список пар (i, j), где K[i][j] = 0:", zero_pairs)

    n = len(K)
    ordering = find_ordering(zero_pairs, n)

    print("Упорядоченная последовательность:", ordering)

main()