if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    second=[-100,-100]

    for num in range(len(arr)):

        if arr[num] < second[1] and arr[num] > second[0]:
            second[0] = arr[num]

        elif arr[num] > second[1]:
            second[0] = second[1]
            second[1] = arr[num]

    print(second[0])