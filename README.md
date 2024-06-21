# Criando um Sistema Bancário com Python

## OBJETIVO GERAL DO DESAFIO
Criar um sistema bancário com as operações:
 + Sacar
 + Depositar
 + Visualizar extrato

## DESAFIO
Fomos contratados por um grande banco para desenvolver o seu novo sistema.
Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python.
Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

## RESTRIÇÕES DO DESAFIO
 + **Operação de depósito**
   Deve ser possível depositar valores positivos.
   Todos os depósitos devem ser exibidos na operação de extrato.
 + **Operação de saque**
   O sistema deve permitir realizar 3 saques diários com limite máximo de quinhentos reais por saque.
   Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível savar o dinheiro.
   Todos os saques devem ser exibidos na operação de extrato.
 + **Operação de extrato**
   Deve listar todos os depósitos e saques realizados na conta.
   Se o extrato estiver em branco, exibir a mensagem: "Não foram realizadas movimentações.".
   Os valores devem ser exibidos com o formato "R$ xxx.xx"

## SOLUÇÃO PARA O DESAFIO
