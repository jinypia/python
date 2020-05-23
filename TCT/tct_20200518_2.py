'''
배열이 주어질때 둘로 쪼갠 어레이의 합계 차이가 가장 작은 값
[1, -1, -2, 2] 
[1] [-1, -2, 2] -> 1, -1 : 2
[1, -1] [-2, 2] -> 0, 0 : 0
[1, -1, -2] [2] -> -2, 2 : 4
[-1] [-2, 2, 1] -> -1, 1 : 2
[-1, -2] [2, 1] -> -3, 3 : 6
[-2] [2, 1, -1] -> -2, 2 : 4
=> 0 
'''
def suma(arr):
    sum = 0
    for i in arr:
        sum+= i
    return sum

def array(a):
    mn = 100000000000
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            print(a[i:j], a[j:]+a[:i])
            x = suma(a[i:j])
            y = suma(a[j:]+a[:i])
            if x >= y:
                if mn > x-y:
                    mn = x-y
            else:
                if mn > y-x:
                    mn = y-x
    print(mn)
    return mn

a = [1, -1, -2, 2]
b = [1, 2, 3, 4]
c = [-50, 50]
array(a)