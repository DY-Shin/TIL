# def bubble_sort(a):
#     for i in range(len(a)-1, 0, -1):
#         for j in range(0, 1):
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#
# arr = [55, 7, 78, 12, 42]
# print(arr)
# bubble_sort(arr)
# print(arr)
N = 5
num = 49679

cnt = [0] * 10
for _ in range(N):
    cnt[num % 10] += 1
    num //= 10

print(cnt)