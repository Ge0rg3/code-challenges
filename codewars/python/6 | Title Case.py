#The validation checks for this were broken, so this was a bodge.
#A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.
#A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.
#title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
#title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
def title_case(*args):
    title = args[0].split()
    try: minor_words = [x.lower() for x in args[1].split()]
    except IndexError: minor_words = []
    for count, i in enumerate(title):
        if i.lower() not in minor_words or count == 0:
            title[count] = i[0].upper()+i[1:].lower()
        else:
            title[count] = i.lower()
    return " ".join(title)
    
