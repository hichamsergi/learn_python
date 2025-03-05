if __name__ == '__main__':
    N = int(input())

    final=[]

    # Entramos datos 'N':
    for _ in range(N):
        
        command = input().split()

        if command[0] == "insert":
            final.insert(int(command[1]), int(command[2]))
        
        elif command[0] == "remove":
            final.remove(int(command[1]))

        elif command[0] == "append":
            final.append(int(command[1]))

        elif command[0] == "sort":
            final.sort()

        elif command[0] == "pop":
            final.pop()

        elif command[0] == "reverse":
            final.reverse()

        elif command[0] == "print":
            print(final)