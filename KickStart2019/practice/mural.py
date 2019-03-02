# -*- coding: utf-8 -*-

def main():
    T = int(input())
    for time in range(T):
        N = int(input())
        string_of_score = input()
        scores = [int(s) for s in string_of_score]
        n = (N + 1) // 2
        value = maxValue = sum(scores[:n])
        for i in range(N - n):
            value -= scores[i]
            value += scores[i + n]
            if value > maxValue:
                maxValue = value
        print('Case #'+str(time+1)+': '+str(maxValue))
              
if __name__ == '__main__':
    main()