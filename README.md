# Inventra 📦

Sistema de gerenciamento de produtos e estoque desenvolvido em Python, com persistência de dados em arquivos JSON.

O Inventra permite cadastrar, consultar, atualizar e excluir produtos, oferecendo uma estrutura simples para o controle de informações de um estoque.

## Funcionalidades

- [x] Cadastro de produtos
- [x] Listagem de produtos
- [x] Busca de produtos por ID
- [x] Atualização de informações dos produtos
- [x] Exclusão de produtos
- [x] Geração automática de IDs
- [x] Persistência de dados em JSON
- [x] Validação de campos vazios
- [x] Validação de preços e quantidades

## Tecnologias utilizadas

- **Python 3**
- **JSON** para armazenamento e persistência de dados
- **Git e GitHub** para versionamento e hospedagem do projeto

## Estrutura do projeto

```text
Inventra/
│
├── main.py
├── inventra_dados.json
└── README.md
```

## Como executar

1. Clone o repositório:

```bash
git clone https://github.com/Brunoo7/Inventra.git
```

2. Entre na pasta do projeto:

```bash
cd Inventra
```

3. Execute o programa:

```bash
python main.py
```

> Não é necessário instalar bibliotecas externas. O projeto utiliza recursos nativos do Python.

## Armazenamento de dados

Os produtos são armazenados no arquivo `inventra_dados.json`.

Cada produto possui as seguintes informações:

- ID
- Nome
- Preço
- Quantidade disponível
- Categoria

Os dados são mantidos no arquivo mesmo após o encerramento do programa.

## Objetivo

Projeto desenvolvido com o objetivo de praticar conceitos de programação orientada a objetos, manipulação de arquivos, persistência de dados, estruturas de dados e lógica de programação em Python.

## Melhorias futuras

- [ ] Organização do código em módulos
- [ ] Pesquisa de produtos por nome
- [ ] Filtros por categoria
- [ ] Identificação de produtos com estoque baixo
- [ ] Controle de entrada e saída de mercadorias
- [ ] Cálculo do valor total do estoque
- [ ] Migração do JSON para SQLite
- [ ] Integração com SQLAlchemy
- [ ] Desenvolvimento de uma API REST com FastAPI

---

**Status:** Em desenvolvimento.