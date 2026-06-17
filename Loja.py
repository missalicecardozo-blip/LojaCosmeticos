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

def gerente(nome_usuario):
    """"
    função de acesso nivel 'gerente' .
    Requer o parâmetro "nome_usuario" para verifecar quem está tentando acessar.
    Permite visualisar e mudar a lista de produtos (Adicionar, Excluir, Atualizar).
    """
    print ('abrindo a página do gerente...') 

    opcoesgerente = input("digite o número da opção desejada:\n1 - cadastrar cliente\n2 - adicionar estoquista\n3 - excluir estoquista\n4 - voltar\nEscolha: ")
    match opcoesgerente:
        case '1':
            print('\nadicionar cliente')
            nome = input ('Digite o nome do cliente')
            cliente.append(nome)
        case '2':
            print('\adicionar estoquista')
            nome = input ('Digite nome do estoquista')
            estoquista.append(nome)

        case '3':
            print('Excluir estoquista') 
            nome = input ('Digite o nome do estoquista que deseja excluir') 
            estoquista.remove(nome)   
        case '4':
            print('Voltando ao menu principal...')       
def donoempresa(nome_usuario):
    """""
    função de acesso nivel "donoempresa" .
    Requer o parâmento "nome_usuario" para verificar quem esta tentando acessar.
    Permite excluir e adicionar gerentes (Adicionar, Excluir, Atualizar).
    """
    print ('abrindo a página do dono...')
   
    opcoesdono = input("digite o número da opção desejada:\n1 - cadastra cliente\n2 - adicionar gerente\n3 - excluir gerente\n4 - voltar\nEscolha: ")
    match opcoesdono:
        case '1':
            print('\nadicionar cliente')
            nome = input ('digite o nome do cliente')
            cliente.append(nome)
        case '2':
            print('\adicionar gerente')
            nome = input ('Digite o nome do gerente')
            gerente.append(nome)
        case '3':
            print('Excluir gerente')
            nome = input('digite o nome do gerente que deseja excluir')
            gerente.remove(nome)
            estoquista.append(nome)
        case '4':
            print('Voltando ao menu principal...')



user = input ('Escreva seu nome:')
print(f"Seja bem-vindo, {user}!")


while True :
    print("\n=== MENU PRINCIPAL ===")
    print("1 - estoquista")
    print("2 - Gerente")
    print("3 - donoEmpresa")
    print("4 - Sair")

    opcao = input("Digite o numero desejado:")

    match opcao:
        case "1":
            nome = input("Digite o nome do estoquista:")
            estoquista(nome)
        case "2":
            nome = input("Digite o nome do gerente:")
            gerente(nome)
        case "3":
            nome = input("Digite o nome do donoEmpresa:")
            print(f"Bem-Vinda, {nome}")
        case "4":
            print("cancelando o sistema...")
            break
              