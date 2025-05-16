def q1():
    """
    Escreva um programa que solicite ao usuário um número e
    verifique se ele é par ou ímpar. Imprima uma mensagem informando o 
    resultado.
    """
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("O número é Par")
    else:
        print("O número é Ímpar")  
    



def q2():
    """
    Dada a string use o operador de fatiamento para imprimir somente a metade final
    Para 'abcdef, imprima: 'def'
    Para 'texto', imprima 'to'

    """
    import math

    texto = input("Digite um texto: ")
    tamanho = len(texto)
    meio = math.ceil(tamanho / 2)
    print(texto[meio:tamanho])


def q3():
    """
    Leia um número da entrada e imprima todos os 10 primeiros múltiplos dele na mesma linha
    """
    numero = int(input("Digite um número: "))


    for i in range(1, 10):
        print(numero * i)





def q4():
    """
    Escreva um programa que solicite ao usuário para digitar seu nome em letras
    minúsculas e, em seguida, imprima o nome com a primeira letra em maiúscula. Você
    não deve usar o método str.capitalize(). Preposições não devem ser iniadas com maiúsculo
    Exemplo: 
     - romulo junior - Romulo Junior
     - ze da manga - Ze da Manga
    """

    nome = str(input("Digite o seu nome: "))
    maisculo = nome.capitalize()
    print(maisculo)
    

def q5():
    """
    Verificação de Triângulo: Peça ao usuário o comprimento de três lados em uma única entrada
    e verifique se eles podem formar um triângulo. 
    Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.
    Exemplo:
        333: equilátero
        322: isosceles
        234: escaleno
    """
    lado1 = int(input("Digite lado 1: "))
    lado2 = int(input("Digite lado 2: "))
    lado3 = int(input("Digite lado 3: "))

    if lado1 == lado2 and lado3 == lado1:
        print("Equilátero")
    elif lado1 == lado2 and lado1 != lado3:
        print("Isosceles")
    elif lado1 == lado3 and lado1 != lado2:
        print("Isosceles")
    elif lado1 == 0 and lado2 == 0 and lado3 == 0:
        print("Números neutros. Não possui lados ")
    elif lado1 != lado2 and lado3 != lado1:
        print("Escaleno")

    


def q6():
    intervalo = 4
    primeiraDose = 2000

    for i in range(1, 4):
        print(primeiraDose + i * intervalo)



def q7():
       
    SequenciaNum = int(input("Digite um número: "))

    if SequenciaNum > 1 and SequenciaNum % SequenciaNum == 0:
        print("É número Primo")
    else:
        print("Não é número Primo")



def q8():
    quantidade = 0
quantiaDoada = 0
while True:
    doar = float(input("Digite a quantia que você quer doar: "))
    if doar < 0:
        print(f"{quantiaDoada:.2f}")
        if quantidade > 0:

            print(f'{quantiaDoada / quantidade:.2f}')
        break
    else:
        quantiaDoada += doar
        quantidade += 1
    pass

def q9():
    
    pass

def q10():
    graus = float(input("Digite a temperatura: "))
Temperatura = str(input("c, f, k "))


if Temperatura == "C":
    print(graus * 9/5 + 32)
    print(graus + 273,15 )
elif Temperatura == "f":
    print(graus * 5/9)
    print(graus * 1,8 - 459,67)
elif Temperatura == "k":
    print(graus + 273,15 )
    print(graus *  9/5 + 32)
else:
    print("Inválido")
    pass

if __name__ == "__main__":
    q5()
