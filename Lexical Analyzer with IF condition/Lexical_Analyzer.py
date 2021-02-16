import re


# Next Token Function
def nexttoken(file):
    delim=[b':',b';',b',',b'(',b')',b'{',b'}',b'[',b']',b'<',b'>',b'<=',b'=>',b'\'',b'\"',b'&',b'|',b'#']
    oper=[b'+',b'-',b'*',b'/',b'%',b'=',b'!',b'!=',b'^']
    key=[b'num',b'list',b'void',b'for',b'if',b'else',b'return',b'while']
    char=getchar(file)
    while(char==b' ' or char==b'\n' or char==b'\r' or char==b'\t'):
        char=getchar(file)
    if not char:
        return char
    x = re.findall(b'[1-9]', char)     
    if x:
        while True:
            next_char=getchar(file)
            y = re.findall(b'[1-9]x*', next_char) 

            if next_char in delim or next_char in oper :
                ungetchar(file)
                break
            elif next_char==b' ' or next_char==b'\n' or next_char==b'\r' or next_char==b'\t':
                break
            elif not y:
                break    
            elif not next_char:
                break
            char=char+next_char
        return char    
        
    while(char==b' ' or char==b'\n' or char==b'\r' or char==b'\t'):
        char=getchar(file)
    if char == b'/' :
        char=getchar(file) 
        if char == b'*':
            while True :
                char=getchar(file) 
                if char==b'*':
                    char=getchar(file) 
                    if char==b'/':
                        break
        else:
            ungetchar(file)



    if char in delim:
        next_char=getchar(file)
        if not next_char:
            return char
        if(next_char==b'=' or next_char==b'>'):
            char=char+next_char
            return char   
        else:
            ungetchar(file)
            return char    

    if char in oper:
        next_char=getchar(file)
        if not next_char:
            return char
        if(next_char==b'='):
            char=char+next_char
            return char
        else:
            ungetchar(file)
            return char    


    while True:
        next_char=getchar(file)
        if next_char in delim or next_char in oper :
            ungetchar(file)
            break
        if next_char==b' ' or next_char==b'\n' or next_char==b'\r' or next_char==b'\t':
            break
        if not next_char:
            break
        char=char+next_char

    # x = re.findall(b'[1-9@$][a-zA-Z_]x*', char)                    
    # if x:
    #     return "error" 
    # x = re.findall(b'[@$]', char)                    
    # if x:
    #     return "error"    

    if char in key:
        return char   

    x = re.findall(b'[a-zA-Z1-9_]', char)                    
    if x:
        return char   
# End Next Token Function



#Getchar Function
def getchar(file):
    return file.read(1)



# UnGetchar Function
def ungetchar(file):
     file.seek(-1,1)


def utilize_file(file):
    return open(file,'rb')


# If Program run directly
if __name__ == "__main__":

    tslang_file = utilize_file('tslang.txt')
    while (True):
        token=[]
        str_tok=nexttoken(tslang_file)
        if(str_tok =="error"):
            print("error")
            tslang_file.close()
            break

        elif not str_tok :
            tslang_file.close()
            break

        else :
            token.append(str_tok.decode('utf-8'))
            print(str_tok.decode('utf-8'))



