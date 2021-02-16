
import re


# Next Token Function
def nexttoken(file):
    delim=[b':',b';',b',',b'(',b')',b'{',b'}',b'[',b']',b'<',b'>',b'<=',b'=>',b'\'',b'\"',b'&',b'|',b'#',b'~',b'/']
    oper=[b'+',b'-',b'*',b'/',b'%',b'=',b'!',b'!=',b'^']
    key=[b'num',b'list',b'void',b'for',b'if',b'else',b'return',b'while']
    char=getchar(file)
    if(char==b'/'):
        return char
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




tslang_file = utilize_file('grammar.txt')
token = ''


def gettoken():
    global token
    if(token == ''):
        token = nexttoken(tslang_file).decode('utf-8')
    print(token)


def droptoken():
    global token
    token = ''


def word():
    global token
    x = re.match('[a-zA-Z_][a-zA-Z_1-9@$]*$', token)
    if x:
        return True
    else:
        return False


def num():
    global token
    x = re.match('[1-9]+$', token)
    if x:
        return True
    else:
        return False


def signs():
    global token
    x = re.match('[^1-9a-zA-Z_]+$', token)
    if x:
        return True
    else:
        return False



def anything1():
    global token
    if( token=='^'):
        droptoken()
        gettoken()
        if(token==';'):
            return True
        else:
            return False
    elif(word()):
        droptoken()
        gettoken()
        return anything()
    elif(signs()):
        droptoken()
        gettoken()
        return anything()
    elif(num()):
        droptoken()
        gettoken()
        return anything()
    else:
        return False


def anything():
    global token
    correct = anything1()
    if(correct==False):
        return False

    if(correct==True):
        return True

    else:
        while(correct):
            droptoken()
            gettoken()
            if(token==';'):
                return True
            anything1()
        if(correct == False):
            return False
        # else:
        #     return (True,token)
# print

def start_grammar():
    global token
    token = ''
    gettoken()
    while(word()):
        droptoken()
        gettoken()
        if(token == ':='):
            droptoken()
            gettoken()
            if(not token):
                print('error error')
                return
            correct = anything()
            print(correct)
            if correct == False:
                print('error error')
                return
            else:
                droptoken()
                gettoken()
                if(not token):
                    break
        else:
            print('error error')
            return
    if(not token):
        print("It's correct")
    else:
        print('error error')
        return


start_grammar()

tslang_file.close()


# def anything(token):
#     while(token):
#         if(anything1(token)==False):
#             print('error error')
#             return
#         token=gettoken(token)
#     return True


# def start_grammar():
#     token = ''
#     token=gettoken(token)
#     while(token):
#         token=gettoken(token)
#         if(word(token)):
#             token=droptoken()
#             token=gettoken(token)
#             if(token=='='):
#                 token=droptoken()
#                 if anything(token)==False:
#                     return
#             else:
#                 print('error error')
#         else:
#             print('error error')
#         token=gettoken(token)
#     print("It's correct")
