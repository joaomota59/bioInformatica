def ribossomo(entrada):
    start = ["AUG"]
    stop = ["UAA","UAG","UGA"]
    geneticCode = {
        'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 
        'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 
        'UAU':'Y', 'UAC':'Y', 'UAA':'ST', 'UAG':'ST', 
        'UGU':'C', 'UGC':'C', 'UGA':'ST', 'UGG':'W', 
        'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
        'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
        'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
        'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
        'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
        'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
        'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
        'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
        'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
        'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
        'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
        'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'
        }

    matriz = []
    aux = ''
    flagStart = False
    for i in range(0,len(entrada),3):
        trio = entrada[i:i+3]
        
        if trio == start[0]:#Começa a ler a entrada
            flagStart = True
            aux+=geneticCode[trio]
        elif trio in stop:
            flagStart = False
            #aux+=geneticCode[trio]
            matriz.append(aux)
            aux = ''
        elif flagStart:
            aux+=geneticCode[trio]     
    return matriz

if  __name__ == '__main__':
    arquivo = open('ribossomo-output.txt','w')

    proteinas = ribossomo('AUGCUGCAAACCUGUACAAUCCUCCGGCGCCACAGACAGGAGACUGACGCCCGACACUUGGAUAACAAUCGUUCCAAGAUCGACACUUUGCUACCACUGCGCCUUCGGGUAGGCCGAUGGUUUCAUAUCCAUCGAAUAGAUGCGAUGCCCUUAGUCUCUCCUAUAAAGGGGUGGUUUCCUGAUUUGUCCUCCCUGGCAAUAGUGCGUGCAGUUCUGAUUCGUACAACGCGUGUCCACUUACUUAUCCCUUACCCUCUCGAAUCUUAUGUUAGAUCUAAACAUGUUAACUGCCGUCAUCCUAAGUCAGUUUAG')
    
    for proteina in proteinas:
        arquivo.write(proteina+'\n')
    arquivo.close()

    print("Saída salva, no diretório corrente!")
