if __name__ == '__main__':

    max_low=float('inf')
    sec_low=float('inf')

    records=[]
   
    for _ in range(int(input())):
        name = input()
        score = float(input())

        #Si la puntuación es mas baja que la mas baja:
        if score < max_low:
            sec_low = max_low
            max_low = score
        #Si la puntuación es la segunda mas baja:
        elif score < sec_low and score != max_low:
            sec_low = score
        
        #Añadimos el record a records
        records.append([name,score])

    #Localizar y mostrar los nombres que coinciden con la segunda puntuación mas baja:

    names=[rec[0] for rec in records if rec[1] == sec_low]
    names.sort()

    for rec in names:
        print(rec)