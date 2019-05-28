#!/usr/bin/env python

from unicodedata import normalize
import re

template = {
    'A': 1, 'B': 2, 'C': 0, 'D': 1, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I':0,
    'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 1, 'P': 1, 'Q': 1, 'R': 1,
    'S': 0, 'T': 0, 'U': 0, 'V': 0, 'X': 0, 'Z': 0, 'Y': 0, 'W': 0,

    'a': 1, 'b': 1, 'c': 0, 'd': 1, 'e': 1, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
    'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 1, 'p': 1, 'q': 1, 'r': 0,
    's': 0, 't': 0, 'u': 0, 'v': 0, 'x': 0, 'z': 0, 'y': 0, 'w': 0
}
def remove_acentos(word):
    '''
    Função que remove acentos e cedilhas de uma string
    '''
    return normalize('NFKD', word).encode('ASCII', 'ignore').decode('ASCII')

def checa_buracos(inputword):
    '''
    Função que checa quantos buracos tem uma string
    '''
    word = str(inputword)
    if len(word) == 0:
        return 0
    else:
        try:
            palavra = remove_acentos(word)
            buracos = 0
            for letra in palavra:
                buracos += template[letra]
            return buracos
        except KeyError:
            raise KeyError('A palavra inserida deve conter apenas letras')
        return buracos
if __name__ == "__main__":
    palavra = str(input("Digite uma palavra (apenas letras): "))
    buracos = checa_buracos(palavra)
    print(palavra,"tem ", buracos, "buracos.")
