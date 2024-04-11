import methods.RungeKutta_4 as RK4
import methods.RungeKutta_2 as RK2
import methods.Euler as Euler  


def f(x, y):
    return (2 * y - 2) / x

def main():
    x0 = 1
    y0 = 3
    valor = 2
    h = 0.5

    print("Euler: ", Euler.method(x0, y0, f, valor, h))
    print("Runge-Kutta 2: ", RK2.method(x0, y0, f, valor, h))
    print("Runge-Kutta 4: ", RK4.method(x0, y0, f, valor, h))
    

if __name__ == "__main__":
    main()

