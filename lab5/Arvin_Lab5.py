from os.path import exists

# this function determines whether the file is valid or not
def main():
    while True:
        file_name = input("Enter the name of an input file: ")
        
        if not exists(file_name):
            print("Oops... An error occurred - Try again")
            continue
        
        # this block reads the information the file has, then closes it
        with open(file_name,'r',encoding='utf_8') as f:
            identifiers = f.readlines()
            words = {}
            line_no = 0
            for identifier in identifiers:   
                identifier_strip = identifier.strip()
                line_no = line_no + 1
                
                if not valid_identifier(identifier_strip):
                    continue
                    
                if identifier_strip in words:
                    words[identifier_strip].append(line_no)
                else:
                    words[identifier_strip] = [line_no]
            
        f.close()
        for w in words:
            print(w, ": ", words[w])
        
        # break from the main loop
        break

# this function gets a string and returns a boolean
# true, if identifier is valid identifier
# false, if identifier is not a valid identifier
def valid_identifier(identifier):
    for ch in identifier:
        result = str.isalpha(ch) or str.isdigit(ch) or '_' in ch
        if not result:
            return False

    return True

if __name__ == "__main__":
    main()

# test output
# ---------------------------------------------------
# Enter the name of an input file: test1
# Oops... An error occurred - Try again
# Enter the name of an input file: test2
# Oops... An error occurred - Try again
# Enter the name of an input file: t5.dat
# apple :  [1, 11]
# 1 :  [2, 3]
# ball :  [4, 19]
# art :  [5]
# dog :  [6]
# pen :  [8, 21]
# rat :  [9]
# 4 :  [10]
# carrot :  [13]
# orange :  [15]
# ant :  [16, 17, 18]
# stick :  [20]
# _ :  [22]
# goodbye :  [25]
# Enter the name of an input file: