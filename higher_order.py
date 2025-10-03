def f(x):
    return x + 2

def g(h, x):
    return h(x) * 2

print(g(f, 3))


def addx(x):
    def _(y):
        return x + y
    return _

add2 = addx(2)
add3 = addx(3)

print(add2(2), add3(3))