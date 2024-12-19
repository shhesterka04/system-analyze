import json
import os

def membership_function(points, x):
    for i in range(len(points) - 1):
        (x0, y0), (x1, y1) = points[i], points[i + 1]
        if x0 <= x <= x1:
            if x0 == x1:
                return max(y0, y1)
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return 0

def fuzzy_control(temp_json, heat_json, rules_json, current_temp):
    temp_data = json.loads(temp_json)
    heat_data = json.loads(heat_json)
    rules = json.loads(rules_json)

    temp_memberships = {term['id']: membership_function(term['points'], current_temp) for term in temp_data['температура']}

    rule_results = []
    for temp_term, heat_term in rules:
        temp_degree = temp_memberships.get(temp_term, 0)
        if temp_degree > 0:
            heat_points = next(term['points'] for term in heat_data['температура'] if term['id'] == heat_term)
            rule_results.append((temp_degree, heat_points))

    if not rule_results:
        return 0

    numerator = 0
    denominator = 0
    for degree, points in rule_results:
        for x, y in points:
            numerator += x * y * degree
            denominator += y * degree

    return numerator / denominator if denominator != 0 else 0

def read_json_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        if not content.strip():
            raise ValueError(f"File {file_path} is empty")
        return content


def main():
    current_temp = 20.0
    optimal_control = fuzzy_control(temp_json, heat_json, rules_json, current_temp)
    print(f'Optimal control value: {optimal_control}')


if __name__ == "__main__":
    base_path = os.path.dirname(__file__)

    temp_json = read_json_file(os.path.join(base_path, "temp.json"))
    heat_json = read_json_file(os.path.join(base_path, "heat.json"))
    rules_json = read_json_file(os.path.join(base_path, "rules.json"))
    main()