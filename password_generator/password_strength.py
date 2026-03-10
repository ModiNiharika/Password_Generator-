import string
def check_strength(password):

    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbols = any(c in string.punctuation for c in password)

    score = 0
    
    if(length>=8):
        score = score + 1
    if(has_upper and has_lower):
        score = score + 1
    if(has_digit):
        score = score + 1
    if(has_symbols):
        score = score + 1

    if(score==1):
        return 'Weak |  █░░░'
    elif(score==2):
        return 'Medium |  ██░░'
    elif(score>=3):
        return 'Strong |  ████'
    else : 
        return 'Try again'
    