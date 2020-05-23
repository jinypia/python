'''
음수, 양수로 구성된 3개의 숫자를 받아 임의로 2개를 선택하여 덧셈 곱셈 뺄샘 중 가장 큰거를 리턴
[ 1, 2, 3 ] -> 2*3 -> 6
[ 1, -2, 3 ] -> 3-(-2) -> 5
'''


def quiz(n):
    mx = -99999999999
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if mx < n[i]*n[j]:
                mx = n[i]*n[j]
            elif mx < n[i]+n[j]:
                mx = n[i]*n[j]
            elif mx < n[i]-n[j]:
                mx = n[i]-n[j]
            elif mx < n[j]-n[i]:
                mx = n[j]-n[i]
    return mx

n1 = [ 1, 2, 3 ]
n2 = [ 1, -2, 3 ] 
n3 = [ 1, 2, -3 ] 

print(quiz(n3))

