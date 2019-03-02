# -*- coding: utf-8 -*-

def main():
    T = int(input())
    for _ in range(T):
        A, B = [int(s) for s in input().split()]
        N = int(input())
        while A < B:
            mid = (A + B + 1) // 2
            print(mid, flush=True)
            Answer = input()
            if Answer == 'CORRECT':
                break
            elif Answer == 'TOO_SMALL':
                A = mid
            elif Answer == 'TOO_BIG':
                B = mid - 1
            elif Answer == 'WRONG_ANSWER':
                assert False

if __name__ == '__main__':
    main()