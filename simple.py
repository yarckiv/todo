def maximum(*args):
    z = list(*args)
    x = z[0]
    for a in z:
        if x < a:
            x = a
    print(x)


def minimum(*args):
    z = list(*args)
    a = z[0]
    for x in z:
        if x < a:
            a = x
    print(a)


def sets(*args):
    x = list(*args)
    d = [x[0]]
    for a in x:
       if a in d:
           continue
       else:
           d.append(a)
    print(d)


def counter(start, step):
    start = start
    step = step
    while step:
        yield start
        start = start + step
a = [1, 2, 3]
d = [4, 5, 6]
x = [1,2,3,4,5,5,5,8,88,9,6,7,22]


def ziper(*args):
    z = []
    for f in args:
        for x in f:
            z.append(x)

print(list(ziper(a,d,x)))
print(list(zip(a,d,x)))




