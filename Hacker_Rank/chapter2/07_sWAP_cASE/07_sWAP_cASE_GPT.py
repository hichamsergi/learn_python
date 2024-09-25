def swap_case(s):
                
    swaped=""
    
    for letter in s:

        if letter.isupper():

            swaped += letter.lower()

        elif letter.islower():

            swaped += letter.upper()

        else:
            
            swaped += letter            
        
    return swaped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)