print("===SIstema de Pedido de Lanchonete===")
print()

#---Inputs
nome_cliente = input("Digite seu nome: ").strip()
valor_pedido = float(input("Digite o valor da conta: "))
cupom = input(f"{nome_cliente}, você tem cupom? (S/N)").strip().upper()

#---Variaveis
valor_final = valor_pedido
frete_centro = 4.00
frete_praia = 8.00
frete_padrao = 12.00

#---condicionais
if cupom == "S":
    nome_cupom = input("Nome do cupom: ").strip().upper()
    if nome_cupom == "LAKERS99":
        valor_desconto = valor_pedido * 0.85
        print("Cupom aplicado!")

    else:
        valor_desconto = valor_pedido
        print("Cupom inválido!")
        

elif cupom == "N":
    valor_sem_desconto = valor_pedido * 1.00
    print("Nenhum cupom aplicado.")

região = input("Qual a sua região? ").strip().upper()

if região == "CENTRO":
    if cupom == "S":
        valor_final = valor_desconto + frete_centro
    else:
        valor_final = valor_sem_desconto + frete_centro

elif região == "PRAIA":
    if cupom == "S":
        valor_final = valor_desconto + frete_praia
    else:
        valor_final = valor_sem_desconto + frete_praia

else:
    if cupom == "S":
        valor_final = valor_desconto + frete_padrao

    elif cupom == "N":
        valor_final = valor_sem_desconto + frete_padrao

print(
    f"Nome:{nome_cliente}", 
    f"Região: {região}",
    f"Cupom aplicado: {cupom}",
    f"Valor do pedido: R${valor_pedido:.2f}",
    f"Valor final: R${valor_final:.2f}",
    sep="\n"
    
    )
    







