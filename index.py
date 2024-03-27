# Inicio do projeto
#teste
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

def adicionar_candidatos(candidatos):
    num_adicionais = obter_numero_candidatos()
    for i in range(num_adicionais):
        dados_candidato = preencher_dados_candidato()
        candidatos.append(dados_candidato)
    return candidatos

def procura_candidatos(candidatos, nota_entrevista=None, nota_teste_teórico=None, nota_teste_prático=None, nota_soft_skills=None):
    candidatos_selecionados = []
    
    for candidato in candidatos:
        nome, notaE, notaT, notaP, notaS = candidato
        
        if nota_entrevista is not None and notaE < nota_entrevista:
            continue
        
        if nota_teste_teórico is not None and notaT < nota_teste_teórico:
            continue
        
        if nota_teste_prático is not None and notaP < nota_teste_prático:
            continue
        
        if nota_soft_skills is not None and notaS < nota_soft_skills:
            continue
        
        candidatos_selecionados.append(candidato)
    
    return candidatos_selecionados

def main():
    Candidatos = []
    while True:
        print("Escolha uma opção:")
        print("1. Adicionar novos candidatos")
        print("2. Procurar candidato por nota")
        print("3. Sair")
        opcao = input("Digite o número correspondente à sua escolha: ")
        
        if opcao == '1':
            num_candidatos = obter_numero_candidatos()
            for i in range(num_candidatos):
                dados_candidato = preencher_dados_candidato()
                Candidatos.append(dados_candidato)
            exibir_resultados(Candidatos)
            
            while True:
                opcao_adicionar = input("Deseja adicionar mais candidatos? (s/n): ").lower()
                if opcao_adicionar == 's':
                    Candidatos = adicionar_candidatos(Candidatos)
                    exibir_resultados(Candidatos)
                elif opcao_adicionar == 'n':
                    break
                else:
                    print("Opção inválida. Por favor, escolha 's' para adicionar mais candidatos ou 'n' para encerrar a adição.")
        
        elif opcao == '2':
            if not Candidatos:
                print("Não há candidatos registrados. Por favor, adicione candidatos primeiro.")
            else:
                nota_entrevista = int(input("Digite a nota mínima desejada para a entrevista: "))
                nota_teste_teórico = int(input("Digite a nota mínima desejada para o teste teórico: "))
                nota_teste_prático = int(input("Digite a nota mínima desejada para o teste prático: "))
                nota_soft_skills = int(input("Digite a nota mínima desejada para as soft skills: "))
                
                candidatos_filtrados = procura_candidatos(Candidatos, nota_entrevista, nota_teste_teórico, nota_teste_prático, nota_soft_skills)
                exibir_resultados(candidatos_filtrados)
        
        elif opcao == '3':
            print("Encerrando o programa.")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma das opções listadas.")

if __name__ == "__main__":
    main()
