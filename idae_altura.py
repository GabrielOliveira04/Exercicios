idades = []
alturas = []

#lê a idade e a altura ded cada pessoa e armazena nos vetores

for i in range(5):
    idade=int(input("Digite a idade da pessoa {}: ".format(i+1)))
    altura = float(input("Digite a altura dda pessoa {} :".format(i+1)))
    idades.append(idade)
    alturas.append(altura)

#imprimir as idaeds e alturas na ordem inversa
print("\nIdades na ordem inversa: ")

for idade in reversed(idades):
    print(idade)


for altura in reversed(alturas)   :
    print(altura)