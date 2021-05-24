num1=int(input("Ingrese primer numero:"))
num2=int(input("Ingrese segundo numero:"))
num3=int(input("Ingrese tercer numero:"))       

if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)