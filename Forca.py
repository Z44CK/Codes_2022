import random
import string

from palavra import palavras


def palavra_randomica(palavras):
    palavra = random.choice(palavras)  # escolhe uma palavra randomica da lista
    while '_' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)

    return palavra.upper()  # sempre retornar a palavra em maiusculo, pois na forca não tem diferente em maisuculo e
    # minusculo


def jogo():
    palavra_secreta = palavra_randomica(palavras)
    letras_na_palavra = set(palavra_secreta)  # letras na palavra - aqui a palavra_secreta ao invés de palavras
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()  # o que o usuario já adivinhou
    vidas = 5

    while len(letras_na_palavra) > 0 and vidas > 0:
        print('Você ja usou essas letras: ', ' '.join(letras_usadas))
        print('Você possui', vidas, 'vidas restante')
        lista_palavras = [letra if letra in letras_usadas else '_' for letra in
                          palavra_secreta]  # aqui a palavra_secreta ao invés de palavras
        print('Palavra atual: ', ' '.join(lista_palavras))

        # pegando entrada do usario
        letra_digitada = input('Informe uma letra: ').upper()
        if letra_digitada in alfabeto - letras_usadas:
            letras_usadas.add(letra_digitada)
            if letra_digitada in letras_na_palavra:  # aqui é letra_digitada ao invés de letras_usadas
                letras_na_palavra.remove(letra_digitada)
            else:
                vidas = vidas - 1  # só subtrai a vida se a pessoa errou

        elif letra_digitada in letras_usadas:
            print('Você já usou essa letra, tente novamente!!')
        else:
            print('Charactere invalido, tente novamente!!')

    # chega aqui quando len(letras_na_palavra) == 0
    if vidas == 0:
        print(f'FIM DE JOGO!! A palavra era "{palavra_secreta}"')
    else:
        print(f'VENCEDOR!! A palavra é "{palavra_secreta}"')


jogo()
