while True:
        try:
            num = int(input("Quantos candidatos? "))
        except ValueError:
            print("Por favor, insira apenas números inteiros.")
Candidatos = []
    
for i in range(numCandidatos):
    
    
    while True:
        nome = input("Digite o nome do candidato: ")
        if nome.replace(' ', '').isalpha():
            print('')
        else:
            print("Por favor, insira apenas letras e espaços.")
   
    while True:
        try:
            notaE = (int(input(f"Nota da Entrevista do Candidato: ")))
            if not 0 <= notaE <= 10:
                raise ValueError("Nota inválida! Digite Novamente")
        except ValueError as e:
                print("Valor inválido")
        else:
                break
        
        
    while True:
        try:
            notaT = (int(input(f"Nota do Teste Teórico do Candidato: ")))
            
            if not 0 <= notaT <= 10:
                raise ValueError("Nota inválida! Digite Novamente")
        except ValueError as e:
                print("Valor inválido")
        else:
                break
    
    
    while True:
        try:
            notaP = (int(input(f"Nota do Teste Prático do Candidato: ")))
            
            if not 0 <= notaP <= 10:
                raise ValueError("Nota inválida! Digite Novamente")
        except ValueError as e:
                print("Valor inválido")
        else:
                break
    
    while True:
        try:
            notaS = (int(input(f"Nota da Soft Skills do Candidato: ")))
            
            if not 0 <= notaS <= 10:
                raise ValueError("Nota inválida! Digite Novamente")
        except ValueError as e:
                print("Valor inválido")
        else:
                break
    
    

    Candidatos.append((nome, notaE, notaT, notaP, notaS))

print("-------------------------------------------------------------------------")
print("| Candidato\t\t| Resultado ")
print("-------------------------------------------------------------------------")

for cand in Candidatos:
    nome, notaE, notaT, notaP, notaS = cand
    notas_formatadas = f"e{notaE}_t{notaT}_p{notaP}_s{notaS}"
    print(f"| {nome.ljust(15)}\t| {notas_formatadas.ljust(22)}")

print("-------------------------------------------------------------------------")