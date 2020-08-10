def main():

    # quantidade de solucoes encontradas
    cout = 0
    # inicia o tabuleiro para as condicoes de contorno
    restrains = [[1 for j in range(8)] for i in range(8)]

    # row checa a ataques da coluna
    column = [1 for j in range(8)]

    # diag_1 e diag_2 checa ataques nas diagonais
    diag_1 = [1 for j in range(15)]
    diag_2 =  [1 for j in range(15)]


    # i: linha, j: coluna
    for i in range(8):
        string = input()
        for j in range(8):
            if string[j] == "*":
                restrains[i][j] = 0

    n = search(0, column, diag_1, diag_2, restrains, cout)
    print(n)

def search(y, column, diag_1, diag_2, restrains, cout):

    # y representa a quantidade de rainhas na tabuleiro bem como a linhas atual,
    # ja que, em uma linha, deva conter somente uma rainha
    # se as 8 rainhas forem posicionadas no tabuleiro,
    # uma solucao eh encontrada
    if y == 8:
        return cout+1
    
    for i in range(8):
        if restrains[y][i] and column[i] and diag_1[i+y] and diag_2[i-y+8-1]:
            
            column[i] = 0
            diag_1[i+y] = 0
            diag_2[i-y+8-1] = 0

            cout = search(y+1, column, diag_1, diag_2, restrains, cout)

            column[i] = 1
            diag_1[i+y] = 1
            diag_2[i-y+8-1] = 1

    return cout


if __name__ == "__main__":
    main()
