from math import log2

def entropy(probabilities):
    return -sum(prob * log2(prob) for prob in probabilities if prob > 0)

def main(input_matrix):
    amount_of_purchases = sum(sum(row) for row in input_matrix)
    
    compatible_event_prob_matrix = [[value / amount_of_purchases for value in row] for row in input_matrix]
    
    p_y_vector = [sum(row) for row in compatible_event_prob_matrix]
    p_x_vector = [sum(col) for col in zip(*compatible_event_prob_matrix)]
    
    H_XY = entropy([prob for row in compatible_event_prob_matrix for prob in row])
    H_Y = entropy(p_y_vector)
    H_X = entropy(p_x_vector)
    
    overall_conditional_H = 0
    for row_index, row in enumerate(compatible_event_prob_matrix):
        conditional_prob_row = [prob / p_y_vector[row_index] for prob in row if p_y_vector[row_index] > 0]
        conditional_H = entropy(conditional_prob_row)
        overall_conditional_H += conditional_H * p_y_vector[row_index]
    
    information_quantity = H_X - overall_conditional_H
    H_XY_through_sum = H_Y + overall_conditional_H
    
    print(f"I(X,Y) = Количество информации: {round(information_quantity, 2)}")
    print(f"H(XY) = Энтропия совместного события: {round(H_XY_through_sum, 2)}")

test_matrix = [[20, 15, 10, 5],
               [30, 20, 15, 10],
               [25, 25, 20, 15],
               [20, 20, 25, 20],
               [15, 15, 30, 25]]

main(test_matrix)