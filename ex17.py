n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1+n2)/2
if (media >= 7):
    print("Sua média foi: ", media)
    print("Você foi aprovado!")
elif media == 10:
    print("Sua média foi: ", media)
    print("Aprovado com Distinção!")
else: 
    print("Sua média foi: ", media)
    print("Reprovado!")