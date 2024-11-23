import csv
import math
from collections import Counter

def calculate_entropy(probabilities):
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

def main():
    data = []
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            data.append([int(x) for x in row[1:]])

    total_counts = [sum(column) for column in zip(*data)]
    total_sum = sum(total_counts)
    probabilities = [count / total_sum for count in total_counts]

    sum_probabilities = probabilities[:6]
    
    product_probabilities = probabilities[6:]

    joint_probabilities = Counter()
    for i in range(len(sum_probabilities)):
        for j in range(len(product_probabilities)):
            joint_probabilities[(i, j)] += sum_probabilities[i] * product_probabilities[j]
    joint_probabilities = [joint_probabilities[key] for key in sorted(joint_probabilities)]

    H_AB = calculate_entropy(joint_probabilities)
    
    H_A = calculate_entropy(sum_probabilities)
    
    H_B = calculate_entropy(product_probabilities)
    
    Ha_B = H_AB - H_A

    I_AB = H_A + H_B - H_AB
    
    return [round(H_AB, 2), round(H_A, 2), round(H_B, 2), round(Ha_B, 2), round(I_AB, 2)]

if __name__ == "__main__":
    print(main())