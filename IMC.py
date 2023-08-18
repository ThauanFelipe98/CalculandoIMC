peso = float(input("Digite aqui o seu peso: "))
altura = float(input("Digite aqui a sua altura: "))
imc = peso / (altura * altura)
print(imc)

if(imc < 25):
    print("Peso Normal!")
elif(imc < 30):
    print("Sobrepeso!")
elif(imc < 35):
    print("Obesidade!")
else:
    print("Obesidade Grave!")    