T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    cont = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    cont.sort()
    truck.sort()
    able_cont = 0

    while cont:
        if truck:
            if cont[-1] <= truck[-1]:
                p = cont.pop()
                able_cont += p
                truck.pop()
            else:
                cont.pop()
        else:
            break

    print(f'#{test_case} {able_cont}')
