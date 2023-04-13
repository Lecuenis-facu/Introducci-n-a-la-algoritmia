### Al ingresar 3 lados de un triángulo, devuelva que tipo es

lado1 = int(input("ingrese lado 1"))
lado2 = int(input("ingrese lado 2"))
lado3 = int(input("ingrese lado 3"))

if lado1 >= lado2 and lado1 >= lado3:
    if lado1 < (lado2 + lado3):
        print("Es un triángulo")
        if lado2 == lado3 and lado2 == lado1:
            print("Triángulo equilatero")
        if lado2 == lado3 and lado2 != lado1:
            print("Triángulo isosceles")
        if lado2 != lado1 and lado2 != lado3:
            print("Triángulo escaleno")
    else:
        print("No es un triángulo")
            
if lado2 >= lado1 and lado2 >= lado3:
    if lado2 < (lado1 + lado3):
        print("Es un triángulo")
        if lado1 == lado3 and lado2 == lado1:
            print("Triángulo equilatero")
        if lado1 == lado3 and lado2 != lado1:
            print("Triángulo isosceles")
        if lado2 != lado1 and lado2 != lado3:
            print("Triángulo escaleno")
    else:
        print("No es un triángulo")
            
if lado3 >= lado2 and lado3 >= lado1:
    if lado3 < (lado2 + lado1):
        print("Es un triángulo")
        if lado2 == lado1 and lado2 == lado3:
            print("Triángulo equilatero")
        if lado2 == lado1 and lado2 != lado3:
            print("Triángulo isosceles")
        if lado2 != lado1 and lado2 != lado3:
            print("Triángulo escaleno")
    else:
        print("No es un triángulo")