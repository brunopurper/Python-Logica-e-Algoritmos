peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

def calcular_imc(peso, altura):

    imc = peso / altura ** 2
    imc = round(imc, 2)
    return imc

if calcular_imc(peso, altura) > 25:
    print("Você está gordinho hein!")
else:
    print("ta bem na fita champs!")

