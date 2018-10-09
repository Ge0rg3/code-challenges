#Your task is to write a function that takes a string and return a new string with all vowels removed.
#For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
vowels = ["a","e","i","o","u"]
def disemvowel(string):
    nstring = ""
    for i in string:
        if i.lower() not in vowels:
            nstring += (str(i))
    return nstring
