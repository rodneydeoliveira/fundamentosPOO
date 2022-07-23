def cria_conta(numero, ag, titular, saldo): #parametros
            #Chave   #valor/parametro
    conta = {"número": numero, "ag": ag, "titular": titular, "saldo": saldo}
    return conta

def deposita (conta, valor):
    conta["saldo"] += valor

def saca (conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print(f"Saldo é {conta['saldo']}")


conta = cria_conta(400, 2565, "Rodney", 100.0)
deposita(conta, 200.0)
print(conta)
extrato(conta)
