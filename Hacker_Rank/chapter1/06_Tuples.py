if __name__ == '__main__':

    n = int(input())

    integer_tuple = tuple(map(int, input().split()))


    print(abs(hash(integer_tuple)))
