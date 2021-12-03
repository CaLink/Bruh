def test(a):
        print(a)
        def add(b):
                nonlocal a
                a += 1
                return a+b
        return add
