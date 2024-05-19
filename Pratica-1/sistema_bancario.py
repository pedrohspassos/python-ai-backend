
"""
Regras de negocio:

Possuir tres funcionalidades:

- Deposito
  - possibilitar apenas depositar valores positivos
  - depositos devem ser armazenados e exibidos no extrato

- Saque
  - possibilitar apenas 3 saques como limite
  - limitar o valor de cada saque em 500
  - caso o saldo seja insuficiente, não permitir que aconteça a operação
  - exibir no extrato o saque realizado

- Extrato
  - Listar todos os saques e depositos realizados durante a operação
  - exibir nessa listagem o saldo atual da conta

Observações:
- Nesse exemplo, iremos trabalhar com apenas uma unica conta, logo não teremos o numero da conta associado a operação
- Esse sistema sera incrementado na proxima pratica (Pratica-2) com uma nova estrutura e funcionalidades 

"""


# Função Principal
def main():

  menu =  """
 ----------------------------------------------------
 Seja Bem Vindo, realize sua operação bancaria!!
 ----------------------------------------------------
 [d] Depositar
 [s] Sacar
 [e] Extrato
 [q] Sair
 ----------------------------------------------------
 ==> """

  saldo = 0
  limite = 500
  extrato = ""
  numero_saques=0
  LIMITE_SAQUES=3

  exibir_menu(menu, saldo, extrato,limite,numero_saques,LIMITE_SAQUES)




# !! Metodos implementados no banco !! 

#### Método exibir menu ####
def exibir_menu(menu, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
  
  while True:
    opcao = input(menu)

    if opcao == "d":
      saldo, extrato = realizar_deposito(saldo, extrato)
      
      
    elif opcao == "s":
      saldo, extrato, numero_saques = realizar_saque(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)
     
    elif opcao == "e":
      exibir_extrato(saldo, extrato)
      
    elif opcao == "q":
      print("\nObrigado pela preferencia, volte quando precisar!")
      break
    else:
      print("\nOperação invalida, por favor selecione novamente a operação desejada")
    

#### Método depositar ####
def realizar_deposito(saldo, extrato):
  valor_deposito = float(input("\nInforme o valor a ser depositado: "))

  if valor_deposito > 0:
    saldo += valor_deposito
    extrato += f"Deposito: R$ {valor_deposito:.2f}\n"
    print("Deposito realizado com sucesso!")
  else:
    print("Operação falhou! O valor informado é invalido.")
  
  return saldo, extrato

    
#### Método sacar ####
def realizar_saque(saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
 
  valor_saque = float(input("\nInforme o valor a ser sacado: "))

# Verificando condições
  execedeu_saldo = valor_saque > saldo
  execedeu_limite = valor_saque > limite
  execedeu_saques = numero_saques > LIMITE_SAQUES

  if execedeu_saldo:
    print("\nOperação falhou! Voce não tem saldo suficiente.")
  elif execedeu_limite:
    print("\nOperação falhou! O valor do saque execeu o limite permitido pelo banco.")
  elif execedeu_saques:
    print("\nOperação falhou! Foi atingido o numero maximo de saques.")
  elif valor_saque > 0:
    saldo -= valor_saque
    extrato += f"Saque: R$ {valor_saque:.2f}\n"
    numero_saques+=1
    print("Saque realizado com sucesso!")

  else:
    print("\nOperação falhou! O valor informado é invalido.")
  
  return saldo, extrato, numero_saques
  



### Método exibir extrato ###
def exibir_extrato(saldo, extrato):

  print("\n###################### Extrato ######################")
  print("Não foram realizadas movimentações" if not extrato else extrato)
  print(f"""----------------------------------------------------
Saldo: R$ {saldo:.2f}
#####################################################
""")

if __name__ == "__main__":
  main()