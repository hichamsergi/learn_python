if __name__ == '__main__':
    
    N = int(input())

    list = []

    for _ in range(N):

        comm = input()

        comm = comm.split()

        if comm[0] == "insert":

            list.insert( int(comm[1]), int(comm[2]) )
        
        elif comm[0] == "print":
            
            print(list)

        elif comm[0] == "remove":

            list.remove( int(comm[1]) )
        
        elif comm[0] == "append":

            list.append( int(comm[1]) )
        
        elif comm[0] == "sort":

            list.sort()
        
        elif comm[0] == "pop":
        
            list.pop()

        elif comm[0] == "reverse":
            
            list.reverse()