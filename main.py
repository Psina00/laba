import numpy as np
import random

Ne = 0
eps = (input('Введите точность оценки вероятности ошибки декодирования:'))
const_g = (input('Введите порождающий многочлен:')[::-1])
l = (input('Введите длину сообщения:'))
N = 9/4*(int(eps)**2)
print(N)

for j in range(int(N)):
    const_r = len(str(const_g)) - 1
    var_m = random.getrandbits(int(l))
    var_m = "{0:b}".format(var_m)
    var_mx = [int(i) for i in list(str(var_m))]
    var_k = len(var_mx)

    if len(var_mx) < int(l):
        for i in range(int(l) - len(var_mx)):
            var_mx.insert(0, 0)

    var_mx = ''.join(str(x) for x in var_mx)[::-1]
    var_mx = [int(x) for x in list(str(var_mx))]
    print('mx = ', var_mx)

    if const_r > 1:
        var_xr = [int(i) for i in list(str(10 ** const_r))]
        var_xr.reverse()
    else:
        var_xr = [1]

    var_mx_xr = np.polynomial.polynomial.polymul(var_mx, var_xr)
    z1, var_cx = np.polynomial.polynomial.polydiv(var_mx_xr, [int(i) for i in list(str(const_g))])

    var_cx = abs(var_cx)
    var_cx = ''.join([str(int(i)) for i in var_cx.tolist()])
    var_cx = [int(i) for i in list(str(var_cx))]

    for i in range(len(var_cx)):
        if var_cx[i] > 1:
            var_cx[i] = 1

    var_ax = np.polynomial.polynomial.polyadd(var_mx_xr, var_cx)
    var_na = var_k + const_r
    print('cx = ', var_cx)
    print('ax = ', var_ax)
    print('n = ', var_na)

    vect_e = random.getrandbits(var_na)
    vect_e = "{0:b}".format(vect_e)
    vect_e = [int(x) for x in list(str(vect_e))]
    vect_e = [random.randint(0, 1) for x in vect_e]

    if len(vect_e) < int(var_na):
        for i in range(int(var_na) - len(vect_e)):
            vect_e.insert(0, 0)

    for i in range(len(vect_e)):
        if vect_e[i] == 1:
            err = vect_e.count(1)
            p = err / len(vect_e)
        elif all(i == 0 for i in vect_e):
            p = 0

    print('e = ', vect_e)
    print('p = ', p)
    vect_e = int(''.join(str(x) for x in vect_e), 2)
    var_ax = ''.join([str(int(i)) for i in var_ax.tolist()])[::-1]
    var_a = int(''.join(str(i) for i in var_ax), 2)
    var_b = var_a ^ vect_e
    var_b = "{0:b}".format(var_b)
    var_b = ''.join(var_b)[::-1]
    var_bx = [int(i) for i in list(str(var_b))]
    print('bx = ', var_bx)
    z2, var_sx = np.polynomial.polynomial.polydiv(var_bx, [int(i) for i in list(str(const_g))])
    var_sx = abs(var_sx)
    var_sx = ''.join([str(int(i)) for i in var_sx.tolist()])[::-1]
    var_sx = [int(i) for i in list(str(var_sx))]

    print('sx = ', var_sx)

    if all(x == 0 for x in var_sx):
        var_ERR = 0
        print('Нет ошибок: 0')
    else:
        var_ERR = 1
        print("Обнаружены ошибки: 1")

    if (vect_e is not None) & (var_ERR == 0):
        Ne += 1
print('Вероятность ошибки декодирования = ', Ne/N)
