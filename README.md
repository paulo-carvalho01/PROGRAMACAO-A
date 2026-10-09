# Banco Dcomp

Protótipo acadêmico de sistema bancário desenvolvido em Python com Flask e interface HTML/CSS.

## Funcionalidades

- Cadastro de clientes com nome, CPF e idade.
- Criação de contas para clientes cadastrados, com saldo inicial opcional.
- Listagem e pesquisa de contas, com consulta de saldo e dados do titular.
- Depósitos e saques, incluindo validação de valores e saldo disponível.

## Como executar

1. Instale o Python 3.10 ou superior.
2. No terminal, acesse a pasta do projeto e instale a dependência:

   ```powershell
   py -m pip install -r requirements.txt
   ```

3. Inicie o servidor:

   ```powershell
   py banco.py
   ```

4. Abra http://127.0.0.1:5000 no navegador.

Os dados são mantidos em memória enquanto o servidor estiver ligado e são reiniciados ao encerrá-lo. O servidor de desenvolvimento do Flask é destinado a demonstrações locais.
