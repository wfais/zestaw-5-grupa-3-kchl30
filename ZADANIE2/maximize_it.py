from itertools import product

def maximize_expression(K, M, lists):
    all_combinations = product(*lists)
    return max(sum(x**2 for x in combination) % M for combination in all_combinations)

if __name__ == "__main__":
    K, M = map(int, input().rstrip().split())

    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    result = maximize_expression(K, M, lists)
    print(result)
