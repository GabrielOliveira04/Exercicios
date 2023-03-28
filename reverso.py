def reverso(numero):
    reverso = 0
    while numero > 0:
        digito = numero % 10
        reverso = (reverso * 10) + digito
        numero = numero // 10
    return reverso

# programa principal
numero = int(input("Digite um número inteiro: "))
print("O reverso do número {} é {}.".format(numero, reverso(numero)))
