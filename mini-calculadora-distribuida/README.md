# Mini Calculadora Distribuída

Atividade prática sobre **RPC (Remote Procedure Call)** usando Python e apenas recursos da biblioteca padrão.

## Objetivo

Demonstrar a diferença entre comunicação manual por sockets e uma chamada de procedimento remoto. O cliente solicita operações matemáticas e o servidor executa os cálculos.

## Tecnologias

- Python 3
- `xmlrpc.server`
- `xmlrpc.client`
- Nenhuma biblioteca externa

## Estrutura

```text
mini-calculadora-distribuida/
├── servidor_rpc.py
├── cliente_rpc.py
└── README.md
```

## Como executar

Abra dois terminais na pasta do projeto.

### Terminal 1: servidor

```bash
python servidor_rpc.py
```

Saída esperada:

```text
Servidor RPC ativo na porta 8000...
```

### Terminal 2: cliente

```bash
python cliente_rpc.py
```

O cliente exibirá um menu para realizar soma, subtração, multiplicação e divisão.

## Exemplo

Com os valores 10 e 5:

```text
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```

## Análise da atividade

1. **Qual processo possui as funções `soma()`, `subtracao()`, `multiplicacao()` e `divisao()`?**  
   O processo servidor possui e executa essas funções.

2. **O cliente possui o código dessas operações?**  
   Não. O cliente apenas solicita a execução das funções por RPC.

3. **Qual endereço e porta identificam o serviço?**  
   Na execução local, o serviço é identificado por `localhost` na porta `8000`.

4. **Quem inicia a chamada?**  
   O cliente inicia a chamada RPC.

5. **O resultado foi calculado no cliente ou no servidor?**  
   No servidor. O cliente recebe o resultado após a execução remota.

6. **Qual a diferença em relação aos sockets TCP?**  
   Com sockets TCP, normalmente o programador precisa controlar diretamente a conexão e o envio/recebimento das mensagens. Com RPC, a comunicação é abstraída e o cliente pode chamar uma função remota de forma semelhante a uma chamada de função local.

## Experimento de falha

Se o servidor for encerrado com `Ctrl + C` e o cliente for executado novamente, a chamada não poderá ser atendida e ocorrerá uma falha de comunicação.

Isso acontece porque a função aparentemente local (`servidor.soma(...)`, por exemplo) depende de um processo remoto disponível. Portanto, uma chamada RPC continua sujeita a indisponibilidade, falhas de comunicação e latência.

## Desafio 1

Foi adicionada a operação remota `divisao(a, b)`, incluindo tratamento para divisão por zero.

## Desafio 2

O cliente foi transformado em um menu interativo. As operações continuam sendo executadas remotamente pelo servidor.

## Desafio extra: dois computadores

Para executar entre computadores da mesma rede, o servidor pode ser configurado para escutar em todas as interfaces:

```python
SimpleXMLRPCServer(("0.0.0.0", 8000), allow_none=True)
```

No cliente, substitua `localhost` pelo IPv4 do computador que executa o servidor:

```python
xmlrpc.client.ServerProxy("http://IP_DO_SERVIDOR:8000/")
```

O firewall do sistema operacional pode precisar permitir a comunicação pela porta 8000.
