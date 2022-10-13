def my_strrev(s):
    # 문자열 s를 리스트로 변환
    # for문을 이용해서 뒤집기
    # 리스트를 문자열로 변환
    s_list = list(s)
    for i in range(len(s_list) // 2):
        s_list[i], s_list[len(s_list) - 1 - i] = s_list[len(s_list) - 1 - i], s_list[i]
    new_s = ''.join(s_list)
    return new_s

s = 'algorithm'
# s = my_strrev(s)
# s = s[::-1]
s_list = list(s)
s_list.reverse()
s = ''.join(s_list)
print(s)