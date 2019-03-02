# -*- coding: utf-8 -*-

def main():
    T = int(input())
    for time in range(T):
        N, K, x1, y1, C, D, E1, E2, F = [int(s) for s in input().split()]
        A = []
        A.append((x1 % F + y1 % F) % F)
        for i in range(2, N + 1):
            A.append(((C % F + D % F)*A[-1] + E1 % F + E2 % F) % F) 
        sum = 0
        for i in range(1, K + 1):
            sum += POWER(N, A, i)
            sum %= 1000000007
        print('Case #'+str(time + 1)+': '+str(sum))

def POWER(N, A, i):
    sum = 0
    for j in range(N):
        sum += POWERj(N, A, i, j)
        sum %= 1000000007
    return sum

def POWERj(N, A, i, j):
    sum = 0
    for k in range(N - j):
        sum += POWERjk(N, A, i, j, k)
        sum %= 1000000007
    return sum
    
def POWERjk(N, A, i, j, k):
    sum = 0
    for m in range(j + 1):
        sum += A[k + m] * pow(m + 1, i)
        sum %= 1000000007
    return sum
        
if __name__ == '__main__':
    main()