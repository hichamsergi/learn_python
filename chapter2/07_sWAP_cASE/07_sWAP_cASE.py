def swap_case(s):
        
    upp_abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    low_abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        
    swaped=""
    
    for letter in s:

        if letter.isupper():

            for l in range(len(upp_abc)):

                if upp_abc[l] == letter:

                    swaped += low_abc[l]

        elif letter.islower():

            for l in range(len(low_abc)):

                if low_abc[l] == letter:

                    swaped += upp_abc[l]
        else:
            
            swaped += letter            
        
    return swaped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)