numCandidatos = int(input("Quantos Candidatos?: "))
Candidatos = []
    
for i in range(numCandidatos):
    nome = (input(f"Nome do Candidato {i +1}"))
    notaE = (float(input(f"Nota da Entrevista do Candidato: ")))
    notaT = (float(input(f"Nota do Teste Teórico do Candidato: ")))
    notaP = (float(input(f"Nota do Teste Prático do Candidato: ")))
    notaS = (float(input(f"Nota da Soft Skills do Candidato: ")))
    
    Candidatos.append((nome, notaE, notaT, notaP, notaS))
    
for cand in Candidatos:
    nome, notaE, notaT, notaP, NotaS = cand
    print("{nome}/t/t{notaE}")