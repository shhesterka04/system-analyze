import math

def task(var: str) -> float:
    matrix = [list(map(int, line.split(','))) for line in var.strip().split('\n')]

    entropy = 0
    for row in matrix:
        row_sum = sum(row)
        if row_sum > 0:
            for value in row:
                if value > 0:
                    p = value / row_sum
                    entropy -= p * math.log2(p)

    return round(entropy, 1)

if __name__ == "__main__":
    input_csv = "2,0,2,0,0\n0,1,0,0,1\n2,1,0,0,1\n0,1,0,1,1\n0,1,0,1,1"
    print(task(input_csv))