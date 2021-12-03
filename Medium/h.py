def simp(a):
    first = 2
    while a % first!=0:
        first+=1
    if first == a:
        return "Sigma"
    else:
        return "Simp"
