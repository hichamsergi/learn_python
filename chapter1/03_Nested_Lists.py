if __name__ == '__main__':
    records = []
    lowest = 100
    s_lowest = 100
    list_names = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        if score < lowest:
            s_lowest = lowest
            lowest = score
            
        elif score < s_lowest and score > lowest:
            s_lowest = score
        
        records.append([name, score])

    for name_record in records:
        if name_record[1] == s_lowest:
            list_names.append(name_record[0])

    list_names = sorted(list_names)

    for f_name in list_names:
        print(f_name)