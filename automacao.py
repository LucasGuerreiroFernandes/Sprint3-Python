ListaPedidos=[]
PedidoFeito=[]
Tipos=("Emergência","Comida","Banheiro","Limpeza","Remédio","Outros")


def pedir ():
    quarto=str(input("Qual o número do seu quarto?"))
    PedidoFeito.append(quarto)
    pedido=int(input("Sobre qual tema é seu pedido? (1.Emergência/2.Comida/3.Banheiro/4.Limpeza/5.Remédio/6.Outros)"))
    PedidoFeito.append(Tipos[pedido])

    if pedido == "1":
        descricaoEscolha= "Nada"
    else:
        descricaoEscolha=str(input("Você deseja adicionar alguma descrição sobre seu pedido?  S/N").upper)


    if descricaoEscolha=="S":
        descricao=str(input("Digite Aqui a descrição:"))
        PedidoFeito.append(descricaoEscolha)

   
    
    return PedidoFeito
    
    
pedir ()
print(PedidoFeito)
