def plus(name,age):

    print(name)
    print(age)

    if len(name) != len(age):
        print("Whoops")
        return(None)
    else:
        return (dict(zip(name,age)))
