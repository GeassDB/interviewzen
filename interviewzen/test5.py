class C(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __hash__(self):
        return hash(self.b)

a = C(1, 'a')
b = C(1, 'a')
c = C(1, 'b')

l = [a, b, c]

r = {}

for i in l:
    if i not in r:
        r[i] = 1
    else:
        r[i] += 1

for i in r:
    print(r[i])

if a == b:
    print('eq')

if a is b:
    print('is')
