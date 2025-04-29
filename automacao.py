import pandas as pd

Tipos = ("Emergência", "Comida", "Banheiro", "Limpeza", "Remédio", "Outros")

ListaDePedidoDF = pd.DataFrame(columns=['num', 'Quarto', 'Pedido', 'Descrição'])

def pedir():
    global ListaDePedidoDF 

    quarto = input("Qual o número do seu quarto? ")

    pedido = int(input("Sobre qual tema é seu pedido? (1.Emergência/2.Comida/3.Banheiro/4.Limpeza/5.Remédio/6.Outros) "))
    tipo_pedido = Tipos[pedido - 1]

    descricao = ""
    if pedido != 1:  
        descricaoEscolha = input("Você deseja adicionar alguma descrição sobre seu pedido? S/N ").upper()
        if descricaoEscolha == "S":
            descricao = input("Digite aqui a descrição: ")

    num_pedido = len(ListaDePedidoDF) + 1 

   
    
    ListaDePedidoDF.loc[len(ListaDePedidoDF)] = [num_pedido, quarto, tipo_pedido, descricao]
    ListaDePedidoDF.to_excel("Lista.xlsx")
    print(ListaDePedidoDF)
    

    
def excluir():
    global ListaDePedidoDF

    print(ListaDePedidoDF)
    linha = int(input("Número do pedido a excluir: ")) - 1
    ListaDePedidoDF = ListaDePedidoDF.drop(linha)
    ListaDePedidoDF.to_excel("Lista.xlsx")
    
    print(ListaDePedidoDF)

while True:
    escolha = str(input("O que você deseja fazer PEDIR/EXCLUIR/SAIR?")).upper()

    if escolha == "PEDIR":
        pedir()
        print("Pedido feito com sucesso")
    elif escolha == "EXCLUIR":
        excluir()
        print("Pedido excluído com sucesso")
    elif escolha == "SAIR":
        print("Programa fechado")
        break
    else:
        print("Digite um comando válido")
    
 






   
    
        

    