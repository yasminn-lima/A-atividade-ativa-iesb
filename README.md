# ☕ Coffee Shops Tia Rosa - Sistema de Gerenciamento

Um sistema simples em **Python** para gerenciar clientes, produtos e pedidos de uma cafeteria fictícia chamada **Coffee Shops Tia Rosa**.  
O programa roda no terminal e permite cadastrar clientes, cadastrar produtos, registrar pedidos e visualizar os pedidos realizados.

---

## 📌 Funcionalidades

- **Cadastrar Cliente**  
  Permite adicionar um novo cliente, informando nome e telefone.

- **Cadastrar Produto**  
  Permite adicionar novos produtos com nome e preço.

- **Fazer Pedido**  
  Associa um cliente a um produto cadastrado, gerando um pedido.

- **Mostrar Pedidos**  
  Lista todos os pedidos já realizados, mostrando cliente, produto e preço.

- **Sair**  
  Encerra o sistema.

---

## 🛠 Tecnologias Utilizadas

- **Python 3.x**
- Uso de listas e dicionários para armazenamento em memória
- Estrutura de menu interativo no terminal

---

## 📂 Estrutura do Código

- **Listas:**  
  - `clientes` → guarda dados dos clientes (`nome` e `telefone`)  
  - `produtos` → guarda dados dos produtos (`nome` e `preco`)  
  - `pedidos` → guarda os pedidos feitos (cliente, produto e preço)

- **Funções principais:**  
  - `menu()` → controla as opções e navegação  
  - `cadastrar_cliente()` → registra clientes  
  - `cadastrar_produto()` → registra produtos  
  - `fazer_pedido()` → registra pedidos  
  - `mostrar_pedidos()` → exibe todos os pedidos

---

## ▶️ Como Executar

1. **Instale o Python** (se ainda não tiver) → [Download Python](https://www.python.org/downloads/)

2. Salve o código em um arquivo, por exemplo:

====== MENU PRINCIPAL ======
1 - Cadastrar cliente
2 - Cadastrar produto
3 - Fazer pedido
4 - Mostrar pedidos
5 - Sair
