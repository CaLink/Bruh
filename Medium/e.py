def Whe(a,b,c):

    #if c == a or c == b:
    #   return "Here"

    if a>=b:
        if c>a:
            return "Right"

        else:
            if c<b:
                return "Left"
            else:
                return "Here"

    else:
        if c>b:
            return "Right"
        else:
            if c<a:
                return "Left"
            else:
                return "Here"

