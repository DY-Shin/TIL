n = int(input())

line_1 = list(input())
line_2 = list(input())
line_3 = list(input())
line_4 = list(input())
line_5 = list(input())
line_6 = list(input())
line_7 = list(input())
line_8 = list(input())

square = [line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8]
count = 0

for i in range(8 - n):
    k = []
    for j in range(8 - n):
        k.append(square[j][i])
        if k == k[::-1]:
            count += 1
