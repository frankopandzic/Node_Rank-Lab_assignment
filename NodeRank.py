from decimal import Decimal, ROUND_HALF_UP
# import time


def get_node_ranks(nodes, beta, r_start):
    N = len(nodes)
    r1 = [(1-beta)/N for _ in range(N)]
    for i, node in enumerate(nodes):
        for j, dest in enumerate(node):
            r1[int(dest)] += beta * r_start[i] / len(node)
    return r1


if __name__ == '__main__':
    # start = time.time()
    # file = open("C://Users//Franko//Desktop//FAKS//4.Godina//LJETNI//AVSP//LAB4//A//btest2//R.in", "r")
    N, beta = input().split()
    # N, beta = file.readline().split()
    N = int(N)
    beta = float(beta)
    nodes = []
    for i in range(N):
        nodes.append(input().split())
        # nodes.append(file.readline().split())

    all_node_ranks = []
    r = [1/N for _ in range(N)]
    for i in range(100):
        node_ranks = get_node_ranks(nodes, beta, r)
        all_node_ranks.append(node_ranks)
        if node_ranks == r:
            break
        r = node_ranks

    Q = int(input())
    # Q = int(file.readline())
    for i in range(Q):
        n, t = input().split()
        # n, t = file.readline().split()
        n = int(n)
        t = int(t)
        # print(round(node_ranks[t-1][n], 10))
        if t-1 >= len(all_node_ranks):
            print(Decimal(Decimal(all_node_ranks[-1][n]).quantize(Decimal('.0000000001'), rounding=ROUND_HALF_UP)))
            continue
        print(Decimal(Decimal(all_node_ranks[t-1][n]).quantize(Decimal('.0000000001'), rounding=ROUND_HALF_UP)))
    # print(time.time() - start)