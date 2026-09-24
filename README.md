# 🧮 Mini Calculadora Distribuída

Projeto acadêmico desenvolvido em **Python** com o objetivo de demonstrar o funcionamento de uma aplicação distribuída utilizando **RPC (Remote Procedure Call)**.

A aplicação é dividida em duas partes: um **cliente**, responsável pela interação com o usuário, e um **servidor RPC**, responsável por executar as operações matemáticas solicitadas pelo cliente.

---

## 📌 Sobre o projeto

A **Mini Calculadora Distribuída** utiliza o protocolo **XML-RPC** para permitir que o cliente solicite a execução de funções que estão disponíveis no servidor.

O usuário escolhe uma operação matemática, informa dois valores e o cliente envia a solicitação ao servidor. O servidor executa a operação e retorna o resultado.

### 🔄 Funcionamento

```text
┌──────────────────────┐
│       CLIENTE        │
│   cliente_rpc.py     │
└──────────┬───────────┘
           │
           │ XML-RPC
           │ localhost:8000
           ▼
┌──────────────────────┐
│      SERVIDOR RPC    │
│   servidor_rpc.py    │
└──────────┬───────────┘
           │
           ▼
     Executa operação
           │
           ▼
      Retorna resultado
           │
           └──────────────► Cliente
```

---

## 🎯 Objetivos

- Compreender o conceito de sistemas distribuídos.
- Utilizar RPC para comunicação entre aplicações.
- Implementar comunicação utilizando **XML-RPC**.
- Separar as responsabilidades entre cliente e servidor.
- Desenvolver operações matemáticas disponibilizadas remotamente.
- Compreender o funcionamento de chamadas de procedimentos remotos.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| 🐍 Python | Linguagem de programação |
| 🔗 XML-RPC | Comunicação entre cliente e servidor |
| 🖥️ `SimpleXMLRPCServer` | Implementação do servidor RPC |
| 📡 `xmlrpc.client` | Comunicação do cliente com o servidor |
| 🐙 GitHub | Versionamento e armazenamento do projeto |

---

## 📂 Estrutura do projeto

```text
mini-calculadora-distribuida/
│
├── cliente_rpc.py
├── servidor_rpc.py
└── README.md
```

### 📄 `cliente_rpc.py`

Responsável pela interação com o usuário.

O cliente apresenta um menu com as operações disponíveis e realiza chamadas remotas ao servidor.

### 📄 `servidor_rpc.py`

Responsável por disponibilizar as funções matemáticas através do XML-RPC.

As funções registradas no servidor são:

- `soma()`
- `subtracao()`
- `multiplicacao()`
- `divisao()`

---

## ➕ Operações disponíveis

| Opção | Operação | Função RPC |
|:---:|---|---|
| `1` | Soma | `soma()` |
| `2` | Subtração | `subtracao()` |
| `3` | Multiplicação | `multiplicacao()` |
| `4` | Divisão | `divisao()` |
| `0` | Encerrar | - |

O servidor também possui tratamento para **divisão por zero**.

---

## ▶️ Como executar

### 1. Pré-requisito

É necessário ter o **Python 3** instalado.

Para verificar a instalação:

```bash
python --version
```

ou:

```bash
python3 --version
```

---

### 2. Iniciar o servidor

Abra um terminal dentro da pasta do projeto e execute:

```bash
python servidor_rpc.py
```

O servidor deverá apresentar:

```text
Servidor RPC ativo na porta 8000...
```

O servidor ficará aguardando as solicitações do cliente.

---

### 3. Executar o cliente

Abra **outro terminal**, na mesma pasta, e execute:

```bash
python cliente_rpc.py
```

Será exibido o menu:

```text
=== MINI CALCULADORA DISTRIBUÍDA ===
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
0 - Sair
```

---

## 💻 Exemplo de execução

### Servidor

```text
Servidor RPC ativo na porta 8000...
```

### Cliente

```text
=== MINI CALCULADORA DISTRIBUÍDA ===
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
0 - Sair

Escolha: 1
Digite o primeiro valor: 10
Digite o segundo valor: 5

Resultado: 10 + 5 = 15.0
```

Outro exemplo:

```text
Escolha: 3
Digite o primeiro valor: 8
Digite o segundo valor: 4

Resultado: 8 * 4 = 32.0
```

---

## 🌐 Comunicação RPC

Neste projeto, o cliente cria uma conexão com o servidor através de:

```python
xmlrpc.client.ServerProxy("http://localhost:8000/")
```

Dessa forma, o cliente consegue chamar remotamente funções que estão registradas no servidor.

Por exemplo:

```python
resultado = servidor.soma(a, b)
```

A chamada é enviada ao servidor RPC, que executa:

```python
def soma(a, b):
    return a + b
```

O resultado é então retornado para o cliente.

---

## 🔐 Tratamento de erros

O cliente possui tratamento para situações como:

- Entrada de valores que não são numéricos.
- Servidor RPC desligado.
- Falhas de comunicação.
- Opções inválidas.

O servidor também trata a tentativa de divisão por zero:

```python
if b == 0:
    return "Erro: divisão por zero"
```

---

## 📚 Conceitos estudados

Este projeto permite colocar em prática conceitos relacionados a:

- Sistemas distribuídos
- Arquitetura cliente-servidor
- RPC (Remote Procedure Call)
- XML-RPC
- Comunicação entre processos
- Chamadas de funções remotas
- Separação entre cliente e servidor
- Tratamento de erros

---

## 🎓 Finalidade acadêmica

Este projeto foi desenvolvido como atividade prática acadêmica com o objetivo de aplicar conceitos de **sistemas distribuídos** utilizando a linguagem Python.

A implementação demonstra, de forma prática, como uma aplicação cliente pode solicitar a execução de operações disponibilizadas por um servidor remoto através de RPC.

---

## 👨‍💻 Autor

**Renan Carneiro**

Estudante de Análise e Desenvolvimento de Sistemas.

---

## 📌 Status

**Concluído ✔️**

Projeto desenvolvido para fins acadêmicos e de estudo sobre sistemas distribuídos e comunicação RPC.

---

⭐ Se este projeto foi útil para seus estudos, considere deixar uma estrela no repositório!
