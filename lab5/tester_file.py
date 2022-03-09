
with open('t5.dat','r',encoding='utf_8') as f:
    read_data = f.read()

def valid_identifier(identifier):
    result = False
    
    for ch in identifier:
        
        result = str.isalpha(ch) or str.isdigit(ch) or '_' in ch
        
        #if statment skips the invalid characters
        if result == False:
            continue 

        print(ch)
        print(result)

        return result
        

valid_identifier(read_data)

f.close()

result = False

txt = read_data
words = txt.split()
for x,t in enumerate(words):
    return (x+1, words)

print(x(5))