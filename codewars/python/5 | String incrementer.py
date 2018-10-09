#Your job is to write a function which increments a string, to create a new string. If the string already ends with a number, the number should be incremented by 1. If the string does not end with a number the number 1 should be appended to the new string.
#foo -> foo1
#foo0042 -> foo0043
#foo099 -> foo100
def increment_string(strng):
    intst = ""
    for i in strng[::-1]:
        try: intst = str(int(i))+intst
        except:
            if intst == "": strng +="1"
            break
    intleng = len(intst)
    if strng == "": return "1"
    strng = strng[:len(strng)-intleng]
    if intst != "":
        intst = int(intst)+1
        zeros = "0"*(int(intleng)-len(str(intst)))
        return strng+zeros+str(intst)
    else:
        return strng+intst
