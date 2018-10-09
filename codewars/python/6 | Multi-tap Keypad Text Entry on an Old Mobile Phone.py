#Prior to having fancy iPhones, teenagers would wear out their thumbs sending SMS messages on candybar-shaped feature phones with 3x4 numeric keypads.
#------- ------- -------
#|     | | ABC | | DEF |
#|  1  | |  2  | |  3  |
#------- ------- -------
#------- ------- -------
#| GHI | | JKL | | MNO |
#|  4  | |  5  | |  6  |
#------- ------- -------
#------- ------- -------
#|PQRS | | TUV | | WXYZ|
#|  7  | |  8  | |  9  |
#------- ------- -------
#------- ------- -------
#|     | |space| |     |
#|  *  | |  0  | |  #  |
#------- ------- -------
#For example, to type a letter "R" you would press the 7 key three times (as the screen display for the current character cycles through P->Q->R->S->7). A character is "locked in" once the user presses a different key or pauses for a short period of time (thus, no extra button presses are required beyond what is needed for each letter individually). The zero key handles spaces, with one press of the key producing a space and two presses producing a zero.
#For this assignment, write a module that can calculate the amount of button presses required for any phrase. Punctuation can be ignored for this exercise. Likewise, you can assume the phone doesn't distinguish between upper/lowercase characters (but you should allow your module to accept input in either for convenience).
def presses(phrase):
    presses = 0
    phrase = phrase.lower()
    for letter in phrase:
        if letter in '1*#adgjmptw ': presses+= 1
        elif letter.lower() in '0behknqux': presses+= 2
        elif letter.lower() in 'cfilorvy': presses+= 3
        elif letter.lower() in '234568sz': presses+= 4
        elif letter.lower() in '79': presses+= 5
    return presses
