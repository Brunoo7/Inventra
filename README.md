# Inventra — Gerenciador de Estoque

Sistema de gerenciamento de estoque desenvolvido em Python, com persistência de dados em arquivos JSON. O projeto permite cadastrar, consultar, atualizar e excluir produtos, além de realizar operações de controle e acompanhamento do estoque.

O Inventra começou como um exercício prático de programação orientada a objetos e evoluiu para uma aplicação de gerenciamento de estoque via terminal.

## Funcionalidades

- **Cadastro de produtos:** registra ID, nome, preço, quantidade e categoria.
- **Listagem:** exibe os produtos cadastrados.
- **Busca por ID:** localiza produtos pelo identificador.
- **Busca por nome:** permite pesquisas utilizando partes do nome, sem diferenciar letras maiúsculas e minúsculas.
- **Atualização:** permite modificar os dados de produtos cadastrados.
- **Exclusão:** remove produtos mediante confirmação.
- **Filtro por categoria:** exibe produtos de uma categoria específica.
- **Alerta de estoque baixo:** identifica produtos cuja quantidade está abaixo de um limite definido.
- **Valor total do estoque:** calcula o valor financeiro total dos produtos disponíveis.

## Tecnologias utilizadas

- Python
- Programação Orientada a Objetos (POO)
- JSON
- Manipulação de arquivos
- Git e GitHub

## Estrutura do projeto

```text
Inventra/
│
├── main.py
├── produto.py
├── gerenciador.py
├── inventra_dados.json
└── README.md
```

## Como executar

**1. Clone o repositório:**

```bash
git clone https://github.com/Brunoo7/Inventra.git
```

**2. Entre na pasta do projeto:**

```bash
cd Inventra
```

**3. Execute a aplicação:**

```bash
python main.py
```

Não é necessário instalar bibliotecas externas. O projeto utiliza recursos nativos do Python.

## Persistência e validação de dados

Os dados dos produtos são armazenados em um arquivo JSON, permitindo que as informações permaneçam disponíveis após o encerramento da aplicação.

O sistema também realiza validações para lidar com situações como:

- Arquivo JSON inexistente.
- Arquivo com conteúdo inválido ou corrompido.
- Estrutura de dados inesperada.
- Produtos com campos ausentes ou valores inválidos.
- Entradas incorretas fornecidas pelo usuário.

## Objetivos de aprendizado

O desenvolvimento do Inventra permitiu praticar:

- Criação e organização de classes.
- Encapsulamento de responsabilidades.
- Métodos e atributos de instância.
- Manipulação de listas e dicionários.
- Leitura e escrita de arquivos JSON.
- Tratamento de exceções.
- Validação e integridade de dados.
- Organização de um projeto Python em múltiplos módulos.