def fun_strings(string1, string2):
    if ( type(string1)!=str or type(string2)!=str):
        return 0 
    else:     
        if string1==string2:
            return 1
        else: 
            if (len(str(string1))!=len(str(string2)) and string2=='learn'):
                return 3
            else:               
                if len(str(string1))>len(str(string2)):
                    return 2
print('1: ', fun_strings(5, 'false'))
print('2: ', fun_strings('python', 'Python'))
print('3: ', fun_strings('Learn', 'Learn'))
print('4: ', fun_strings('Python', 'learn'))