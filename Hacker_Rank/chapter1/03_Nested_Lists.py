if __name__ == '__main__':

    max_low=float('inf')
    sec_low=float('inf')

    records=[]
   
    for _ in range(int(input())):
        name = input()
        score = float(input())

        if score < max_low:
            sec_low = max_low
            max_low = score

        elif score < sec_low and score != max_low:
            sec_low = score
        
        records.append([name,score])


    names=[rec[0] for rec in records if rec[1] == sec_low]
    names.sort()

    for rec in names:
        print(rec)