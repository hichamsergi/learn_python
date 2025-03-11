if __name__ == '__main__':
    
    n = int(input())
    integer_list = tuple([int(i) for i in input().split()])
    print(hash(integer_list))
