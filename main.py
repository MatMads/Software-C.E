#Sistema de gerenciamento de estoque, compra e venda.

print('Escolha uma opção:')
print('1 - Cadastrar produto')
print('2 - Lista de produtos')
print('3 - Compra e venda')

#Cadastrar um produto no sistema:
    #-Código do produto - int
    #-Nome do produto - string
    #-Quantidade em estoque - int
    #-Valor unitário - float




def cadastrarProduto():
    produto = []
    nome_produto = input('Nome do produto: ')
    produto.append(nome_produto)
    id = int(input('Código do produto: '))
    produto.append(id)
    quantidade = int(input('Quantidade de itens: '))
    produto.append(quantidade)
    valor_unit = float(input('Valor (unitário) do produto: R$ '))
    produto.append(valor_unit)
    print(produto)
    


def listaEstoque():
    print()


cadastrarProduto()



    #Configurar opção de compra
        #-Listar e selecionar o produto (Em lista ou tabela)
        #-Quantidade
        #-Valor
        #-Perguntar se deseja comprar algo mais
    #Pagamento
        #-Crédito (Juros de 5% em cima do valor total)
        #-Débito (Desconto de 10% em cima do valor total)