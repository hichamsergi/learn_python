if __name__ == '__main__':
    n = int(input())
    s_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        s_marks[name] = scores
    
    q_name = input()
    
    total = sum(s_marks.get(q_name)) / len(s_marks.get(q_name))

    print('%.2f' % total)
    
