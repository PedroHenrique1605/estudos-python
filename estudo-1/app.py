print("Sistema de Cupom de Desconto")

nome_cliente = input("Digite seu nome: ")
print(f"{nome_cliente}, informe o valor da conta")
valor_conta = float(input("Digite o valor da conta: "))
cupom = input(f"{nome_cliente}, você tem cupom? (S/N)").upper().strip()

#variaveis
frete_centro = 5.00
frete_pitangueiras = 7.00
frete_padrão = 12.00
desconto = 1.0

#---BLOCO DO CUPOM---
if cupom == "S":
    nome_cupom = input("Digite o nome do cupom: ").upper().strip()
    if nome_cupom == "GUARUJA10":
        desconto = 0.90
        print("Cupom aplicado")
    else:
        print("Cupom invalido")
else:
    print("Sem cupom aplicado")

#---BLOCO DO FRETE---
bairro = input(f"{nome_cliente}, digite seu bairro para calcularmos seu frete: ").upper().strip()

if bairro == "CENTRO":
    print(f"Seu frete é de R${frete_centro:.2f}")
    valor_final = (valor_conta * desconto) + frete_centro

elif bairro == "PITANGUEIRAS":
                print(f"Seu frete é de R${frete_pitangueiras:.2f}")
                valor_final = (valor_conta * desconto) + frete_pitangueiras

else:
                print(f"Seu frete é de R${frete_padrão:.2f}")
                valor_final = (valor_conta * desconto) + frete_padrão

print(f"O valor final a ser pago é de R${valor_final:.2f}")


    


        
    