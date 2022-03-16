from math import pi, sqrt

def problema1():

    V, X, Y = [int(d) for d in input().split()]
    X = X/10000
    Y = Y/10000
    
    def raio():
        return ((V/(2*pi))**1/3)

    def altura():
        return ((4*V/pi)**1/3)

    def area():
        return ((2*pi*raio() * altura()) + 2*(pi*(raio()**2)))

    def custo():
        return (X * (4*pi*raio()) + Y * 2*pi*raio() * altura())

    def saida():
        print(f"{raio():.2f}, {altura():.2f}, {area():.2f}, {custo():.2f}")
        return
    
    saida()
    return

def problema2():

    X, Y = [int(d) for d in input().split()]

    def funcao(x):
        if x > 0:
            return (sqrt(40**2 + (100-x)**2) / X) + x / Y
        

    def derivada():
        # Retorna o ponto em que f''(x) = 0
        a = X**2 - Y**2
        b = (X**2 * -200) - (Y**2 * -200)
        c =  (X**2 * 40**2) + (X**2 * 100**2) - (Y**2 * 100**2)

        D = (b**2 - 4*a*c)
        x1 = ((-b + D**(1/2)) / (2*a))
        x2 = ((-b - D**(1/2)) / (2*a))

        lista = (x1, x2)
        return lista

    def pontoMinimo():
        x1, x2 = derivada()
        if funcao(x1-1) > funcao(x1) and funcao(x1+1) > funcao(x1): return x1
        else: return x2

    def distanciaTotal():
        ilhaestacao = sqrt(40**2 + pontoMinimo()**2)
        total = ilhaestacao + (100 - pontoMinimo())
        return total

    def saida():
        print(f"Distância da estação até a cidade: {100 - pontoMinimo():.3f}km")
        print(f"Distância total: {distanciaTotal():.3f}km")

    saida()
    return

problema1()
problema2()