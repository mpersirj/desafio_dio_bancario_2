# desafio_dio_bancario_2
projeto bootcamp

# Sistema Bancário em Python

Este projeto é um sistema bancário desenvolvido como parte do Bootcamp Engenharia de Dados com Python, realizado pela plataforma [DIO (Digital Innovation One)](https://www.dio.me/). O objetivo do projeto foi aplicar conceitos de lógica de programação, modularização, e manipulação de dados em Python para criar um sistema funcional e escalável.

## Funcionalidades

O sistema bancário implementa as seguintes funcionalidades principais:

1. **Depósito**
   - Permite o depósito de valores na conta bancária.

2. **Saque**
   - Realiza saques com validações de saldo, limite diário de saques e limite por operação.

3. **Extrato**
   - Exibe o histórico de movimentações e o saldo atual da conta.

4. **Cadastro de Usuário**
   - Registra novos usuários no sistema com informações como nome, CPF, data de nascimento e endereço.

5. **Cadastro de Conta Corrente**
   - Cria contas correntes associadas a usuários existentes.

6. **Listagem de Contas**
   - Exibe todas as contas cadastradas no sistema.

## Regras de Negócio

- Cada usuário é identificado pelo CPF, e não é possível cadastrar dois usuários com o mesmo CPF.
- Uma conta corrente é vinculada a um único usuário, mas um usuário pode ter várias contas.
- O número da conta é gerado de forma sequencial e a agência é fixa (\"0001\").
- O limite diário de saques é de 3 operações por dia, com um valor máximo de R$500,00 por saque.

## Tecnologias Utilizadas

- **Python 3.8 ou superior**
- Programação estruturada
- Modularização e funções

