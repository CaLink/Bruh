def perfect(a):
    sum = 0

    for i in range(1,int(a/2)+1):
        if a%i == 0:
            sum+=i
            print(i)
    return sum==a


"""
def is_perfect(n):
        s = [j for j in range(1, n // 2 + 1) if not n % j]
        return sum(s) == n
"""    