#FUNÇÕES
def transf_aprovada(saldo_emissor,saldo_receptor,valor_transferencia):####### FUNÇÃO PARA IMPRIMIR A SAÍDA CASO A TRANSAÇÃO SEJA APROVADA
    saldo_emissor -= valor_transferencia
    saldo_receptor += valor_transferencia
    print("\nSua transferência foi realizada com sucesso!\nSaldo do emissor: R${}\nSaldo do receptor: R${}".format("%.2f" % saldo_emissor, "%.2f" % saldo_receptor))

def erro_valores(valor_transferencia, tipo_transferencia):####### FUNÇÃO PARA VERFICAR O ERRO E O MOTIVO PELO QUAL A TRANSAÇÃO NÃO FOI APROVADA
    if valor_transferencia <= 5000:
        if tipo_transferencia == "TED":
            print("\nSua transferência não foi completada pois transferências via TED só são permitidas para valores acima de R$ 5 mil e até R$ 10 mil")
        else:
            print("\nSua transferência não foi completada pois Transferências via DOC só são permitidas para valores acima de R$ 10 mil")
    elif 5000 < valor_transferencia <= 10000:
        if tipo_transferencia == "PIX":
            print("\nSua transferência não foi completada pois o limite de valor máximo permitido para uma transferência via PIX é de R$ 5 mil")
        else:
            print("\nSua transferência não foi completada pois Transferências via DOC só são permitidas para valores acima de R$ 10 mil")
    else:
        if tipo_transferencia == "PIX":
            print("\nSua transferência não foi completada pois o limite de valor máximo permitido para uma transferência via PIX é de R$ 5 mil")
        else:
            print("\nSua transferência não foi completada pois transferências via TED só são permitidas para valores acima de R$ 5 mil e até R$ 10 mil")

def validadorCPF(cpf_busca):######## FUNÇÃO PARA VALIDAR O CPF
    cpf = [int(char) for char in cpf_busca if char.isdigit()]
    if len(cpf) != 11:
        return False
    if cpf == cpf[::-1]:
        return False
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

#ENTRADAS
saldo_emissor=0
saldo_receptor=0

valor_transferencia=float(input("Qual o valor da transferência? "))
tipo_transferencia=str(input("Qual o tipo de transferência? (apenas PIX, TED ou DOC) "))
nome_emissor=str(input("Qual o nome do(a) emissor(a)? "))
agencia_emissor=int(input("Qual a agência do(a) {}? ".format(nome_emissor)))
conta_emissor=int(input("Qual a conta do(a) {}? ".format(nome_emissor)))
cpf_emissor=input("Qual o CPF do(a) {}? (no formato XXX.XXX.XXX-XX) ".format(nome_emissor))
nome_receptor=str(input("Qual o nome do(a) receptor(a)? "))
agencia_receptor=int(input("Qual a agência do(a) {}? ".format(nome_receptor)))
conta_receptor=int(input("Qual a conta do(a) {}? ".format(nome_receptor)))
cpf_receptor=input("Qual o CPF do(a) {}? ".format(nome_receptor))

#PROCESSAMENTO
if validadorCPF(cpf_emissor) and validadorCPF(cpf_receptor):
    if tipo_transferencia == "PIX" or tipo_transferencia == "TED" or tipo_transferencia == "DOC":
        if conta_emissor == conta_receptor and agencia_emissor == agencia_receptor:
            print("\nSua transferência não foi completada pois a agência e conta do emissor são as mesmas do receptor")
        else:
            if valor_transferencia <= 5000:
                if tipo_transferencia == "PIX":
                    transf_aprovada(saldo_emissor,saldo_receptor, valor_transferencia)
                else:
                    erro_valores(valor_transferencia,tipo_transferencia)
            elif 5000 < valor_transferencia <= 10000:
                if tipo_transferencia == "TED":
                    transf_aprovada(saldo_emissor,saldo_receptor, valor_transferencia)
                else:
                    erro_valores(valor_transferencia,tipo_transferencia)
            else:
                if tipo_transferencia == "DOC":
                    transf_aprovada(saldo_emissor,saldo_receptor, valor_transferencia)
                else:
                    erro_valores(valor_transferencia,tipo_transferencia)
    else:
        print("\nSua transferência não foi completada pois foi selecionado um tipo de transferêcia inválido (digite apenas PIX, TED ou DOC)")
else:
    print("\nSua transferência não foi completada pois ocorreu algum erro com a validação do CPF do emissor ou do receptor")