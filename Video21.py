# Mayor de 3 numeros
num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))
num3 = int(input("Digite otro numero: "))

if num1>=num2 and num1>=num3:
    print(f"El numero mayor es {num1}")
elif num2>=num1 and num2>=num3:
    print(f"El numero es mayor es {num2}") 
elif num3>=num1 and num3>=num2:
    print(f"El numero mayor es {num3}")   