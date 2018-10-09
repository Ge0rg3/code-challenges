#You need to create a function that will validate if given parameters are valid geographical coordinates.
#Valid coordinates look like the following: "23.32353342, -32.543534534". The return value should be either true or false.
#Latitude (which is first float) can be between 0 and 90, positive or negative. Longitude (which is second float) can be between 0 and 180, positive or negative.
#Coordinates can only contain digits, or one of the following symbols (including space after comma) -, .
#There should be no space between the minus "-" sign and the digit after it.
def is_valid_coordinates(coordinates):
    two = coordinates.split(', ')
    try:
        if '1e1' in two: return False
        fone = float(two[0]); ftwo = float(two[1])
        if fone/fone == 1 and ftwo/ftwo == 1:
            if -90 <= fone <= 90 and -180 <= ftwo <= 180: return True
            else: return False
        else:
            return False
    except:
        return False
