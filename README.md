# Inventra 📦

Sistema de gerenciamento de produtos e estoque desenvolvido em Python, com persistência de dados em arquivo JSON e interface de menu no terminal.

O Inventra permite cadastrar, consultar, filtrar, atualizar e excluir produtos, além de identificar itens com estoque baixo, oferecendo uma estrutura simples para o controle de informações de um estoque.

## Funcionalidades

- [x] Cadastro de produtos
- [x] Listagem de produtos
- [x] Busca de produtos por ID
- [x] Busca de produtos por nome (parcial, sem diferenciar maiúsculas de minúsculas)
- [x] Filtro de produtos por categoria
- [x] Alerta de estoque baixo (produtos com quantidade igual ou menor que um limite)
- [x] Atualização de informações dos produtos
- [x] Exclusão de produtos, com confirmação
- [x] Geração automática de IDs
- [x] Persistência de dados em JSON
- [x] Validação de campos vazios, preços, quantidades e IDs
- [x] Verificação do arquivo de dados ao iniciar (registros inválidos são descartados)
- [x] Organização do código em módulos

## Tecnologias utilizadas

- **Python 3.10+** (utiliza `match/case`)
- **JSON** para armazenamento e persistência de dados
- **Git e GitHub** para versionamento e hospedagem do projeto

## Estrutura do projeto

```text
Inventra/
│
├── main.py                # Menu principal e ponto de entrada
├── gerenciador.py         # Classe GerenciarProdutos (regras e operações)
├── produto.py             # Classe Produto (modelo de dados)
├── inventra_dados.json    # Banco de dados (arquivo JSON)
└── README.md
```

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Exibe o menu, lê a opção escolhida e chama o método correspondente |
| `gerenciador.py` | Contém todas as operações sobre os produtos e a leitura/gravação do JSON |
| `produto.py` | Define a classe `Produto` e converte o objeto em dicionário (`to_dict`) |

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

> Execute o programa **de dentro da pasta do projeto**: o arquivo `inventra_dados.json` é procurado na pasta em que o comando é executado.

## Menu

```text
======ARMAZEM======
1 - Cadastrar Produto
2 - Listar Produtos
3 - Buscar Produto Pelo ID
4 - Buscar Produto Pelo Nome
5 - Atualizar Produto
6 - Excluir Produto
7 - Filtrar Por Categoria
8 - Alerta De Estoque Baixo
9 - Sair
```

| Opção | O que faz |
|---|---|
| 1 | Cadastra um produto (nome, preço, quantidade e categoria); o ID é gerado automaticamente |
| 2 | Lista todos os produtos cadastrados |
| 3 | Busca um produto pelo ID |
| 4 | Busca produtos cujo nome contém o texto digitado |
| 5 | Atualiza o nome, o preço, a quantidade ou a categoria de um produto |
| 6 | Exclui um produto após confirmação (`s`/`n`) |
| 7 | Lista os produtos de uma categoria |
| 8 | Lista os produtos com estoque igual ou menor que o limite informado |
| 9 | Encerra o programa |

## Armazenamento de dados

Os produtos são armazenados no arquivo `inventra_dados.json`.

Cada produto possui as seguintes informações:

- ID
- Nome
- Preço
- Quantidade disponível
- Categoria

Exemplo de registro:

```json
{
    "ID": 1,
    "Nome": "Teclado mecânico RGB",
    "Preço": 249.9,
    "Quantidade": 15,
    "Categoria": "Periféricos"
}
```

Os dados são mantidos no arquivo mesmo após o encerramento do programa.

O repositório acompanha um **banco de exemplo com 18 produtos em 8 categorias**, incluindo alguns itens com estoque baixo. Para testar o alerta de estoque (opção 8), experimente o limite `5`. Se quiser começar do zero, basta substituir o conteúdo do arquivo por `[]`.

## Validações

- Nome e categoria não podem ficar vazios
- Preço deve ser um número maior que zero
- Quantidade deve ser um número inteiro maior ou igual a zero
- IDs devem ser números inteiros positivos
- Ao iniciar, o programa verifica o arquivo de dados e descarta registros incompletos ou com valores inválidos
- Entradas inválidas apenas repetem a pergunta, sem interromper o programa

## Objetivo

Projeto desenvolvido com o objetivo de praticar conceitos de programação orientada a objetos, manipulação de arquivos, persistência de dados, estruturas de dados, modularização e lógica de programação em Python.

## Melhorias futuras

- [ ] Controle de entrada e saída de mercadorias
- [ ] Cálculo do valor total do estoque
- [ ] Migração do JSON para SQLite
- [ ] Integração com SQLAlchemy
- [ ] Desenvolvimento de uma API REST com FastAPI

---

**Status:** Em desenvolvimento.