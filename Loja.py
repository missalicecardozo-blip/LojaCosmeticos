produtos = ['Base', 'Pó', 'Batom', 'Esmalte', 'Blush', 'Rímel', 'Paleta De Sombra']
cliente = []
estoquista = [ "Marlon", "Taís","Allan","Jeniffer","Aguines",]
gerente = ["Júlio", "Paula"]
donoEmpresa = ["Cinthia"]

def estoquistas(nome_usuario):
    """"
    Função de acesso nível 'estoquista'.
    Solicita o parâmetro 'nome_usuario' é exigido para confirmarquem está realizando o acesso.
    Permite visualisar e mudar a lista de produtos (Adicionar, Excluir,).
    """
    print("abrindo a página de estoquista...")

    opicoesEstoquista = input("Digite o número da opção desejada:\n1 - Adicionar Produtos\n2 - Excluir Produtos\n3 - Voltar\nEscolha: ")
    
    if opicoesEstoquista == "1":
        print("\nAdicionar Produtos:")
        nome = input("Digite o produto que deseja adicionar:" )
        produtos.append(nome)
    elif opicoesEstoquista == "2":
        print("\nExcluir Produtos:")
        nome = input("Digite o produto que deseja excluir")
        produtos.remove(nome)
    elif opicoesEstoquista == "3":
        print("Voltando ao menu principal...")      