
#variaveis de uso
x_ratao = "pão, hamburguer, salada, queixo duplo, presunto, molho especial e barbecue"
x_Hamburguer = "pão, hamburguer, queijo e presunto"
x_salada = "pão, hamburguer, salada, presunto, queixo"  
x_salada_preco = 6.00
x_Hamburguer_preco = 4.00
x_ratao_preco = 10.00
batata_preco = 4.00



print("\n ---Lanchonete Bom Gosto---")
print()

nome_cliente = str(input("Digite seu nome: "))

def menu():
    print("\n ---Bem Vindo(a)!!!")
    print("Escolha suas opções de lanche abaixo: ")
    print()
    print("1 - X-Ratão")
    print("2 - X-Hamburguer")
    print("3 - X-Salada")
    print("4 - Sair")
    return int(input("Sua opção sera qual? "))

while True:
    opcao = menu()

    if opcao == 1:
        valor_atual = x_ratao_preco
        ver_lanche = input("Deseja ver um resumo sobre o lanche que escolheu? (S/N)").strip().upper()
        if ver_lanche == "S":
            print(
                f"O X-Ratão é composto por:",
                f"{x_ratao}",
                f"Seu preço é de R${x_ratao_preco:.2f}.",
                sep="\n"
            )
        elif ver_lanche == "N":
            print("OK, tudo bem. Vamos seguir com o seu pedido.")

        batata_frita = input("Deseja adicionar batatas fritas por R$4.00? (S/N)").strip().upper()
        if batata_frita == "S":
            valor_atual = x_ratao_preco + batata_preco
            print(f"Batatas fritas foram adicionadas. Agora o valor é de R${valor_atual:.2f}.")

        elif batata_frita == "N":
            valor_atual = x_ratao_preco
            print(f"Ok. Vamos continuar com o pedido. O valor continua R${valor_atual:.2f}.")
            

        cupom = input("Deseja aplicar cupom? (S/N)").strip().upper()
        if cupom == "S":
            while True:

                nome_cupom = input("Nome do cupom: ").strip().upper()
                if nome_cupom == "FOME10":
                    valor_final = valor_atual * 0.1
                    print(f"O cupom foi aplicado com sucesso! O preço atual é de R${valor_final:.2f}.")
                    break

                else:
                    print("Cupom inválido! Tente novamente!")

        elif cupom == "N":
            valor_final = x_ratao_preco
            print(f"Ok, vamos manter o preço de R${valor_final:.2f}.")

    elif opcao == 2:
        valor_atual = x_Hamburguer_preco
        ver_lanche = input("Deseja ver um resumo sobre o lanche escolhido? (S/N)")
    

        

    


        
        
        

        
    

        


    










