def baby_gin(player):
    global flag
    for i in range(len(player)):
        if player[i] + 1 in player and player[i] + 2 in player:
            flag = 1
            break
    for i in range(len(player)):
        tri = player[i]
        cnt = 0
        for j in range(len(player)):
            if player[j] == tri:
                cnt += 1
        if cnt >= 3:
            flag = 1
    return flag


T = int(input())
for test_case in range(1, T + 1):
    game = list(map(int, input().split()))
    player1 = [game[0], game[2]]
    player2 = [game[1], game[3]]
    flag = 0
    winner = 0
    for i in range(4, len(game)):
        if i % 2:
            player2.append(game[i])
            baby_gin(player2)
            if flag:
                winner = 2
                break
        else:
            player1.append(game[i])
            baby_gin(player1)
            if flag:
                winner = 1
                break
    print(f'#{test_case} {winner}')
