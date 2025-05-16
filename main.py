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


    pass


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
    elif lado1 != lado2 and lado3 != lado1:
        print("Escaleno")
    


def q6():
    intervalo = 4
    primeiraDose = 2000

    while intervalo == 1:
        print(primeiraDose + 1)
        primeiraDose += 1
    pass


def q7():
      numero = int(input("Digite um numero "))  
while True:

    if numero // 1 or numero // numero:
        print(numero)
    if numero < 0:
        print("Numero Negativo")
        break
        


    pass

def q8():
    pass

def q9():
    pass

def q10():
    pass

if __name__ == "__main__":
    q5()
