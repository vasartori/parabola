from drawille import Canvas
from math import sqrt, radians, sin


def vertice(a, b, c):
    x = ((-b) / 2 * a)
    y = (a * (x ** 2) + (b * x) + c)
    return x, y


def delta(a, b, c):
    return (b ** 2) - 4 * (a * c)


def raiz_real(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        raise Exception('Nao posso trabalhar com numeros imaginarios')
    else:
        x1 = ((-b + sqrt(d)) / 2 * a)
        x2 = ((-b - sqrt(d)) / 2 * a)
        return x1, x2


def printa_parabola(lado):
    s = Canvas()
    s.clear()
    for x in range(0, 180):
        s.set(x / 4, lado + sin(radians(x)) * lado)
    return s.frame()


def resultados():
    i = inputs()
    a = i[0]
    b = i[1]
    c = i[2]
    p = i[3]
    print("A parabola ficará assim:")
    print(printa_parabola(p))
    print("===== V e r t i c e =====")
    v = vertice(a, b, c)
    print("X: {} | Y: {}".format(v[0], v[1]))
    print("===== R a i z e s  R e a i s =====")
    r = raiz_real(a, b, c)
    print("X: 0 | Y: {}".format(c))
    print("X1: {} | X2: {}".format(r[0], r[1]))
    print("===== E i x o  d e  s i m e t r i a =====")
    print("Y: {} | X: {}".format(float(c), v[0] * 2))


def inputs():
    print("Função de segundo grau")
    try:
        a = int(input("Entre com o valor de A:"))
    except BaseException:
        raise Exception("A deve ser inteiro")
    else:
        if a == 0:
            raise Exception("Nao posso fazer os calculos com A valendo zero.")
    try:
        b = int(input("Entre com o valor de B:"))
    except BaseException:
        raise Exception("B deve ser inteiro")
    try:
        c = int(input("Entre com o valor de C:"))
    except BaseException:
        raise Exception("C deve ser inteiro")

    if a > 0:
        p = 30
    else:
        p = -30

    return a, b, c, p


if __name__ == '__main__':
    try:
        resultados()
    except Exception as e:
        print(e)
