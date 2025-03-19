if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    A=[]
    A.extend(arr)
    A.sort()
    print(A[-2])
    