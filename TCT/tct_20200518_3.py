'''
1110010000, 5 회 수행

1회: 1110010000 --> [3, 2, 1, 4] --> 11101100
            -> 1이 3번(11) 0이 2번(10) 1이 1번(1) 0이 4번(100) 
                             -> 각 횟수를 2진수로 변환해서 string 더하기
2회: 11101100   --> [3, 1, 2, 2] --> 1111010
3회: 1111010    --> [4, 1, 1, 1] --> 100111
4회: 100111     --> [1, 2, 3] --> 11011
5회: 11011      --> [2, 1, 2] --> 10110
'''
# 1110010000 -> [3, 2, 1, 4] 10 문자 
def makearray(s):
    ret = []
    cnt = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            cnt += 1
        else:
            ret.append(cnt)
            cnt = 1
    ret.append(cnt) # 마지막자리 수 계산 
 #   print (ret)
    return ret

# [3, 2, 1, 4] -> 11 10 1 110 (binary 합계로 변환)
def binary(arr):
    ret = ''
    for i in arr:
        ret += "{0:b}".format(i)
#    print(ret)
    return ret

# 입력 및 반복 수행 : n - string, k - int
def solution(n, k):
    ret = n
    for i in range(k):
        ret = binary(makearray(ret))
        print(i+1, ret)
    return ret

s = '1110010000'
#makearray(s)
solution(s, 5)