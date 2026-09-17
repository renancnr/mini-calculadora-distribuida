import xmlrpc.client

servidor = xmlrpc.client.ServerProxy("http://localhost:8000/")

def executar():
    while True:
        print("\n=== MINI CALCULADORA DISTRIBUÍDA ===")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "0":
            print("Programa encerrado.")
            break

        if opcao not in {"1", "2", "3", "4"}:
            print("Opção inválida.")
            continue

        try:
            a = float(input("Digite o primeiro valor: "))
            b = float(input("Digite o segundo valor: "))

            if opcao == "1":
                resultado = servidor.soma(a, b)
                operacao = "+"
            elif opcao == "2":
                resultado = servidor.subtracao(a, b)
                operacao = "-"
            elif opcao == "3":
                resultado = servidor.multiplicacao(a, b)
                operacao = "*"
            else:
                resultado = servidor.divisao(a, b)
                operacao = "/"

            print(f"Resultado: {a:g} {operacao} {b:g} = {resultado}")

        except ValueError:
            print("Erro: digite valores numéricos.")
        except ConnectionRefusedError:
            print("Erro: o servidor RPC não está em execução.")
            break
        except OSError as erro:
            print(f"Erro de comunicação com o servidor: {erro}")
            break

if __name__ == "__main__":
    executar()
