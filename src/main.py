import itertools

def route_cost(route, dist_matrix):
    total = 0
    for step in range(len(route) - 1):
        src, dst = route[step], route[step + 1]
        total += dist_matrix[src][dst]
    return total


def tsp_solve(dist_matrix):
    n         = len(dist_matrix)
    cities    = list(range(1, n))
    opt_route = None
    opt_cost  = float('inf')

    all_perms = list(itertools.permutations(cities))

    border = '=' * 64
    separator = '-' * 64

    print(border)
    print(f"  Jumlah kota          : {n}")
    print(f"  Total permutasi diuji: {len(all_perms)}")
    print(border)
    print(f"  {'No':<5} {'Rute':<35} {'Biaya':>8}")
    print(separator)

    for idx, perm in enumerate(all_perms, start=1):
        route = [0] + list(perm) + [0]
        cost  = route_cost(route, dist_matrix)
        route_str = ' -> '.join(map(str, route))
        print(f"  {idx:<5} {route_str:<35} {cost:>8}")

        if cost < opt_cost:
            opt_cost  = cost
            opt_route = route

    print(border)
    print(f"  Rute optimal : {' -> '.join(map(str, opt_route))}")
    print(f"  Biaya minimum: {opt_cost}")
    print(border)
    return opt_route, opt_cost


if __name__ == '__main__':
    dist_matrix = [
        [0, 10, 15, 20],
        [10,  0, 35, 25],
        [15, 35,  0, 30],
        [20, 25, 30,  0],
    ]
    tsp_solve(dist_matrix)
