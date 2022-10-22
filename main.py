import random
def d(rnd, b):
    if rnd==b:
        print('WIN')
    elif rnd>b:
        print('Нужно большее число')
    else:
        print('Нужно меньшее число')
rnd = random.randint(1,10)
x
b = int(input())
for i in range(1,10):
    b1 = int(input())
    print(d(rnd, b1))
    if rnd==b:
        break
all(rnd, b)


