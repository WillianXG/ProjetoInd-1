def obter_numero_candidatos():
    while True:
        try:
            num_candidatos = int(input("Quantos candidatos? "))
            return num_candidatos
        except ValueError:
            print("Por favor, insira apenas números inteiros.")

def obter_nome_candidato():
    while True:
        nome = input("Digite o nome do candidato: ")
        if nome.replace(' ', '').isalpha():
            return nome
        else:
            print("Por favor, insira apenas letras e espaços.")

def validar_nota(mensagem):
    while True:
        try:
            nota = int(input(mensagem))
            if not 0 <= nota <= 10:
                raise ValueError("Nota inválida! Digite Novamente")
            return nota
        except ValueError:
            print("Valor inválido! Digite um número entre 0 e 10.")

def preencher_dados_candidato():
    nome = obter_nome_candidato()
    notaE = validar_nota("Nota da Entrevista do Candidato: ")
    notaT = validar_nota("Nota do Teste Teórico do Candidato: ")
    notaP = validar_nota("Nota do Teste Prático do Candidato: ")
    notaS = validar_nota("Nota da Soft Skills do Candidato: ")
    return nome, notaE, notaT, notaP, notaS

def exibir_resultados(candidatos):
    print("-------------------------------------------------------------------------")
    print("| Candidato\t\t| Resultado ")
    print("-------------------------------------------------------------------------")
    for cand in candidatos:
        nome, notaE, notaT, notaP, notaS = cand
        notas_formatadas = f"e{notaE}_t{notaT}_p{notaP}_s{notaS}"
        print(f"| {nome.ljust(15)}\t| {notas_formatadas.ljust(22)}")
    print("-------------------------------------------------------------------------")

def main():
    num_candidatos = obter_numero_candidatos()
    Candidatos = []
    for i in range(num_candidatos):
        dados_candidato = preencher_dados_candidato()
        Candidatos.append(dados_candidato)
    exibir_resultados(Candidatos)
    
def adicionar_candidatos(candidatos):
    num_adicionais = obter_numero_candidatos()
    for i in range(num_adicionais):
        dados_candidato = preencher_dados_candidato()
        candidatos.append(dados_candidato)
    return candidatos

def main():
    Candidatos = []
    num_candidatos = obter_numero_candidatos()
    for i in range(num_candidatos):
        dados_candidato = preencher_dados_candidato()
        Candidatos.append(dados_candidato)
    exibir_resultados(Candidatos)
    
    while True:
        opcao = input("Deseja adicionar mais candidatos? (s/n): ").lower()
        if opcao == 's':
            Candidatos = adicionar_candidatos(Candidatos)
            exibir_resultados(Candidatos)
        elif opcao == 'n':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha 's' para adicionar mais candidatos ou 'n' para encerrar o programa.")

    


if __name__ == "__main__":
    main()
