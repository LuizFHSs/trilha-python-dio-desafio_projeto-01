# Criando um Sistema Bancário com Python - [Python AI Backend Developer](https://web.dio.me/track/coding-future-vivo-python-ai-backend-developer/)

## ![Capa do bootcamp](https://hermes.dio.me/tracks/648ef080-6c4b-4e54-bf72-34f62030f350.png)

## DESAFIO

Fomos contratados por um grande banco para desenvolver o seu novo sistema.
Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python.
Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

## OBJETIVO GERAL DO DESAFIO

Criar um sistema bancário com as operações:

+ Sacar
+ Depositar
+ Visualizar extrato

## RESTRIÇÕES DO DESAFIO

+ **Operação de depósito**

   Deve ser possível depositar valores positivos.

   Todos os depósitos devem ser exibidos na operação de extrato.

+ **Operação de saque**

   O sistema deve permitir realizar 3 saques diários com limite máximo de quinhentos reais por saque.

   Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro.

   Todos os saques devem ser exibidos na operação de extrato.

+ **Operação de extrato**

   Deve listar todos os depósitos e saques realizados na conta.

   Se o extrato estiver em branco, exibir a mensagem: "Não foram realizadas movimentações.".
  
   Os valores devem ser exibidos com o formato "R$ xxx.xx"

## SOLUÇÃO PARA O DESAFIO

Para resolver o desafio, foi utilizado as tecnologias:

+ VScode
+ Python

Na resolução do desafio, foi criado dois arquivos com a extensão do python.

Um arquivo para rodar o programa, onde contém somente um menu para poder interagir com o programa e outro arquivo que contém três funções para realizar as tarefas propostas neste desafio.

No arquivo [operacao_bancaria](./Modules/operaco_bancaria.py) foram criadas três variáveis:

+ Uma do tipo lista, para representar os extratos
+ Uma do tipo float, para receber os depósitos e saques
+ Uma do tipo int, para armazenar a quantidade de saques

Ainda no arquivo operacao_bancaria, foram criadas três funções:

+ **Deposito**

   É verificado se o valor depositado não é um número negativo;

   É somado o valor depositado com o saldo atual;

   É adicionado na variável extratos o valor depositado com a formatação "Depósito de R$xxx.xx";

   Caso a tentativa de depositar um valor negativo é exibido uma mensagem avisando que houve um erro.

+ **Saque**

   É verificada se houve mais de três saques;

   É verificado se o valor de saque é menor ou igual ao saldo atual e se não passou do limite de saque;

   É subtraido o valor de saque com o saldo atual;

   É adicionado na variável extratos o valor de saque com a formatação "Saque de R$xxx.xx";

   Caso a tentativa de sacar mais de 500 reais ou sacar um valor maior que o saldo atual é exibido uma mensagem de aviso;

   Caso a tentativa de sacar mais de três vezes é exibido uma mensagem de aviso.

+ **Extrato**

   É exibido todas as operações realizadas;

   Caso a tentativa de exibir as operações sem que tenham feito, é exibido a mensagem: "Não foram realizadas movimentações."

### Autor: LuizFHSs
