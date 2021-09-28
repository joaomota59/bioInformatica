import pandas as pd

if __name__ == "__main__":
    vertical, horizontal = ('CACCCCCCACGCAAAUGCGUGGCCAGGCCGCAACAUAGCGUCUGACCUGUAGGAUCUUAACGUGCUCGAAGGGCUACAAAAUUCGAGGGCAACACCCUGACGACGAUGGGAGCGACCACGCGAGAAUACUCAUGAAUUCCAUAUGCUACGUACUAAUCUAGGCCACAGGUCAGGGCAGACACAAUGCAAUGGCACGCGCC', 'CACCCCCCACGCAAAUGCGUGGCCAGGCCGCAACAUAGCACAGCGUCUGUAGGAUCUUAACGUGCUCGAAGGGCUACAAAAUUCGAGGGCAACACCCUGACGUCACGACGAUGGGAGCGACCACGCGAGAAUA')

    #vertical, horizontal = ('AGCT', 'GCTT')
    match = 3
    mismatch = -1
    gap = -2

    matriz = []
    matrizCaminho = []
    ###Inicializando matriz###############
    for i in range(len(vertical)+2):
        aux = []
        aux2 = []
        for j in range(len(horizontal)+2):
            aux.append(0)
            aux2.append("")
        matriz.append(aux)
        matrizCaminho.append(aux2)

    matriz[0][0] = ""
    matriz[0][1] = ""
    matriz[1][0] = ""


    for i in range(len(matriz[0])-2):#colocando sequencias na horizontal
        matriz[0][i+2] = horizontal[i]
        matrizCaminho[0][i+2] = horizontal[i]
        matriz[1][i+2] = (i+1)*gap
    for j in range(len(matriz[2:])):#colocando sequencias na vertical
        matriz[j+2][0] = vertical[j]
        matrizCaminho[j+2][0] = vertical[j]
        matriz[j+2][1] = (j+1)*gap


    ########################################

    ######Preenchendo a matriz##############
    diagonal = 0
    for i in range(len(matriz)-2):
        for j in range(len(matriz[0])-2):
            L = i+2
            C = j+2
            vertical = matriz[L-1][C] + gap
            horizontal = matriz[L][C-1] + gap

            if (matriz[L][0] == matriz[0][C]):#match
                diagonal = matriz[L-1][C-1] + match
            elif (matriz[L][0] == "-" or matriz[0][C] == "-"):#gap
                diagonal = matriz[L-1][C-1] + gap
            else:#matriz[L][0] != matriz[0][C]
                diagonal = matriz[L-1][C-1] + mismatch

            matriz[L][C] = max(vertical,horizontal,diagonal)
    ########################################


    df = pd.DataFrame(matriz)
    df.to_excel("matriz.xlsx",index=False,header=False)


    ##################backtrace#############

    L = len(matriz) -1
    C = len(matriz[0]) -1
    print("Score:",matriz[L][C])
    while L >= 1:
        try:
            if L==1:
                raise TypeError
            if (matriz[L][0] == matriz[0][C]):#match
                matrizCaminho[L][C] = "↖"
                L = L-1
                C = C-1
            else:
                valorVertical = matriz[L-1][C]
                valorHorizontal = matriz[L][C-1]
                valorDiagonal = matriz[L-1][C-1]
                maior = max(valorVertical,valorHorizontal,valorDiagonal)
                if maior == valorVertical:
                    matrizCaminho[L][C] = "↑"
                    L = L-1
                elif maior == valorHorizontal:
                    matrizCaminho[L][C] = "←"
                    C = C-1
                else:
                    matrizCaminho[L][C] = "↖"
                    L = L-1
                    C = C-1
        except TypeError:
            if L == 1:
                matrizCaminho[L][C] = "*"
            else:
                matrizCaminho[L][C] = "↑"
            L = L-1

    df2 = pd.DataFrame(matrizCaminho)
    df2.to_excel("matrizCaminho.xlsx",index=False,header=False)
