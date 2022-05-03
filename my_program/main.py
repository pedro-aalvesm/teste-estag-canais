import pandas as pd
entrada=pd.read_csv('entrada.txt', sep='|')
saldo_emissor=0
saldo_receptor=0

valor_transferencia=float(input("Qual o valor da transferência? "))
tipo_transferencia=str(input("Qual o tipo de transferência? (PIX, TED ou DOC) "))
nome_emissor=str(input("Qual o nome do(a) emissor(a)? "))
agencia_emissor=int(input("Qual a agência do(a) {}? ".format(nome_emissor)))
conta_emissor=int(input("Qual a conta do(a) {}? ".format(nome_emissor)))
cpf_emissor=input("Qual o CPF do(a) {}? (no formato XXX.XXX.XXX-XX) ".format(nome_emissor))
nome_receptor=str(input("Qual o nome do(a) receptor(a)? "))
agencia_receptor=int(input("Qual a agência do(a) {}? ".format(nome_receptor)))
conta_receptor=int(input("Qual a conta do(a) {}? ".format(nome_receptor)))
cpf_receptor=input("Qual o CPF do(a) {}? ".format(nome_receptor))

if tipo_transferencia == "PIX" or tipo_transferencia == "TED" or tipo_transferencia == "DOC":
    if conta_emissor == conta_receptor and agencia_emissor == agencia_receptor:
        print("Sua transferência não foi completada pois a agência e conta do emissor são as mesmas do receptor")
    else:
        if valor_transferencia <= 5000:
            if tipo_transferencia == "PIX":
                saldo_emissor-=valor_transferencia
                saldo_receptor+=valor_transferencia
                print("Sua transferência foi realizada com sucesso!\n Saldo do emissor: R${}\n Saldo do receptor: R${}".format("%.2f"%saldo_emissor,"%.2f"%saldo_receptor))
            elif tipo_transferencia == "TED":
                print("Sua transferência não foi completada pois transferências via TED só são permitidas para valores acima de R$ 5 mil e até R$ 10 mil")
            else:
                print("Sua transferência não foi completada pois Transferências via DOC só são permitidas para valores acima de R$ 10 mil")
        elif 5000 < valor_transferencia <= 1000:
            if tipo_transferencia == "PIX":
                print("Sua transferência não foi completada pois o limite de valor máximo permitido para uma transferência via PIX é de R$ 5 mil)")
            elif tipo_transferencia == "DOC":
                print("Sua transferência não foi completada pois Transferências via DOC só são permitidas para valores acima de R$ 10 mil")
            else:
                saldo_emissor -= valor_transferencia
                saldo_receptor += valor_transferencia
                print("Sua transferência foi realizada com sucesso!\n Saldo do emissor: R${}\n Saldo do receptor: R${}".format("%.2f" % saldo_emissor, "%.2f" % saldo_receptor))
        else:
            if tipo_transferencia == "PIX":
                print("Sua transferência não foi completada pois o limite de valor máximo permitido para uma transferência via PIX é de R$ 5 mil)")
            elif tipo_transferencia == "TED":
                print("Sua transferência não foi completada pois transferências via TED só são permitidas para valores acima de R$ 5 mil e até R$ 10 mil")
            else:
                saldo_emissor -= valor_transferencia
                saldo_receptor += valor_transferencia
                print("Sua transferência foi realizada com sucesso!\n Saldo do emissor: R${}\n Saldo do receptor: R${}".format("%.2f" % saldo_emissor, "%.2f" % saldo_receptor))
else:
    print("Sua transferência não foi completada pois foi selecionado um tipo de transferêcia inválido (digite apenas PIX, TED ou DOC)")