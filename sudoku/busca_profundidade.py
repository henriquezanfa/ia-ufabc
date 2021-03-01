#!/usr/bin/env python

import sys
from sudoku import Sudoku
import time
import utils


def busca_profundidade(entrada, sudoku, profundidade):
    if profundidade > 81:
        return
    if sudoku.atingiu_obj(entrada):
        return entrada

    for a in sudoku.expand_nodes(entrada):
        resultado = busca_profundidade(a, sudoku, profundidade + 1)
        if sudoku.atingiu_obj(resultado):
            return resultado

    return


def main():
    entradas = utils.le_entrada(sys.argv[1])
    s_problema = Sudoku(entradas)

    start = time.time()
    respostas = []
    for jogos in entradas:
        entrata_string = ""
        for linha in jogos:
            for e in linha:
                entrata_string += str(e)

        respostas.append(busca_profundidade(entrata_string, s_problema, 0))

    saida = ""
    for resposta in respostas:
        saida += resposta + "\n"

    print(saida)

    end = time.time()

    print(end-start)


if __name__ == '__main__':
    main()
