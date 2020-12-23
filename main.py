import numpy as np
import matplotlib.pyplot as plt
import random

def cutZeroes(x):
    if (x[len(x) - 1] == 0) & (len(x) > 1):
        x = x[:-1]
        return cutZeroes(x)
    else:
        return x

def addZeroes(x, y):
    if (len(x) < len(y)):
        x.insert(0, 0)
        return addZeroes(x, y)
    else:
        return x

def subs(el, sub):
    x = [0 for i in range(len(el))]
    for i, idx in enumerate(el):
        x[len(x) - i - 1] = abs(abs(el[len(x) - i - 1]) - abs(sub[len(x) - i - 1]))
    return x

def mulDivision(el, div):
    mul = cutZeroes(div)
    while len(el) >= len(mul):
        tempDivisor = mul[:]
        tempDivisor = addZeroes(tempDivisor, el)
        el = subs(el, tempDivisor)
        el = cutZeroes(el)
    return el

Ne = 0
eps = float(input('Введите точность оценки вероятности ошибки декодирования: '))
const_g = (input('Введите порождающий многочлен: ')[::-1])
const_r = len(str(const_g)) - 1
const_g = [int(i) for i in list(str(const_g))]
l = (input('Введите длину сообщения: '))
N = 9/(4*((eps)**2))
print(N)

def coder():
    var_m = random.getrandbits(int(l))
    var_m = "{0:b}".format(var_m)
    var_mx = [int(i) for i in list(str(var_m))][::-1]
    var_k = len(var_mx)

    if len(var_mx) < int(l):
        for i in range(int(l) - len(var_mx)):
            var_mx.insert(0, 0)

    var_mx = ''.join([str(x) for x in var_mx])

    if const_r > 1:
        var_xr = [int(i) for i in list(str(10 ** const_r))]
        var_xr.reverse()
    else:
        var_xr = [1]
    var_xr = ''.join([str(x) for x in var_xr])

    var_mx_xr = int(var_mx, 2) * int(var_xr, 2)
    var_mx_xr = "{0:b}".format(var_mx_xr)
    var_mx_xr = [int(i) for i in list(str(var_mx_xr))]
    var_cx = mulDivision(var_mx_xr, const_g)
    var_mx_xr = ''.join([str(x) for x in var_mx_xr])[::-1]
    var_cx = ''.join([str(x) for x in var_cx])[::-1]
    var_ax = int(var_mx_xr, 2) + int(var_cx, 2)

    var_na = var_k + const_r
    return[var_ax, var_na]

def decoder(var_ax, var_na, ver):
    vect_e = np.random.default_rng().binomial(1, float(ver), var_na).tolist()
    vect_e = int(''.join(str(x) for x in vect_e), 2)
    var_b = var_ax ^ vect_e
    var_b = "{0:b}".format(var_b)
    var_b = ''.join(var_b)[::-1]
    var_bx = [int(i) for i in list(str(var_b))]
    var_sx = mulDivision(var_bx, const_g)
    return[vect_e, var_sx]

def func(ver, Ne):
    for j in range(int(N)):
        cd = coder()
        dcd = decoder(cd[0], cd[1], ver)

        if all(x == 0 for x in dcd[1]):
            var_ERR = 0
        else:
            var_ERR = 1

        if (dcd[0] != 0) & (var_ERR == 0):
            Ne += 1

    Pe = Ne/N
    return(Pe)


p = [i/100 for i in list(range(100))]
Pe_arr = []
for i in range(100):
    Pe_arr.append(func(p[i], Ne))
print(Pe_arr)

plt.plot(p, Pe_arr)
plt.show()
