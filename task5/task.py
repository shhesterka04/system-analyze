import json

def find_conflict_core(rank_a, rank_b):
    def flatten_ranking(ranking):
        flat_ranking = {}
        for idx, cluster in enumerate(ranking):
            if isinstance(cluster, list):
                for item in cluster:
                    flat_ranking[item] = idx
            else:
                flat_ranking[cluster] = idx
        return flat_ranking

    flat_a = flatten_ranking(rank_a)
    flat_b = flatten_ranking(rank_b)

    conflict_core = []
    for item in flat_a:
        if item in flat_b and flat_a[item] != flat_b[item]:
            conflict_core.append(item)

    return conflict_core

def main(json_a: str, json_b: str) -> str:
    rank_a = json.loads(json_a)
    rank_b = json.loads(json_b)

    conflict_core = find_conflict_core(rank_a, rank_b)

    return json.dumps(conflict_core)

if __name__ == "__main__":
    json_a = '[1,[2,3],4,[5,6,7],8,9,10]'
    json_b = '[[1,2],[3,4,5],6,7,9,[8,10]]'
    print(main(json_a, json_b))