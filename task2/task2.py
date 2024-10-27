from collections import defaultdict


def main(var: str) -> str:
    edges = [tuple(map(int, line.split(','))) for line in var.strip().split('\n')]

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    nodes = sorted(graph.keys())
    result = [[0] * len(nodes) for _ in range(len(nodes))]

    for i, u in enumerate(nodes):
        for v in graph[u]:
            result[i][nodes.index(v)] += 1

    output = '\n'.join(','.join(map(str, row)) for row in result)
    return output


if __name__ == "__main__":
    input_csv = "1,2\n1,3\n3,4\n3,5"
    print(main(input_csv))