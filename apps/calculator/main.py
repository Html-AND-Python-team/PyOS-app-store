def run(ruta, args):

    if len(args) < 3:

        print("Uso: calculator <num1> <op> <num2>")

        return


    try:

        a = float(args[0])
        op = args[1]
        b = float(args[2])


        if op == "+":

            print(a + b)


        elif op == "-":

            print(a - b)


        elif op == "*":

            print(a * b)


        elif op == "/":

            if b == 0:

                print("Error: división por cero")

            else:

                print(a / b)


        else:

            print("Operador no válido (+ - * /)")


    except ValueError:

        print("Error: números inválidos")
